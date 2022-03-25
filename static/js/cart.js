class Cart {
	constructor(){
		this.cart = localStorage.getItem("cartLine");
		if(this.cart == null) {
			this.cart = [];
		} else {
			this.cart = JSON.parse(this.cart);
		}
	}

	save() {
		localStorage.setItem("cartLine", JSON.stringify(this.cart));
	}

	add(product) { 
		let foundProduct = this.cart.find(p => p.id == product.id);
		if (foundProduct != undefined) {
			foundProduct.quantity++;
		} else {
			product.quantity = 1;
			this.cart.push(product);
		}
		this.save();
	}

	remove(id) {
		this.cart = this.cart.filter(p => p.id != id);
		this.save()
	}

	changeQuantity(id, quantity) {
		let foundProduct = this.cart.find(p => p.id == id);
		if (foundProduct != undefined) {
			foundProduct.quantity = quantity;
			if (foundProduct.quantity <= 0) {
				this.remove(foundProduct);
			} else {
				this.save();
			}
		}
	}

	getNumberProduct() {
		let number = 0;
		for (let product of this.cart) {
			number += product.quantity;
		}
		return number;
	}

	getTotalPrice() {
		let total = 0;
		for (let product of this.cart) {
			total += product.quantity * parseInt(product.price);
		}
		return total + " €";
	}

	// getTotalPrice(user) {
	// 	let total = 0;
	// 	for (let product of this.cart) {
	// 		if (product.user == user) {
	// 			total += product.quantity * parseFloat(product.price);
	// 		} else {
	// 			total = 0
	// 		}
	// 	}
	// 	return total + " €";
	// }
}

export { Cart };