import { Cart } from "./cart.js"

let cart = new Cart()
let cartItems = document.querySelector(".cart-items")
let totalPrice = document.querySelector(".cart-total-price")
let total = document.querySelector(".cart-total")
let order = document.querySelector(".cart-order")
let user = document.querySelector(".user")

totalPrice.innerHTML = cart.getTotalPrice()


for(let element of cart.cart) {
	let cartRow = document.createElement('div')
	let hr = document.createElement('hr')
	cartRow.classList.add('cart-row')
	let cartRowContents = `
		<input type="hidden" name="product-id" value="${element.id}">
		<div class="cart-item cart-column">
			<img class="cart-item-image" src="${element.image}">
			<span class="cart-item-name">${element.name}</span>
		</div>
		<span class="cart-price cart-column" style="margin-left: 50px">${element.price} €</span>
		<div class="cart-quantity cart-column">
			<input class="cart-quantity-input" name="quantity" type="number" min="0" value="${element.quantity}">
			<button class="btn btn-danger" type="button" value="${element.id}">Supprimer</button>
		</div>`
	cartRow.innerHTML = cartRowContents
	cartItems.appendChild(cartRow)
	cartItems.appendChild(hr)
}


let deleteBtn = document.querySelectorAll(".btn-danger")
function deleteCartLine() {
	deleteBtn.forEach((item) => {
		item.addEventListener('click', function() {
			cart.remove(item.value)
			item.parentNode.parentNode.remove()
			totalPrice.innerHTML = cart.getTotalPrice()
		})
	})
}

function changeQuantity() {
	let quantities = document.querySelectorAll(".cart-quantity-input")
	quantities.forEach((item) => {
		item.addEventListener('change', function() {
			let product = item.nextSibling.nextSibling.value
			cart.changeQuantity(product, item.value)
			totalPrice.innerHTML = cart.getTotalPrice()
		})
	})
}

deleteCartLine();
changeQuantity();