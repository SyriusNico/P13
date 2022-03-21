import { Cart } from "./cart.js"

let cart = new Cart()
let cartItems = document.querySelector(".cart-items")


for(let element of cart.cart) {
	let cartRow = document.createElement('div')
	cartRow.classList.add('cart-row')
	let cartRowContents = `
		<div class="cart-item cart-column">
			<img class="cart-item-image" src="${element.image}">
			<span class="cart-item-name">${element.name}</span>
		</div>
		<span class="cart-price cart-column" style="margin-left: 50px">${element.price}</span>
		<div class="cart-quantity cart-column">
			<input class="cart-quantity-input" type="number" value="1">
			<button class="btn btn-danger" type="button">Supprimer</button>
		</div>`
	cartRow.innerHTML = cartRowContents
	console.log(cart.getTotalPrice())
	cartItems.appendChild(cartRow)	
}

let totalPrice = document.querySelector(".cart-total-price")
totalPrice.innerHTML = cart.getTotalPrice()