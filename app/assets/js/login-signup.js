//---------------------------
// Log In
//---------------------------
function loginButton() {
    const form = document.querySelector('form');
    const formData = new FormData(form);
    fetch('/submit_login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const alertDiv = document.getElementById('login-alert');
        if (data.success) {
            // Redirect to index page if login is successful
            alertDiv.style.display = 'block';
            alertDiv.classList.remove('alert-danger');
            alertDiv.classList.add('alert-success');
            alertDiv.innerText = 'Login successful. Redirecting to dashboard...';
            
            setTimeout(() => {
                window.location.href = 'http://127.0.0.1:5000/index';
            }, 2000);
        } else {
            // Display error message if login is unsuccessful
            alertDiv.classList.remove('alert-success');
            alertDiv.classList.add('alert-danger');
            alertDiv.innerText = 'Invalid username or password';
            setTimeout(function() {
                alertDiv.style.display = 'none';
            }, 2000);
        }
    })
    .catch(error => console.error(error));
}