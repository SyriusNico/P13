import { Cart } from "./cart.js"

let cart = new Cart()

let cartCount = document.getElementById('cart-count')

cartCount.innerHTML = "(" + cart.getNumberProduct() + ")"