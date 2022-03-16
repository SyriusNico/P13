// const descriptions = document.querySelectorAll("#btn-describe");
const descriptions = document.querySelectorAll(".description");
let bgModal = document.querySelector('.bg-modal');
let image = document.querySelector(".modal-image");
let brand = document.querySelector(".modal-brand");
let name = document.querySelector(".modal-name");
let text = document.querySelector(".modal-description");
let price = document.querySelector(".modal-price");
let size = document.querySelector(".modal-size");
let close = document.querySelector(".close");



function getPreviousElement(element,selector) {
	var sibling = element.previousElementSibling;
	if (!selector) return sibling;
};

// Open a window when you click on the description button
function openModal() {
	descriptions.forEach((item) => {
		item.addEventListener('click', function() {
			event.preventDefault();
			bgModal.style.display = 'flex' ;
			let element = getPreviousElement(item);
			let formData = new FormData();
			formData.append('description', element.getAttribute("value"));
			fetch("/store/products/describe?description=" + element.value)
				.then(res => res.json())
				.then(data => {
					image.src = data[0].image;
					brand.innerHTML = data[0].brand;
					name.innerHTML = data[0].name;
					text.innerHTML = data[0].description;
					price.innerHTML = data[0].price;
					size.innerHTML = data[0].sizes;
				})
		}) 
	})
};


function closeModal() {
	close.addEventListener('click', function() {
		bgModal.style.display = 'None';
	})
};

openModal();
closeModal();