// Fetch secret keys from template
var stripe_public_key = document.getElementById('id_stripe_public_key').innerHTML.slice(1, -1);
var client_secret = document.getElementById('id_client_secret').innerHTML.slice(1, -1);

// Supply the key
var stripe = Stripe(stripe_public_key);

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
    base: {
        color: "#6c757d",
        fontFamily: '"Poppins", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create("card", {style: style});
card.mount("#card-element");

//Listen to change events on the card Element and display any errors
card.on('change', ({error}) => {
  let displayError = document.getElementById('card-errors');
  if (error) {
    displayError.textContent = error.message;
  } else {
    displayError.textContent = '';
  }
});