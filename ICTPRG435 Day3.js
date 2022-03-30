// document.querySelector('#mybutton').addEventListener('mouseover', greet);
// function greet(){
//     console.log('Hello')
//   }



// document.querySelector('#mybutton').addEventListener('mouseover', () => {greet("hello world")});

// function greet(x) {
//     console.log(x)
// }



// document.querySelector('#mybutton').addEventListener('mouseover', () => {
//     console.log("Hello")
//     console.log("123")
// // });

// let btn = document.querySelector('#mybutton')
// btn.addEventListener("click", greet);

// function greet(e) {
//     console.log(e);
//     console.log(e.altKey);
//     console.log(e.target.innerHTML);
//     console.log(e.key)
// }

// let key=document.querySelector("#test")

// key.addEventListener("keydown", keys)

// function keys(e) {
//     let char = console.log(e.key)
//     if (char =="A") {
//         alert('"A" had been pressed')
//     }

// }



// draw circle with radius 10, fill with red
// draw a 30x20 rectangle, fill with green
// draw a blue horizontal line across the center of the canvas

// var canvas = document.getElementById("myCanvas");
// var ctx = canvas.getContext("2d");
// ctx.beginPath()
// ctx.fillStyle = "#FF0000";
// ctx.arc(100, 50, 10, 0, 2 * Math.PI);
// ctx.fill()
// ctx.stroke();


// ctx.beginPath()
// ctx.fillStyle = "green";
// ctx.rect(100, 70, 30, 20);;
// ctx.fill()
// ctx.stroke();

// ctx.beginPath()
// ctx.strokeStyle = "blue";
// ctx.moveTo(0, 50);
// ctx.lineTo(200, 50);
// ctx.fill()
// ctx.stroke();


// document.querySelector("#cnfpwd").addEventListener('change', validatePassword);
// function validatePassword(){
// if(document.querySelector("#pwd").value != document.querySelector("#cnfpwd").value) {
// document.querySelector("#cnfpwd").setCustomValidity("Passwords Don't Match");
// document.querySelector("#cnfpwd").reportValidity();
// document.querySelector("#pwd").value ='';
// document.querySelector("#cnfpwd").value ='';
//  }
// else {
// document.querySelector("#cnfpwd").setCustomValidity('');
// document.querySelector("#cnfpwd").reportValidity();
//  }
// }



// draw = document.querySelector("#btn");

// draw.addEventListener("click",drawPattern)

// function drawPattern() {

//     var canvas = document.getElementById("myCanvas");
//     var ctx = canvas.getContext("2d");
//     ctx.beginPath()
//     ctx.fillStyle = "#FF0000";
//     ctx.arc(100, 50, 10, 0, 2 * Math.PI);
//     ctx.fill()
//     ctx.stroke();
//     console.log("a")

// }


// let draw = document.querySelector("#btn");

// draw.addEventListener("click",drawPattern);

// let canvas = document.getElementById("myCanvas");
// let ctx = canvas.getContext("2d");

// function drawPattern() {

//     let x = document.querySelector("#x").value;
//     console.log(x);

//     let y = document.querySelector("#y").value;
//     console.log(y);

//     let xx = document.querySelector("#xx").value;
//     console.log(x);

//     let yy = document.querySelector("#yy").value;
//     console.log(y);


//     ctx.beginPath();
//     ctx.strokeStyle = "blue";
//     ctx.moveTo(x, y);
//     ctx.lineTo(xx, yy);
//     ctx.fill();
//     ctx.stroke();

// }

// let resetButton = document.querySelector("#btn2");
// resetButton.addEventListener("click",restDrawing);

// function restDrawing(){
    
//     ctx.clearRect(0, 0, canvas.width, canvas.height);

// }

// let x = document.querySelector("#startX")

// x.addEventListener("change",function(){

//  if(x.value >400) {
//     alert("x value can't be large than 400")
//  }
//   else {
//       console.log(x.value)
//   }
// })

// let y = document.querySelector("#startY");

// y.addEventListener("change",function(){

//  if(y.value >400) {
//     alert("y value can't be large than 400")
//  }
//   else {
//       console.log(y.value)
//   }
// })



//get p color value 
let p = document.querySelector("#text")
const textColor = p.style.color


// console.log(textColor)



//click button

const btn = document.querySelector("#button")

btn.addEventListener("click", changeColor)

function changeColor(){

   //get user color value
    let input = document.querySelector("#color")
    let inputColor = input.value
    p.style.color = inputColor

}

btn.addEventListener("dblclick", () =>{

    p.style.color = textColor

})
