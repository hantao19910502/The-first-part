#!/usr/bin/env python
#_*_coding:utf-8_*_

#!/usr/bin/env python
# -*- coding=UTF-8 -*-

from subprocess import Popen,PIPE
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('args.conf')

def runCommand(name):
        process =Popen(name,shell=True,stdout=PIPE,stderr=PIPE)
        out=process.stdout.read()
        if out:
                return out
        else:
                return process.stderr.read()

MDB_LIST=[]
SDB_LIST=[]
sdb_index=[]
mdb_index=[]
sdb=runCommand(config.get('IP_SECTION','SDB_HOST'))
mdb=runCommand(config.get('IP_SECTION','MDB_HOST'))
main_host=runCommand(config.get('IP_SECTION','MAIN_HOST'))
MAIN_LIST=main_host.splitlines()
logic=runCommand(config.get('IP_SECTION','LOGIC'))
LOGIC_LIST=logic.splitlines()
MYSQL_USER=config.get('USER','MYSQL_USER')

DB_MAX_COUNT=config.getint('OTHER','DB_MAX_COUNT')
MYSQL_PASS=config.get('USER','MYSQL_PASS')
for sdbs in sdb.splitlines():
    SDB_LIST.append(sdbs.split("\t")[0])
    sdb_index.append(sdbs.split("\t")[1])
for mdbs in mdb.splitlines():
    MDB_LIST.append(mdbs.split("\t")[0])
    mdb_index.append(mdbs.split("\t")[1])
if mdb_index != sdb_index:
    raise Exception("mdbip without corresponding sdbip") 