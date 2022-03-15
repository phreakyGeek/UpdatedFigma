function gotoDashboard(){
    window.open("./dashboard.html","_self")
}
function myClick() {
    window.open("./dashboard.html","_self");
}
function goToLogin(){
    window.open("./index.html","_self");
}
function goToAddEdit(){
    window.open("./addEdit.html","_self");
}
function goTonewUser(){
    window.open("./newUser.html","_self");
}
function changePart(){
    window.open("./changePart.html","_self");
}
function setupPage(){
    window.open("./setup.html","_self");
}
function configButton(){
    let configForm = document.getElementById("configForm");
    let settingForm = document.getElementById("settingForm");
    let configButton = document.getElementsByClassName("configButton");
    settingForm.style.display = "none";
    configForm.style.display = "block";
    //configButton[0].style.backgroundColor = "white";
    console.log(configButton[0].style.backgroundColor);
}
function settingButton(){
    let configForm = document.getElementById("configForm");
    let settingForm = document.getElementById("settingForm");
    let configButton = document.getElementsByClassName("configButton");
    configForm.style.display = "none";
    settingForm.style.display = "block";
}
// function login()