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
let productId = document.querySelector(".product-id");
let body = document.body;

function getPreviousElement(element,selector) {
	var sibling = element.previousElementSibling;
	if (!selector) return sibling;
};

function addOptions(listOfOptions) {
	for(let i = 0; i<listOfOptions.length; i++) {
		console.log(listOfOptions[i]);
		opt = document.createElement("option");
		opt.value = opt.text = listOfOptions[i],
		size.appendChild(opt); 
	}
}

// Open a window when you click on the description button
function openModal() {
	descriptions.forEach((item) => {
		item.addEventListener('click', function() {
			event.preventDefault();
			bgModal.style.display = 'flex' ;
			body.style.overflow = 'hidden';
			let element = getPreviousElement(item);
			fetch("/store/products/describe?description=" + element.value)
				.then(res => res.json())
				.then(data => {
					image.alt = data[0].name;
					image.src = data[0].image;
					brand.innerHTML = data[0].brand;
					name.innerHTML = data[0].name;
					text.innerHTML = data[0].description;
					price.innerHTML = data[0].price;
					productId.value = data[0].id;
					addOptions(data[0].sizes);
				})
		}) 
	})
};

function closeModal() {
	close.addEventListener('click', function() {
		bgModal.style.display = 'None';
		body.style.overflow = 'auto';
	})
};

openModal();
closeModal();
