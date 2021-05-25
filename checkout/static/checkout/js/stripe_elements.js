// Fetch secret keys from template
var stripePublicKey = document.getElementById('id_stripe_public_key').innerHTML.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').innerHTML.slice(1, -1);

// Supply the key
var stripe = Stripe(stripePublicKey);

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


//Submit payment to Stripe
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    card.update({'disabled': true})
    document.getElementById("submit-button").disabled = true;

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            let displayError = document.getElementById('card-errors');
            displayError.textContent = result.error.message;
            console.log(result.error.message);
            card.update({'disabled': false})
            document.getElementById("submit-button").disabled = false;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
                console.log(result.paymentIntent.status);
            }
        }
    });
});