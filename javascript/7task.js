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
 　　var zhangHao = document.getElementById('zhanghao');
     var mimaPd = document.getElementById('mima').value;
     var errorMessage = document.querySelector('.error');
 　　if(zhangHao.value === ""){ //输入不能为空
     errorMessage.innerHTML = '账号不能为空';
     errorMessage.style.display = "block";
 // 　　　　 　　　　alert("账号不能为空!");
　　　　return false;
　　}else if(!filter.test(zhangHao.value)){
     errorMessage.innerHTML = '账号格式错误!';
     errorMessage.style.display = "block";
 // 　　　　alert("账号格式错误!");
　　　　return false;
　　}else if ((mimaPd.length>11)||(mimaPd.length<6)) {
     errorMessage.innerHTML = '密码长度错误!';
     errorMessage.style.display = "block";
        // alert("密码长度错误!");
        return false;
        } else {
     window.location.href="7task.html";
   }　
 }
    veryfy.addEventListener('click',check,false);
};
