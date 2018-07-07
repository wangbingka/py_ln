//  window.onload =function () {}，这一句用于保证所有界面被加载完成后再进行内部的操作

// onclick，点击鼠标，onmouseover，放在鼠标上，onmouseout，离开鼠标。在Properities上可以查看相关的事件，常见都是以'on'开头
// var btn = document.querySelector('.btn');
// btn.onclick = function () {
//     console.log('被点了!');
// };
// btn.onmouseover = function () {
//     console.log('谁在上面!');
// };
// btn.onmouseout = function () {
//     console.log('离开了!');
// };

window.onload =function () {
    var btn = document.querySelector('.btn');

    /* event，可以保存此时的操作以及相关的属性，可以后面调用 ,*/
    function showMessage(event){
        console.log(event);

    }
    /*
    * addEventListener,添加绑定事件
    * 'click'，一般去掉事件处理程序前面的'on'，就是事件的名称，其他还有'mouseover'、'mouseout'等
    * showMessage，函数，一般是自定义的
    * var listGroup = document.querySelector('.list-group');，最后的list-group为元素的class属性值
    * var lost = document.getElementById('atlas');最后的atlas为元素的id属性
    * 最后的一个false是一种事件传递方式，从内到外，从最里层到最外层传递，ture是相反的从外层到里层
    * */

    btn.addEventListener('click',showMessage,false);

    var listGroup = document.querySelector('.list-group');
    function showeMessage1(event) {
        console.log(event.target.alt);

        /*
          * 停止事件的传播，当如果事件从是从外到内传播时，可以阻止其继续传播
          * 这样就不会触发绑定在子模块上的传播行为
          * */
        event.stopPropagation();
    };
    listGroup.addEventListener('click',showeMessage1,true);

    var atlas = document.getElementById('atlas');
    function showAnotherMessage(event) {
        console.log('点击了atlas!');
    };
    atlas.addEventListener('click',showAnotherMessage,false);





    /*
    btn.onclick = function () {
        console.log('被点了!');
    };
    btn.onmouseover = function () {
        console.log('谁在上面!');
    };
    btn.onmouseout = function () {
        console.log('离开了!');
    };
    */
} ;

// 如果放在window.onload =function () {}，的外面，会因为图片没有加载完成报错
    //     var listGroup = document.querySelector('.list-group');
    //     function showeMessage(event) {
    //         console.log(event.target.alt);
    //     }
    //     listGroup.addEventListener('click',showeMessage,true);
    // };

