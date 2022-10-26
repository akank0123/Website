document.getElementById("callFormBtn").addEventListener("click",function(){
    document.querySelector(".form").style.display = "flex";
})
document.querySelector(".closed").addEventListener("click",function(){
    document.querySelector(".form").style.display = "none";
})
function myFunction(){
    var x=document.getElementById("app");
    if(x.style.display ==="flex"){
        x.style.display="block";
    }else{
        x.style.display="none"
    }
}