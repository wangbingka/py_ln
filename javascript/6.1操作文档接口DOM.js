// DOM ,Document Object Model
// 使用html中定义的id，获取整段话,类似定义<li id= 'page-title'> 123dadff </li>
// document.getElementById('id_name')
document.getElementById('page-title');
// 上下两句等同效果
var pageTitle = document.getElementById('page-title');
// 通过pageTitle.属性获取元素各种属性的值

// nodeName，此模块的类型，类似ul,div,li,p等
pageTitle.nodeName
"H1"

// innerText，此模块中网页显示的值
pageTitle.innerText
"Coldplay"

//


// parentNode，此模块，父一级的模块类型
pageTitle.parentNode
<body>​…​</body>​

// previousElementSibling，此模块上一个模块的整体代码组成
pageTitle.previousElementSibling
<script src=​"6.1操作文档接口DOM.js">​</script>​

// nextElementSibling，此模块下一个模块的整体代码组成
pageTitle.nextElementSibling
<p>​乐队于1997年成立于伦敦​</p>​

// 两个属性可以连续通过'.'连接使用，表示此模块下一个模块网页显示的内容值
pageTitle.nextElementSibling.innerText
"乐队于1997年成立于伦敦"


// 直接使用项目的名称，类似ul,div,li,p等，如果有多个值，会按照顺序形成一个list数组,通过索引号可以访问具体的某个元素
document.getElementsByTagName('li');
// 上下两句等同效果
var list = document.getElementsByTagName('li')
list[0];

// 使用定义的class_名称
// querySelector,获取这个class的第一个元素
// querySelectorAll,获取这个class下的所有元素，形成一个数组
document.querySelector('.artist-list li');
var list1 = document.querySelector('.artist-list li');

document.querySelectorAll('.artist-list li');
var list = document.querySelectorAll('.artist-list li');

// list1和list[0]，结果是等同的

var artistList = document.querySelector('.artist-list')
undefined

// childElementCount,此类模块中元素的数量。
artistList.childElementCount
4

// firstElementChild,此类数组元素中的第一个子模块
artistList.firstElementChild
<li>​Chris Martin​</li>​
artistList.firstElementChild.innerText
"Chris Martin"

// 直接更改对应属性的内容
artistList.firstElementChild.innerText = '克里斯 马丁'
"克里斯 马丁"

// lastElementChild,此类数组元素中的最后一个子模块
artistList.lastElementChild
<li>​Will Champion​</li>​


// 创建一个类型为'li'的单元模块
var newMember = document.createElement('li')
undefined

// 创建一个文本显示为'张三'的模块
var newMemberText = document.createTextNode('张三');
undefined

// 将'张三'这个内容模块，作为属性，添加到之前创建的单元模块中
newMember.appendChild(newMemberText)
"张三"

// 将之前创建的模块，添加到class 为'.artist-list'的子模块中，并且只能时最后一个
document.querySelector('.artist-list').appendChild(newMember)
<li>​张三​</li>​

// 使用'insertBefore'和'firstElementChild',将'newMember'模块，插入到class'artist-list'的第一个子模块元素
artistList.insertBefore(newMember,artistList.firstElementChild)
<li>​张三​</li>​

//
var bandMember = document.createElement('h3')
undefined
bandMember.innerText = '乐队成员'
"乐队成员"

// 将这个bandMember模块，插入到子模块的父级，最后一个模块
artistList.parentNode.insertBefore(bandMember,artistList.previousElementSibling)
<h3>​乐队成员​</h3>​
