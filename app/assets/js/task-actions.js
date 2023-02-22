//---------------------------
// Constant fields
//---------------------------
const task_description = document.getElementById('task_description');
const day_id = document.getElementById('day_id');
const user_id = document.getElementById('user_id');
const alertDiv2 = document.getElementById('login-alert');
//---------------------------
// Add new task with button
//---------------------------
function addNewTask() {
    if(task_description.value == "" || user_id.value == ""){
        // Display error message if fields are empty
        alertDiv2.style.display = 'block';
        alertDiv2.innerText = '';
        alertDiv2.classList.remove('alert-success');
        alertDiv2.classList.add('alert-danger');
        alertDiv2.innerText = 'Task was not added. Do not leave empty fields.'+ day_id.value;
        setTimeout(function() {
            alertDiv2.style.display = 'none';
        }, 1000);
    }
    else if (day_id.value == "Select a day"){
        // Display error message if day is not selected
        alertDiv2.style.display = 'block';
        alertDiv2.innerText = '';
        alertDiv2.classList.remove('alert-success');
        alertDiv2.classList.add('alert-danger');
        alertDiv2.innerText = 'Task was not added. Select a day.' + day_id.value;
        setTimeout(function() {
            alertDiv2.style.display = 'none';
        }, 1000);
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
                alertDiv2.style.display = 'block';
                alertDiv2.innerText = '';
                alertDiv2.classList.remove('alert-danger');
                alertDiv2.classList.add('alert-success');
                alertDiv2.innerText = 'Task added successfully';
                
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
                alertDiv2.style.display = 'block';
                alertDiv2.innerText = '';
                alertDiv2.classList.remove('alert-success');
                alertDiv2.classList.add('alert-danger');
                alertDiv2.innerText = 'Task was not added';
                setTimeout(function() {
                    alertDiv2.style.display = 'none';
                }, 1000);
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

        // Call the taskStatus function with the id
        taskStatus(id);
    });
});
function taskStatus(id) {
    fetch('/task_status', {
        method: 'POST',
        body: id
    })
    .then(response => response.json())
    .then(data =>{

        if(data.success){
            window.location.reload('http://127.0.0.1:5000/index');
        }
        else{}
    })
    .catch(error => console.error(error));
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
            alertDiv2.style.display = 'block';
            alertDiv2.innerText = '';
            alertDiv2.classList.remove('alert-danger');
            alertDiv2.classList.add('alert-success');
            alertDiv2.innerText = 'Task deleted successfully';
            
            window.location.href = 'http://127.0.0.1:5000/index';

        } else {

            // Display error message if login is unsuccessful
            alertDiv2.style.display = 'block';
            alertDiv2.innerText = '';
            alertDiv2.classList.remove('alert-success');
            alertDiv2.classList.add('alert-danger');
            alertDiv2.innerText = 'Task was not deleted';
            setTimeout(function() {
                alertDiv2.style.display = 'none';
            }, 1000);
        }
    })
    .catch(error => console.error(error));
}

//EDIT THE TASK DESCRIPTION
document.querySelectorAll('.task-item').forEach(function(label) {
    label.addEventListener('click', function(event) {
        // Save a reference to the original label text
        var originalText = this.innerText;

        // Set the label to be editable
        this.contentEditable = true;
        this.classList.add('editing');

        // Focus on the label so the user can start typing right away
        this.focus();

        // Listen for the 'blur' event to save the changes
        this.addEventListener('blur', function() {
            // Get the new task description
            var taskId = this.dataset.taskId;
            var newDescription = this.innerText;

            // Only update the task if the description has changed
            if (newDescription !== originalText) {
                // Call a function to update the task in the database
                updateTask(taskId, newDescription);
            }

            // Set the label back to non-editable mode
            this.contentEditable = false;
            this.classList.remove('editing');
        });
    });
});


function updateTask(taskId, newDescription) {
    fetch('/update_task', {
        method: 'POST',
        body: JSON.stringify({taskId: taskId, newDescription: newDescription})

    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Reload the page
            //window.location.reload();
        }
    })
    .catch(error => console.error(error));
}
