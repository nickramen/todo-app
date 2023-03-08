$(document).ready(function() {
    
    fetch('/users_list')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#table-body');
        tableBody.innerHTML = '';
        data.forEach(user => {
            const statusBadge = user[3] == 1 ? '<span class="badge badge-success">Active</span>' : '<span class="badge badge-warning">Inactive</span>';
            var buttons = `<ion-icon name="create-sharp" class="icon" style="color:#17a2b8;"></ion-icon>
                            <ion-icon name="reader-sharp" class="icon" style="color:gray;"></ion-icon>
                            <ion-icon name="trash-sharp" class="icon" style="color:red;"><a>data-toggle="modal" data-target="#exampleModal</a></ion-icon>
            `
            const row = document.createElement('tr');
            row.innerHTML = `
            <td>${user[0]}</td>
            <td>${user[1]}</td>
            <td>${user[2]}</td>
            <td>${statusBadge}</td>
            <td>${buttons}</td>
            `;
            tableBody.appendChild(row);
        });
    })
    .catch(error => console.error(error));

});

const alertDiv2 = document.getElementById('login-alert');

// ALERTS
function myAlertMessage(message, type){
    const alertDiv2 = document.getElementById('login-alert');

    if(type == 'error'){
        alertDiv2.style.display = 'block';
        alertDiv2.innerText = '';
        alertDiv2.classList.remove('alert-success');
        alertDiv2.classList.add('alert-danger');
        alertDiv2.innerText = message;
    }
    else if(type == 'success'){
        alertDiv2.style.display = 'block';
        alertDiv2.innerText = '';
        alertDiv2.classList.remove('alert-danger');
        alertDiv2.classList.add('alert-success');
        alertDiv2.innerText = message;
        
    }

}

// SIGNUP 
const signup_username = document.getElementById('signup-username');
const signup_email = document.getElementById('signup-email');
const signup_password = document.getElementById('signup-password');
const signup_confirm_password = document.getElementById('signup-confirm-password');

function addUser() {

    if(signup_username.value == "" || signup_email.value == "" || signup_password.value == "" || signup_confirm_password.value ==""){
        myAlertMessage('User not added. One or more fields are empty.', 'error')
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 1000);
    }
    else if(signup_password.value == signup_confirm_password.value){

        const form = document.querySelector('form');
        const formData = new FormData(form);
        fetch('/add_user', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                myAlertMessage('User added successfully', 'success');
                window.location.href = 'http://127.0.0.1:5000/users';

            } else {
                const myModal = $('#addUserModal');
                myModal.modal('hide');
                var inputs = document.querySelectorAll('#addUserModal input');
                // Reset the value of each input field
                for (var i = 0; i < inputs.length; i++) {
                    inputs[i].value = '';
                }
                myAlertMessage('User was not added', 'error');
                setTimeout(function() {
                    alertDiv2.style.display = 'none';
                }, 1000);
            }
        })
        .catch(error => console.error(error));
    }
    else{
        myAlertMessage('User was not added. Passwords do not match.', 'error')
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 1000);
    }
}
