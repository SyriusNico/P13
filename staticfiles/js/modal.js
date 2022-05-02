import { Cart } from "./cart.js"

const descriptions = document.querySelectorAll(".description");
let bgModal = document.querySelector('.bg-modal');
let image = document.querySelector(".modal-image");
let brand = document.querySelector(".modal-brand");
let name = document.querySelector(".modal-name");
let text = document.querySelector(".modal-description");
let price = document.querySelector(".modal-price");
let size = document.querySelector(".modal-size");
let close = document.querySelector(".close");
let body = document.body;
let category = document.querySelector(".title-collection").childNodes;
category = category[1].innerHTML
let cart = new Cart()

function getPreviousElement(element,selector) {
	let sibling = element.previousElementSibling;
	if (!selector) return sibling;
};

function addOptions(listOfOptions) {
	for(let i = 0; i<listOfOptions.length; i++) {
		let opt = document.createElement("option");
		opt.value = opt.text = listOfOptions[i];
		size.appendChild(opt); 
	}
}

function getSize() {
	let sizeOptions = document.querySelector("#size").childNodes;
	for(let sizeOption of sizeOptions) {
		sizeOption.addEventListener('click', function() {
			console.log(sizeOption.value)
			return sizeOption.value
		})
	}
}

// Open a window when you click on the description button
function openModal() {
	descriptions.forEach((item) => {
		item.addEventListener('click', function(event) {
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
					let productId = data[0].id;
					let user = document.querySelector('.user');
					user = parseInt(user.value)
					let oneSize = getSize();
					addOptions(data[0].sizes);
					addToCard(
						productId, name.innerHTML, 
						data[0].price, image.src, 
						oneSize, user, category
					);
				})
		}) 
	})
};

function addToCard(id, name, price, image, size, user, category) {
	let addToCartButton = document.querySelector(".add-to-cart")
	addToCartButton.addEventListener("click", function() {
		location.href = location.origin + "/store/products/?category=" + category
		cart.add({
			"id":id,"name":name, 
			"price":price, "image":image, 
			"size":size, "user":user
		})
	})
}

function closeModal() {
	if (bgModal.style.display != 'None') {
		close.addEventListener('click', function() {
			bgModal.style.display = 'None';
			body.style.overflow = 'auto';
		})
	}
};



openModal();
closeModal();