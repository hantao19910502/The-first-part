//����//
alert('oldboy');
//ȫ�ֱ���//
//name = 'alex'//
//�ֲ�����//
//var name = 'alex'//

/**
//����//
function Foo(name){
		var args = arguments[1];
		//Ĭ�ϲ���
		var name = 'hantao';
		console.log(name);
		console.log(args);
		
}
function Bar(){
	console.log(name);
}
Foo('han','26')
Bar()
*/

//��ִ�к���//
/**
(function(){
	console.log('zhangqian');
})()
*/
/**
//�β�//
(function(name){
	console.log(name);
})('han tao')
*/

/**
//��������//
var  array = [1,2,3,4]
//var  array = Array(1,2,3,4)
//������׷��
array.push('alex');
console.log(array)
//�ײ�׷��
array.unshift('old')
console.log(array)
//�ڶ�����ʱҪΪ0����Ϊ׷�ӣ����ֵΪɾ��׷��
array.splice(3,0,'boy1')
console.log(array)
//��ĳ��λ��׷����ֵ
array[100] = 'zhangqian'
console.log(array[99])
console.log(array[100])
*/

//forѭ��//
/**
var array = [11,22,33,44]
var dic = {name:'hantao',age:26}

for (var item in array){
	console.log(item)
	console.log(array[item])
}
*/
var a = '0123456789'
for (var i=0;i<10;i++){
	console.log(i)
	console.log(a[i])
}

