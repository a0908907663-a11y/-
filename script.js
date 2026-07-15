function login(event){

event.preventDefault();


let email=document.getElementById("email").value;

let password=document.getElementById("password").value;


if(email==="" || password===""){

alert("يرجى إدخال البريد الإلكتروني وكلمة المرور");

}

else{

alert("تم تسجيل الدخول بنجاح");

window.location.href="home.html";

}

}



function sendMessage(event){

event.preventDefault();

alert("تم إرسال رسالتك بنجاح، شكراً لتواصلك معنا ❤️");

}