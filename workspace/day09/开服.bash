#!/bin/bash

custom(){
		IP=$1
        User=root
        MYSQLPath=/home/pirate/programs/mysql
        PirateDB="show databases like 'pirate%'" 
		ssh $IP "$MYSQLPath/bin/mysql  -u$User -e '$PirateDB'" | grep -v Database
}
ShowPirate(){
        custom
        IP=$1
        ssh $IP "$MYSQLPath/bin/mysql  -u$User -e \"$PirateDB\"" | grep -E "pirate[0-9]"
}

ShowTmp(){
        custom
        IP=$1
        ssh $IP "$MYSQLPath/bin/mysql  -u$User -e \"$TmpDB\"" | grep -E "tmp[0-9]"
}

sortpiratedb(){
        >/tmp/db_ip_piratenum
        for h in `awk '$3~/mdb0[1-7]/{print $1}' ~/optool/host.list`
        do
                custom 
                echo -ne "$h `ShowPirate $h | wc -l` \n" >>/tmp/db_ip_piratenum
        done
		datacsvnum=`cat data.csv | wc -l`
		for h in `seq $datacsvnum`
		do
				sortr=`cat /tmp/db_ip_piratenum | sort -k2.1,2.2nr| tail -1`
				num1=`echo $sortr | awk '{print $NF}'`
				num2=`expr $num1 + 1`
				echo $sortr
				echo $sortr | sed -i 's/$num1/$num2/g'
		done			
}
sortpiratedb

