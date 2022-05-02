const stripe = Stripe('pk_test_51KhgjvBjHQ5DRC9EELeowiZIqc2AnGDR94FgSsxk9u2XUkznvzSXTheQ0z9MYkCVrhF1Vxto79uMTOO53uJC9har00kyHNa1xx');
const elem = document.getElementById('submit');


const options = {clientSecret: elem.getAttribute('data-secret')};
const elements = stripe.elements(options);

const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: 'http://markedet.herokuapp.com/payment/success/',
    },
  });

  if (error) {
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {
  	
  }
});