windows.load(){
    function showForm() {
    var create = document.getElementById("login");
    // var bg = document.getElementsByClassName("background")[0];
    var loginPage = document.getElementById("login-page");
    var links = document.getElementsByClassName("close");
    for(var i=0;i<links.length;i++) {
        links[i].onclick = function() {
        loginPage.style.display = "none";
        // bg.style.display = "none";
        }
    }
    create.onclick = function() {
        loginPage.style.display = "block";
        // bg.style.display = "block";
    }

}
}
