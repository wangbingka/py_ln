// ‘//’为单行注释标记；
// '/*....*/'为多行注释表示，其中的每一行开头建议加个'*'，为了实际意义，只是让注释更好看



//打开页面时跳出显示对应的内容提示
    // alert('Hellow World!');




//控制台，可以在浏览器控制台编译测试js文件
    /*
    var words = 'Hellow World!';
    console.log(words)
    */

//值的类型：number(数字)，string(字符串)，null(没有值)，undefined(没有定义的值),true(真)，false(假)
// false：0,null,undefined,false这四类；其中值均为true

// 'type0f(变量)'为变量的字符类型
// "+"用于两个数值，结果是两个数字之和，用于两个字符串或者一个字符串一个数值，结果是两个变量的字符合并值
// ‘String’将其他转换为字符串，'parseInt'将对象转换为整数型值，'parseFloat'将对象转换为浮点型
    // var fullName = '王皓', weight=26;
    // typeof(fullName);
    // parseFloat(weight);


// 字符串的内容
var words = '宁浩网是个网站';

words.length;
// 获得'words'的字符串长度,结果为7

words.charAt(0);
// 获得'words'索引为0的字符串，结果为‘宁’

words.charAt(words.length-1);
// 获得'words'最后一个索引的字符串，结果为'站'

words.indexOf('网');
// 获得'words'第一个'网'字符的索引

words.lastIndexOf('网');
// 获得'words'最后一个'网'字符的索引

words.substring(0,3);
// 获得'words'从索引0到索引3之间的字符，包括索引0，不包括索引3

words.replace('宁浩网','Hulu');
// 将'words'中的字符'宁浩网',替换成字符串'Hulu'

var words1 = '宁浩网,是个网站';
var newWords1 = words1.split(',');
// 将'words1',从括号中','处，分割成多部分组成一个数组newWords1

// 2.4Array数组

var trackCD1 = [];
typeof(trackCD1);

trackCD1 = ['长城','农民','不可一世'];
//往数组中添加元素

trackCD1.length;
// 数组中元素的数量

trackCD1[3] = 'Bye-Bye';
// 如果数组中已有这个索引，会更改索引对应的值，如果没有则会添加这个元素

trackCD1.push('遥望','温暖的的家乡');
// 会自动添加元素，添加在最后面

trackCD1.pop();
// 会删除最后一个元素，并得到这个删除的元素
trackCD1.shift();
// 会删除第一个元素，并得到这个删除的元素

delete trackCD1[3];
// 会删除这个索引3的元素，但是索引还在，只不过变成一个undefined的元素，元素数量保持不变

trackCD1.splice(3);
// 会彻底删除这个索引3的元素，这个位置不再存在，元素数量也会减少

var trackCd2 = ['可否冲破','快乐王国'];
var tracks = trackCD1.concat(trackCd2);
// concat，合并前后两个数组为一个数组

