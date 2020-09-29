// Stripe setup 
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
      iconColor: '#c4f0ff',
      color: 'rgb(60, 63, 54)',
      fontWeight: 500,
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      ':-webkit-autofill': {
        color: '#fce883',
      },
      '::placeholder': {
        color: 'rgb(60, 63, 54)',
      },
    },
    invalid: {
      iconColor: '#FFC7EE',
      color: '#FFC7EE',
    },
};

var card = elements.create('card', {style: style});
card.mount('#card-element');
