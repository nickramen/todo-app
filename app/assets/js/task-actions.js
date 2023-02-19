//---------------------------
// Constant fields
//---------------------------
const task_description = document.getElementById('task_description');
const day_id = document.getElementById('day_id');
const alertDiv = document.getElementById('login-alert');
//---------------------------
// Add new task with button
//---------------------------
function addNewTask() {
    if(task_description.value == ""){
        // Display error message if fields are empty
        alertDiv.style.display = 'block';
        alertDiv.innerText = '';
        alertDiv.classList.remove('alert-success');
        alertDiv.classList.add('alert-danger');
        alertDiv.innerText = 'Task was not added. Do not leave empty fields.'+ day_id.value;
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 2000);
    }
    else if (day_id.value == "Select a day"){
        // Display error message if day is not selected
        alertDiv.style.display = 'block';
        alertDiv.innerText = '';
        alertDiv.classList.remove('alert-success');
        alertDiv.classList.add('alert-danger');
        alertDiv.innerText = 'Task was not added. Select a day.' + day_id.value;
        setTimeout(function() {
            alertDiv.style.display = 'none';
        }, 2000);
    }
    else{
        const form = document.querySelector('form');
        const formData = new FormData(form);
        fetch('/add_task', {
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
                alertDiv.innerText = 'Task added successfully';
                
                window.location.href = 'http://127.0.0.1:5000/index';

            } else {
                const myModal = $('#addTaskModal');
                myModal.modal('hide');
                var inputs = document.querySelectorAll('#addTaskModal input');
                // Reset the value of each input field
                for (var i = 0; i < inputs.length; i++) {
                    inputs[i].value = '';
                }
                // Display error message if login is unsuccessful
                alertDiv.style.display = 'block';
                alertDiv.innerText = '';
                alertDiv.classList.remove('alert-success');
                alertDiv.classList.add('alert-danger');
                alertDiv.innerText = 'Task was not added';
                setTimeout(function() {
                    alertDiv.style.display = 'none';
                }, 2000);
            }
        })
        .catch(error => console.error(error));
    }
}

//---------------------------
// Change task status with checkbox
//---------------------------
// Get all elements with class "list-of-tasks"
var inputs = document.querySelectorAll('.list-of-tasks');
// Attach a click event to each element
inputs.forEach(function(input) {
input.addEventListener('click', function() {
        // Get the id of the clicked input
        var id = this.id;
        // Call a function and pass the id as an argument
        taskStatus(id);
    });
});
function taskStatus(id) {
    fetch('/task_status', {
        method: 'POST',
        body: id
    })
    .then(response => response.text())
    .catch(error => console.error(error));
    window.location.reload('http://127.0.0.1:5000/index');
}

//---------------------------
// Delete task with button and modal
//---------------------------
// Get all elements with class "icon-delete"
var inputs = document.querySelectorAll('.icon-delete');
// Attach a click event to each element
inputs.forEach(function(input) {
input.addEventListener('click', function() {
        // Get the id of the clicked input
        var id = this.id;
        // Set the delete button from the modal
        var deleteButton = document.querySelector('#task-delete-button');
        deleteButton.setAttribute('task-id', id);
    });
});

function taskDelete() {
    var id = document.getElementById("task-delete-button").getAttribute("task-id");  
    console.log(id)
    fetch('/delete_task', {
        method: 'POST',
        body: id
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect to index page if login is successful
            alertDiv.style.display = 'block';
            alertDiv.innerText = '';
            alertDiv.classList.remove('alert-danger');
            alertDiv.classList.add('alert-success');
            alertDiv.innerText = 'Task deleted successfully';
            
            window.location.href = 'http://127.0.0.1:5000/index';

        } else {

            // Display error message if login is unsuccessful
            alertDiv.style.display = 'block';
            alertDiv.innerText = '';
            alertDiv.classList.remove('alert-success');
            alertDiv.classList.add('alert-danger');
            alertDiv.innerText = 'Task was not deleted';
            setTimeout(function() {
                alertDiv.style.display = 'none';
            }, 2000);
        }
    })
    .catch(error => console.error(error));
}

