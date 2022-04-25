import { Cart } from "./cart.js"

let cart = new Cart()

let cartCount = document.getElementById('cart-count')
let cartCountResp = document.getElementById('cart-count-resp')
let numberProduct = document.getElementById('number-product')
let numberProductResponsive = document.getElementById('number-product-resp')

cartCount.value = "Panier (" + cart.getNumberProduct() + ")"
cartCountResp.value = "Panier (" + cart.getNumberProduct() + ")"
numberProduct.value = cart.getNumberProduct()
numberProductResponsive.value = cart.getNumberProduct()