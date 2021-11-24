const form = document.querySelector("form"),
fileInput = document.querySelector(".file-input"),
progressArea = document.querySelector(".progress-area"),
uploadedArea = document.querySelector(".uploaded-area");
const process=document.querySelector("#process-reset")
var myFormName=document.getElementById("myForm");

myFormName.addEventListener("click", () =>{
  fileInput.click();
});
 var filePath,myFileName;
fileInput.onchange = ({target})=>{
  let file = target.files[0];
  if(file){
    let fileName = file.name;
    console.log(fileName)

    if(fileName.length >= 12){
      let splitName = fileName.split('.');
      fileName = splitName[0].substring(0, 13) + "... ." + splitName[1];
    }
    //  let fileLoaded = Math.floor((loaded / total) * 100);
    //let fileTotal = Math.floor(total / 1000);
   /* let fileSize;
    (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024*1024)).toFixed(2) + " MB";*/
      let progressHTML = `<li class="row">
                          <i class="fas fa-file-alt"></i>
                          <div class="content">
                            <div class="details">
                              <span class="name">${fileName}</span>
                              
                            </div>
                           
                          </div>
                        </li>`;
    uploadedArea.classList.add("onprogress");
    progressArea.innerHTML = progressHTML;
    
  }
}
process.addEventListener("click", () =>{
  let progressHTML = `<li class="row">
                          <i class="fas fa-file-alt"></i>
                          <div class="content">
                            <div class="details">
                              <span class="name">${""}</span>
                              
                            </div>
                           
                          </div>
                        </li>`;
    uploadedArea.classList.add("onprogress");
    progressArea.innerHTML = "";
});

function beforeAfter() {
  document.getElementById('compare').style.width = document.getElementById('slider').value + "%";
}