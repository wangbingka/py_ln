// switch控制语句
// break停止跳出循环,continue跳出本次循环继续下一次循环,

var weather = '多云';
switch (weather) {
    case '下雨':
        alert('忧郁');
        break;
    case '晴天':
        alert('心情不错');
        break;
    default:
        alert('心情糟糕');
        break;
}