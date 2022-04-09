import { Cart } from "./cart.js"

let cart = new Cart()

let cartCount = document.getElementById('cart-count')
let cartCountResp = document.getElementById('cart-count-resp')

cartCount.innerHTML = "Panier (" + cart.getNumberProduct() + ")"
cartCountResp.innerHTML = "Panier (" + cart.getNumberProduct() + ")"