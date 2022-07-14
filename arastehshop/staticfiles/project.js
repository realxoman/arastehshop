//login
function validate(){
    var email1=document.getElementById("input_email1").value;
    var password1=document.getElementById("input_pass1").value;
    if (email1=="user@gmail.com" && password1=="1234")
    {
        alert("ورود موفقیت آمیز بود. به پروفایل کاربری منتقل میشوید");
        return false;
    }
    else
    {
        alert(" نام کاربری یا رمز اشتباه است");
       
    }
}

//signup
function pass_confirm(){
 var pass2=document.getElementById("input_pass2").value;
 var pass2_repeat=document.getElementById("input_pass2_repeat").value;
 if(pass2 !== pass2_repeat)
 {
    alert("رمز عبور را دوباره وارد کنید");
    

 }
 else{
    
     alert("ثبت نام موفقیت آمیز بود");
     
 }
}



//pay
const productbuttom=document.querySelector(".order_button");
const payment=document.querySelector(".payment");
const close=document.querySelector(".close");

productbuttom.addEventListener("click" , () =>{
    payment.style.display="flex";
});

close.addEventListener("click" , () =>{
    payment.style.display="none";
});

function takmil_sefaresh(){
   var cartpaybutton= document.querySelector(".cartpaybutton");
   alert ("امکان انتقال به صفحه بانک وجود ندارد");

}

