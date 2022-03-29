var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d"); 

document.querySelector("#draw").addEventListener("click", draw);
document.querySelector("#palette").addEventListener("click", myPalette);
document.querySelector("#slider").addEventListener("click", mySlider);
document.querySelector("#number").addEventListener("click", myNumber);
document.querySelector("#shapes").addEventListener("click", myShapes);
document.querySelector("#linearFill").addEventListener("click", myFill);

function draw(){  
  let grd = ctx.createLinearGradient(100, 100, 150, 100);
  grd.addColorStop(0, "green");
  grd.addColorStop(0.5, "blue");
  grd.addColorStop(1, "red");

  if (document.querySelector("#shapes").value == "circle"){

      ctx.beginPath();
      ctx.arc(100, 100, document.querySelector("#slider").value, 0, 2 * Math.PI); 
      ctx.strokeStyle = "black";
      ctx.stroke();
      ctx.fillStyle = document.querySelector("#palette").value; 
      ctx.fill();
  }
  else if (document.querySelector("#shapes").value == "square"){
      ctx.strokeRect(100, 100, 50, 50); 
      if(document.querySelector("#linearFill").checked == true){
        ctx.fillStyle = grd;
      }
      else  ctx.fillStyle = document.querySelector("#palette").value; 
      ctx.strokeStyle = "black";
      ctx.stroke();
      ctx.fillRect(100, 100, 50, 50)    
  }
}

function myPalette(){
  console.log(document.querySelector("#palette").value)
}

function mySlider(){
  console.log(document.querySelector("#slider").value)
}

function myNumber(){
  console.log(document.querySelector("#number").value)
}

function myShapes(){
  console.log(document.querySelector("#shapes").value)
}

function myFill(){
  console.log(document.querySelector("#linearFill").checked)
}


