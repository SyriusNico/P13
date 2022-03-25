import { Cart } from "./cart.js"

let cart = new Cart()
let cartItems = document.querySelector(".cart-items")
let totalPrice = document.querySelector(".cart-total-price")
let total = document.querySelector(".cart-total")
let order = document.querySelector(".cart-order")
let user = document.querySelector(".user")

console.log(cart.cart)
totalPrice.innerHTML = cart.getTotalPrice()

if (cart.cart != []) {
	for(let element of cart.cart) {
		if (element.user == user.value) {
			let cartRow = document.createElement('div')
			let hr = document.createElement('hr')
			cartRow.classList.add('cart-row')
			let cartRowContents = `
				<div class="cart-item cart-column">
					<img class="cart-item-image" src="${element.image}">
					<span class="cart-item-name">${element.name}</span>
				</div>
				<span class="cart-price cart-column" style="margin-left: 50px">${element.price} €</span>
				<div class="cart-quantity cart-column">
					<input class="cart-quantity-input" type="number" min="0" value="${element.quantity}">
					<button class="btn btn-danger" type="button" value="${element.id}">Supprimer</button>
				</div>`
			cartRow.innerHTML = cartRowContents
			cartItems.appendChild(cartRow)
			cartItems.appendChild(hr)
		}
	}
} else {
	let cartRow = document.createElement('div')
	cartRow.classList.add('cart-row')
	let cartRowContents = `Votre panier est vide.`
	let cartOder = document.querySelector('cart-order')
	cartOder.remove()
	cartRow.innerHTML = cartRowContents
	cartItems.appendChild(cartRow)
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