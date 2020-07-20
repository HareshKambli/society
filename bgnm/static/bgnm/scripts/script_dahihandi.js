class Dahihandi2015{

	constructor(){this.slideIndex = 1;}


	year2015(){
		document.getElementById("2015").style.display="block";
		document.getElementById("2016").style.display="none";
		document.getElementById("2017").style.display="none";
	}

	openModal() {
	  document.getElementById("myModal2015").style.display = "block";
	}

	// Close the Modal
	closeModal() {
	  document.getElementById("myModal2015").style.display = "none";
	}


	plusSlides(n) {
	  this.showSlides(this.slideIndex += n);
	}

	currentSlide(n) {
	  this.showSlides(this.slideIndex = n);
	}

	showSlides(n) {
	  var i;
	  var slides = document.getElementsByClassName("mySlides2015");
	  this.slideIndex=n;
	  if (n > slides.length) {this.slideIndex = 1}
	  if (n < 1) {this.slideIndex = slides.length}
	  for (i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	  }
	  slides[this.slideIndex-1].style.display = "block";

	}
}

class Dahihandi2016{

	constructor(){this.slideIndex = 1;}

	year2016(){
		document.getElementById("2015").style.display="none";
		document.getElementById("2016").style.display="block";
		document.getElementById("2017").style.display="none";
	}

	openModal() {
	  document.getElementById("myModal2016").style.display = "block";
	}

	// Close the Modal
	closeModal() {
	  document.getElementById("myModal2016").style.display = "none";
	}



	plusSlides(n) {
	  this.showSlides(this.slideIndex += n);
	}

	currentSlide(n) {
	  this.showSlides(this.slideIndex = n);
	}

	showSlides(n) {
	  var i;
	  var slides = document.getElementsByClassName("mySlides2016");
	  this.slideIndex=n;
	  if (n > slides.length) {this.slideIndex = 1}
	  if (n < 1) {this.slideIndex = slides.length}
	  for (i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	  }
	  slides[this.slideIndex-1].style.display = "block";

	}
}

class Dahihandi2017{

	constructor(){this.slideIndex = 1;}

	year2017(){
		document.getElementById("2015").style.display="none";
		document.getElementById("2016").style.display="none";
		document.getElementById("2017").style.display="block";
	}

	openModal() {
	  document.getElementById("myModal2017").style.display = "block";
	}

	// Close the Modal
	closeModal() {
	  document.getElementById("myModal2017").style.display = "none";
	}



	plusSlides(n) {
	  this.showSlides(this.slideIndex += n);
	}

	currentSlide(n) {
	  this.showSlides(this.slideIndex = n);
	}

	showSlides(n) {
	  var i;
	  var slides = document.getElementsByClassName("mySlides2017");
	  this.slideIndex=n;
	  if (n > slides.length) {this.slideIndex = 1}
	  if (n < 1) {this.slideIndex = slides.length}
	  for (i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	  }
	  slides[this.slideIndex-1].style.display = "block";

	}
}

var dahihandi2015 = new Dahihandi2015();
var dahihandi2016 = new Dahihandi2016();
var dahihandi2017 = new Dahihandi2017();
