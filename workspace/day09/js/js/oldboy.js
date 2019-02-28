//声明//
alert('oldboy');
//全局变量//
//name = 'alex'//
//局部便量//
//var name = 'alex'//

/**
//函数//
function Foo(name){
		var args = arguments[1];
		//默认参数
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

//自执行函数//
/**
(function(){
	console.log('zhangqian');
})()
*/
/**
//形参//
(function(name){
	console.log(name);
})('han tao')
*/

/**
//声明数组//
var  array = [1,2,3,4]
//var  array = Array(1,2,3,4)
//数组里追加
array.push('alex');
console.log(array)
//首部追加
array.unshift('old')
console.log(array)
//第二个数时要为0才能为追加，别的值为删除追加
array.splice(3,0,'boy1')
console.log(array)
//在某个位置追加数值
array[100] = 'zhangqian'
console.log(array[99])
console.log(array[100])
*/

//for循环//
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

