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
const compRateFinal = document.getElementById('compRateResult');

let imgBeforeName = "";

/* ON CLICK FILE BTN */
chooseFileBtn.addEventListener("click", function(){
  inputFileDefault.click();
});
/* ON CLICK FILE BTN */

/* VALUE FILE INPUT CHANGED */
inputFileDefault.addEventListener("change", function(){  
  const file = this.files[0];
  imgBeforeName = file.name;
  
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      imgBefore.src = result;
      imgWrapper.classList.add("active");
    }

    // show up img after on click the img before
    imgBefore.addEventListener('click', async () => {
      compResult.classList.remove("active");
      imgWrapper.classList.add("active");
      compressing.classList.add("active");

      // Send Image
      const inputCompressRate = document.getElementById("inputCompressRate").value;
      let formData = new FormData();
      formData.append("file", this.files[0]);
      formData.append("rate", inputCompressRate)
      let response = await fetch('http://127.0.0.1:8000/files/', {
        method: 'POST',
        mode: 'same-origin',
        body: formData
      })
      response = await response.json()

      timeCompressFinal.innerHTML = response.time.toFixed(2);
      compRateFinal.innerHTML = response.rate.toFixed(2);

      // Receive image
      response = await fetch("http://127.0.0.1:8000/files/"+response.fileId+"/"+response.fileExt, {
        method: "GET",
        mode: "same-origin",
      });
      response = await response.blob();
      imgAfter.src = URL.createObjectURL(response)
      
      compResult.classList.add("active"); // show result component
      compressing.classList.remove("active"); // remove the loading animation
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
  let fileName = imgBeforeName;

  if(imgPath != ""){
    saveAs(imgPath, fileName);
  }
});

function getFileName(str) {
  return str.substring(str.lastIndexOf("/") + 1);
}
/* DOWNLOAD IMAGE AFTER */