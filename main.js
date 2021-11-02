const inputFileDefault = document.getElementById('inputFileDefault');
const chooseFileBtn = document.getElementById('chooseFileBtn');
const fileText = document.getElementById('fileText');

const imgBefore = document.getElementById('imgBefore');
const imgAfter = document.getElementById('imgAfter');
const imgWrapper = document.querySelector(".imgWrapper");
const cancelBtn = document.getElementById('cancelBtn');

chooseFileBtn.addEventListener("click", function(){
  inputFileDefault.click();
});

inputFileDefault.addEventListener("change", function(){  
  const file = this.files[0];
  if(file){
    const reader = new FileReader();
    reader.onload = function(){
      const result = reader.result;
      imgBefore.src = result;
      imgWrapper.classList.add("active");
    }

    // show up img after by click the img before
    imgBefore.addEventListener('click', () => {
      imgAfter.src = imgBefore.src;
      imgWrapper.classList.add("active");
    });

    cancelBtn.addEventListener('click', () => {
      imgBefore.src = "";
      imgWrapper.classList.remove("active");
    });
    reader.readAsDataURL(file);
  }
  if(inputFileDefault.value){
    fileText.innerHTML = inputFileDefault.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    cancelBtn.addEventListener('click', () => {
      fileText.innerHTML = "No File Chosen";
      imgWrapper.classList.remove("active");
    });
  } else {
    fileText.innerHTML = "No File Chosen";
  }
});

