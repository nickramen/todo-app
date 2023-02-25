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

// Constant fields
const task_description = document.getElementById('task_description');
const day_id = document.getElementById('day_id');
const user_id = document.getElementById('user_id');
const alertDiv2 = document.getElementById('login-alert');

// Add new task with button
function addNewTask() {
    if(task_description.value == "" || user_id.value == ""){
        myAlertMessage('Task was not added. Do not leave empty fields.', 'error');
        setTimeout(function() {
            alertDiv2.style.display = 'none';
        }, 1000);
    }
    else if (day_id.value == "Select a day"){
        myAlertMessage('Task was not added. Select a day.', 'error');
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
                myAlertMessage('Task added successfully', 'success');
                window.location.href = 'http://127.0.0.1:5000/index';

            } else {
                const myModal = $('#addTaskModal');
                myModal.modal('hide');
                var inputs = document.querySelectorAll('#addTaskModal input');
                // Reset the value of each input field
                for (var i = 0; i < inputs.length; i++) {
                    inputs[i].value = '';
                }
                myAlertMessage('Task was not added', 'error');
                setTimeout(function() {
                    alertDiv2.style.display = 'none';
                }, 1000);
            }
        })
        .catch(error => console.error(error));
    }
}

// Change task status with checkbox
var inputs = document.querySelectorAll('.list-of-tasks');

// Attach a click event to each element
inputs.forEach(function(input) {
input.addEventListener('click', function() {
        var id = this.id;
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

// Delete task with button and modal
var inputs = document.querySelectorAll('.icon-delete');
inputs.forEach(function(input) {
input.addEventListener('click', function() {
        var id = this.id;
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
            myAlertMessage('Task deleted successfully', 'success');
            
            window.location.href = 'http://127.0.0.1:5000/index';

        } else {
            myAlertMessage('Task was not deleted', 'error');
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
        var originalText = this.innerText;
        this.contentEditable = true;
        this.classList.add('editing');
        this.focus();

        // Listen for the 'blur' event to save the changes
        this.addEventListener('blur', function() {
            var taskId = this.dataset.taskId;
            var newDescription = this.innerText;

            if (newDescription !== originalText) {
                updateTask(taskId, newDescription);
            }
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
            window.location.reload();
        }
    })
    .catch(error => console.error(error));
}