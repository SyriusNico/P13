const stripe = Stripe('pk_test_51KhgjvBjHQ5DRC9EELeowiZIqc2AnGDR94FgSsxk9u2XUkznvzSXTheQ0z9MYkCVrhF1Vxto79uMTOO53uJC9har00kyHNa1xx');

let element = document.getElementById('submit')
let paymentForm = document.getElementById('payment-form')
let elements = stripe.elements()


let style = {
	base: {
	  color: "#000",
	  lineHeight: '2.4',
	  fontSize: '18px'
	}
};

let cardElement = elements.create('card',{style:style})
cardElement.mount('#card-element')

cardElement.on('change', function(event) {
	let displayError = document.getElementById('card-errors')
	if (event.error) {
	  displayError.textContent = event.error.message;
	  $('#card-errors').addClass('alert alert-info');
	} else {
	  displayError.textContent = '';
	  $('#card-errors').removeClass('alert alert-info');
	}
});

paymentForm.addEventListener('submit', function() {
	let fname = document.getElementById("fname").value
	let email = document.getElementById("email").vallue
	let adr = document.getElementById("adr").value
	let zip = document.getElementById("zip").value
	let city = document.getElementById("city").value
	let country = document.getElementById("state").value
	
	let response = fetch('/payment/checkout').then(function(response) {
		return response.json();
	}).then(function(responseJson) {
		let clientSecret = responseJson.client_secret;
		stripe.confirmCardPayment(clientSecret, {
			payment_method: {
				card: cardElement,
				billing_details: {
					"address": {
					  "city": city,
					  "line1": adr,
					  "postal_code": zip,
					  "country": country
					},
					"email": email,
					"name": fname
				  },
				},
			},)
		.then(function(result) {
			if (result.error) {
				console.log('ça marche pas')
			} else {
				if (result.paymentIntent.status === 'succeeded') {
					window.localStorage.clear()
					window.location.replace("http://127.0.0.1:8000/store/categories/")
				}
			}
		})
	})
})