//name='alex'   全局变量
//var name ='alex'    局部变量

//基本函数
/*
function Foo(name){
	var arg2 = arguments[1]; //默认参数
	console.log(name);
	console.log(arg2);
}

Foo('alex','张倩')


//建议定义全局变量的时候使用window.alert('xxxx')

//匿名函数
var tmp = function(){
	
}
*/
//自执行函数
(function(name){
	console.log(name)
})('zhangqian')



