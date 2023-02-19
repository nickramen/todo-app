//---------------------------
// Constant fields
//---------------------------
const login_username = document.getElementById('login-username');
const login_password = document.getElementById('login-password');

const signup_username = document.getElementById('signup-username');
const signup_email = document.getElementById('signup-email');
const signup_password = document.getElementById('signup-password');
const signup_confirm_password = document.getElementById('signup-confirm-password');

const alertDiv = document.getElementById('login-alert');

//---------------------------
// Log In
//---------------------------
function loginButton() {

    //Check no fields are empty
    if(login_username.value == "" || login_password.value == ""){
        // Display error message if fields are empty
        alertDiv.style.display = 'block';
        alertDiv.innerText = '';
        alertDiv.classList.remove('alert-success');
        alertDiv.classList.add('alert-danger');
        alertDiv.innerText = 'Login failed. One or more fields are empty.';
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 2000);
    }
    else{
        const form = document.querySelector('form');
        const formData = new FormData(form);
        fetch('/submit_login', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect to index page if login is successful
                alertDiv.style.display = 'block';
                alertDiv.innerText = '';
                alertDiv.classList.remove('alert-danger');
                alertDiv.classList.add('alert-success');
                alertDiv.innerText = 'Login successful. Redirecting to dashboard';
                
                setTimeout(() => {
                    window.location.href = 'http://127.0.0.1:5000/index';
                }, 2000);
            } else {
                // Display error message if login is unsuccessful
                alertDiv.style.display = 'block';
                alertDiv.innerText = '';
                alertDiv.classList.remove('alert-success');
                alertDiv.classList.add('alert-danger');
                alertDiv.innerText = 'Login failed. Invalid username or password.';
                setTimeout(function() {
                    alertDiv.style.display = 'none';
                }, 2000);
            }
        })
        .catch(error => console.error(error));
    }
}


//---------------------------
// Sign Up
//---------------------------
function signupButton() {

    if(signup_username.value == "" || signup_email.value == "" || signup_password.value == "" || signup_confirm_password.value ==""){
        // Display error message if fields are empty
        alertDiv.style.display = 'block';
        alertDiv.innerText = '';
        alertDiv.classList.remove('alert-success');
        alertDiv.classList.add('alert-danger');
        alertDiv.innerText = 'Signup failed. One or more fields are empty.';
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 2000);
    }
    else if(signup_password.value == signup_confirm_password.value){ //check if both passwords are the same

        const form = document.querySelector('form');
        const formData = new FormData(form);
        fetch('/submit_signup', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect to index page if login is successful
                alertDiv.style.display = 'block';
                alertDiv.innerText = '';
                alertDiv.classList.remove('alert-danger');
                alertDiv.classList.add('alert-success');
                alertDiv.innerText = 'Signup successful. Now please log in.';
                setTimeout(function() {
                    alertDiv.style.display = 'none';
                }, 2000);

                const loginCard = document.getElementById('login-card');
                const signupCard = document.getElementById('signup-card');

                loginCard.style.display = "block";
                signupCard.style.display = "none";

            } else {
                // Display error message if login is unsuccessful
                alertDiv.style.display = 'block';
                alertDiv.innerText = '';
                alertDiv.classList.remove('alert-success');
                alertDiv.classList.add('alert-danger');
                alertDiv.innerText = 'Signup failed.';
                setTimeout(function() {
                    alertDiv.style.display = 'none';
                }, 2000);
            }
        })
        .catch(error => console.error(error));
    }
    else{
        // Display error message if fields are empty
        alertDiv.style.display = 'block';
        alertDiv.innerText = '';
        alertDiv.classList.remove('alert-success');
        alertDiv.classList.add('alert-danger');
        alertDiv.innerText = 'Signup failed. Passwords do not match.';
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 2000);
    }
}