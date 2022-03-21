class Cart {
	constructor(){
		let cart = localStorage.getItem("cartLine");
		if(cart == null) {
			this.cart = [];
		} else {
			this.cart = JSON.parse(cart);
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

	remove(product) {
		this.cart = this.cart.filter(p => p.id != product.id);
		this.save()
	}

	changeQuantity(product, quantity) {
		let foundProduct = this.cart.find(p => p.id == product.id);
		if (foundProduct != undefined) {
			foundProduct.quantity += quantity;
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
}

export { Cart };