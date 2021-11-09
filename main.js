const inputFileDefault = document.getElementById('inputFileDefault');
const chooseFileBtn = document.getElementById('chooseFileBtn');
const fileText = document.getElementById('fileText');

const imgBefore = document.getElementById('imgBefore');
const imgAfter = document.getElementById('imgAfter');
const imgWrapper = document.querySelector(".imgWrapper");
const cancelBtn = document.getElementById('cancelBtn');

const compResult = document.getElementById('comp_result');
const compressing = document.getElementById('compressing');

/* ON CLICK FILE BTN */
chooseFileBtn.addEventListener("click", function(){
  inputFileDefault.click();
});
/* ON CLICK FILE BTN */

/* VALUE FILE INPUT CHANGED */
inputFileDefault.addEventListener("change", function(){  
  const file = this.files[0];
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      imgBefore.src = result;
      imgWrapper.classList.add("active");
    }

    // show up img after on click the img before
    imgBefore.addEventListener('click', () => {
      imgAfter.src = imgBefore.src;
      imgWrapper.classList.add("active");
      
      compRateval();  // get comp rate value on click image before
      compResult.classList.add("active"); // show result component
      compressing.classList.add("off"); // off the loading animation
    });

    // delete image before, on click cancel btn
    cancelBtn.addEventListener('click', () => {
      imgBefore.src = "";
      imgWrapper.classList.remove("active");
    });
    reader.readAsDataURL(file);
  }
  if(inputFileDefault.value){
    fileText.innerHTML = inputFileDefault.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    
    // delete file path text 
    cancelBtn.addEventListener('click', () => {
      fileText.innerHTML = "No File Chosen";
      imgWrapper.classList.remove("active");
    });
  } else {
    // delete file path text 
    fileText.innerHTML = "No File Chosen";
  }
});
/* VALUE FILE INPUT CHANGED */

/* DOWNLOAD IMAGE AFTER */
imgAfter.addEventListener('click', () => {
  let imgPath = imgAfter.getAttribute("src");
  let fileName = getFileName(imgPath);

  if(imgPath != ""){
    saveAs(imgPath, fileName);
  }
});

function getFileName(str) {
  return str.substring(str.lastIndexOf("/") + 1);
}
/* DOWNLOAD IMAGE AFTER */

/* GET COMPRESS RATE VALUE */
function compRateval(){
  var compRateVal = document.getElementById("inputCompressRate").value;
  localStorage.setItem("compRateVal", compRateVal);
  document.getElementById("compRateResult").innerHTML=localStorage.getItem("compRateVal");
  return false
}
/* GET COMPRESS RATE VALUE */