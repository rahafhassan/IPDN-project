// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()

function makeGrid(event){
    
    event.preventDefault();

    //variabls name
    var height = document.getElementById("inputHeight").value;
    var width = document.getElementById("inputWidth").value;
    var tabl = document.getElementById("pixelCanvas");
    tabl.innerHTML="";

    for (var r=0; r<height; r++){
        var row = document.createElement("tr");
        for (var m=0; m<width; m++){
            var cell = document.createElement("td");
            row.appendChild(cell);
        }
        tabl.appendChild(row);
    }
 
}

function makecolor(event){
    if (event.target.nodeName=="TD"){
       var colorcell=document.getElementById("colorPicker").value;
       event.target.style.backgroundColor=colorcell;
       console.log("clicked");

    }
    

}
document.getElementById("pixelCanvas").addEventListener("click",makecolor(event));