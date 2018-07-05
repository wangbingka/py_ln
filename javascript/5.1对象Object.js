// 对象(Object),每个对象都会有属性(property)，例如苹果，属性有颜色、味道等等
// 对象(Object)，还会有方法，例如对象汽车，，会有方法(method),可以前进，可以后退,有时候也可以成为属性(property)
// 对象(Object),除了数字,字符串，undefined，bool,其他都是对象

//创建一个空对象
var beyond = {};

//对象的属性
beyond.formedIn = '1983';

//对象的属性，另一种定义方法
beyond['foundIn'] = '香港';

console.log(beyond);

//创建对象时，可以直接设置属性
var beyond = {members:4,formedIn:'1983',foundIn:'香港'};
console.log(beyond);


//创建对象时，可以直接设置属性，属性的值可以时任何数据类型，包括数组
var beyond = {members:4,formedIn:'1983',foundIn:'香港',
                artist:['黄家驹','黄家强','黄贯中','叶世荣']
                };
console.log(beyond);

//想要访问对象的数组
beyond.artist
// 返回对象的所有制

beyond.artist[0];
// 返回对象的第一个值:'黄家驹'

beyond.foundIn = '中国香港';
// 更新对象里面属性的值
console.log(beyond);

delete beyond.foundIn
// 删除对象的属性和值
console.log(beyond);

//为对象添加方法,
beyond.showArtist = function () {
    for (var i = 0;i<this.artist.length;i++){
        document.writeln(this.artist[i]);
    }

};

//对象方法，输出到页面中
beyond.showArtist();

//循环输出对象的属性
var property;
for (property in beyond){
    if (typeof beyond[property] != 'function'){
       console.log(beyond[property]);
    }

}

console.log(beyond)