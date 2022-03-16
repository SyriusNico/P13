let sliderContent = document.getElementsByClassName('content');

let counter = 0;

let numberOfSlide = sliderContent.length;

function hideContent() {
	for(let i = 0; i < numberOfSlide ; i++) {
		sliderContent[i].classList.remove('active');
	}
};

setInterval(function () {
	counter++;
	if(counter >= numberOfSlide) {
		counter = 0;
	}
	hideContent();
	sliderContent[counter].classList.add('active');
}, 8000)

