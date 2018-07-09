window.onload =function () {
    var create = document.getElementById("login");
    var closeLogin = document.getElementById("close");
    function showLogin(){
        var loginPage = document.getElementById("login-page");
        loginPage.style.display = "block";
    };
    function hideLogin(){
        var loginPage = document.getElementById("login-page");
        loginPage.style.display = "none";
    };
    create.addEventListener('click',showLogin,false);
    closeLogin.addEventListener('click',hideLogin,false);


    var veryfy = document.getElementById('veryfy');
    function check(){
　　 var filter = /(^(1[35678]\d{9})$)|(^[a-z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*$)/i;
 　　var zhangHao = document.getElementById('zhanghao').value;
 　　if(zhangHao === ""){ //输入不能为空
 　　　　alert("账号不能为空!");
　　　　return false;
　　}else if(!filter.test(zhangHao)){
 　　　　alert("账号格式错误!");
　　　　return false;
　　}else{
　　　　return true;
　　}
 }
    veryfy.addEventListener('click',check,false);
};
