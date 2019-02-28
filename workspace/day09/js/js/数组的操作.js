//数组的方法
/*
声明，如：
    var array = Array() 或 var array = []
 
添加
    obj.push(ele)                   追加
    obj.unshift(ele)                最前插入
    obj.splice(index,0,'content')   指定索引插入
 
移除
    obj.pop()                       数组尾部获取
    obj.shift()                     数组头部获取
    obj.splice(index,count)         数组指定位置后count个字符
 
切片
    obj.slice(start,end)           
 
合并
    newArray ＝ obj1.concat(obj2)   
 
翻转
    obj.reverse()
 
字符串化
    obj.join('_')
 
长度
    obj.length
	
字典是一种特殊的数组
*/



//举例：
//var array = [1,2,3,4]
var array = Array(1,2,3,4)
array.push('hantao')
console.log(array)
array.unshift('hantao1')
console.log(array)
array.splice(1,0,'hantao2')
console.log(array)
array.splice(100,0,'hantao2')  //索引为100的位置追加一个元素
//console.log(array)
console.log(array[98])
console.log(array[99])
console.log(array[101])










