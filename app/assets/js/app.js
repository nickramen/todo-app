// Get the login and signup cards
const loginCard = document.getElementById('login-card');
const signupCard = document.getElementById('signup-card');

// Get the login and signup selectors
const loginSelector = document.getElementById('login-selector');
const signupSelector = document.getElementById('signup-selector');

// Get the login and signup titles
const loginHeader = document.getElementById('login-card-header');
const signupHeader = document.getElementById('signup-card-header');

// Default style values
signupCard.style.display = 'none';
signupSelector.style.backgroundColor = "gray";
signupHeader.style.display = 'none';

loginSelector.addEventListener("click", function() {
    loginCard.style.display = "block";
    signupCard.style.display = "none";
    loginHeader.style.display = 'block';
    signupHeader.style.display = 'none';
    loginSelector.style.backgroundColor = "#343a40";
    signupSelector.style.backgroundColor = "gray";
});

// Add click event listener to the signup selector
signupSelector.addEventListener('click', function() {
    loginCard.style.display = 'none';
    signupCard.style.display = 'block';
    loginHeader.style.display = 'none';
    signupHeader.style.display = 'block';
    loginSelector.style.backgroundColor = '';
    loginSelector.style.color = 'white';
    loginSelector.style.backgroundColor = "gray";
    signupSelector.style.backgroundColor = '#343a40';
    signupSelector.style.color = 'white';
});
