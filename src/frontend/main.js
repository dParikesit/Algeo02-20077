const inputFileDefault = document.getElementById('inputFileDefault');
const chooseFileBtn = document.getElementById('chooseFileBtn');
const fileText = document.getElementById('fileText');

const imgBefore = document.getElementById('imgBefore');
const imgAfter = document.getElementById('imgAfter');
const imgWrapper = document.querySelector(".imgWrapper");
const cancelBtn = document.getElementById('cancelBtn');

const compResult = document.getElementById('comp_result');
const compressing = document.getElementById('compressing');
const timeCompressFinal = document.getElementById('timeCompress');

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
    imgBefore.addEventListener('click', async () => {
      imgWrapper.classList.add("active");

      // Send Image
      let formData = new FormData();
      console.log(inputFileDefault)
      formData.append("file", this.files[0]);
      formData.append("rate", 80)
      let response = await fetch('http://127.0.0.1:8000/files/', {
        method: 'POST',
        mode: 'same-origin',
        body: formData
      })
      response = await response.json()
      // SET DISINI TIME NYA, dari variabel response.time
      let compressTime = 0;
      let timeInterval;
      timeInterval = setInterval(function() {
        compressTime += 0.1;
      }, 100);
      // Receive image
      response = await fetch("http://127.0.0.1:8000/files/"+response.fileId+"/"+response.fileExt, {
        method: "GET",
        mode: "same-origin",
      });
      response = await response.blob();
      imgAfter.src = URL.createObjectURL(response)

      clearInterval(timeInterval);
      timeCompressFinal.innerHTML = compressTime;

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