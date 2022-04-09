// let sliderContent = document.getElementsByClassName('content');
let counter = 0;
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
console.log(slideWidth);


// arrange the slides next to one another
const setSlidePosition = (slide, index) => {
	slide.style.left = slideWidth * index + 'px';
};
slides.forEach((setSlidePosition));

// set up slide loop
setInterval(slideLoop,4000);

function slideLoop() {
	const currentSlide = track.querySelector('.active');
	if (currentSlide.nextElementSibling) {
		const nextSlide = currentSlide.nextElementSibling;
		// move
		const amountToMove = nextSlide.style.left;
		track.style.transform = 'translateX(-' + amountToMove + ')';
		currentSlide.classList.remove('active');
		nextSlide.classList.add('active');
	} else {
		track.style.transform = 'translateX(' + 0 + ')';
		currentSlide.classList.remove('active');
		track.querySelectorAll('.carousel-slide')[0].classList.add('active');
	}
}

