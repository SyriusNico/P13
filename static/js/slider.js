// let sliderContent = document.getElementsByClassName('content');
// let counter = 0;
// let numberOfSlide = sliderContent.length;



// function hideContent() {
// 	for(let i = 0; i < numberOfSlide ; i++) {
// 		sliderContent[i].classList.remove('active');
// 	}
// };

// setInterval(function () {
// 	counter++;
// 	if(counter >= numberOfSlide) {
// 		counter = 0;
// 	}
// 	hideContent();
// 	sliderContent[counter].classList.add('active');
// }, 4000)


const track = document.querySelector('.carousel-track');
const slides = Array.from(track.children);
const slideWidth = slides[0].getBoundingClientRect().width;


// arrange the slides next to one another
const setSlidePosition = (slide, index) => {
	slide.style.left = slideWidth * index + 'px';
};
slides.forEach((setSlidePosition));