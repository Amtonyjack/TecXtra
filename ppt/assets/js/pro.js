function move() 
{
  var elem = document.getElementById("mybar");   
  var width = 1;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
    }
  }
}

function move1() {
  var elem = document.getElementById("mybar1");   
  var width = 1;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
    }
  }
}
function move2(){
  var elem = document.getElementById("mybar2");   
  var width = 1;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
    }
  }
}

function l1()
	{
		var aa=parseInt(document.getElementById('a1').value);
		var ab=parseInt(document.getElementById('a2').value);
		var ac=parseInt(document.getElementById('a3').value);
		var ad=parseInt(document.getElementById('a4').value);
		var q=aa+ab+ac+ad;
		document.getElementById('a5').value= q;
	}



