
//---------------------------
// Add new task with button
//---------------------------
function addNewTask() {
    const form = document.querySelector('form');
    const formData = new FormData(form);
    fetch('/add_task', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .catch(error => console.error(error));
    //$('#exampleModal').modal('hide');
    // Get all the input fields in the modal
    var inputs = document.querySelectorAll('#addTaskModal input');
    // Reset the value of each input field
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].value = '';
    }
    window.location.reload('http://127.0.0.1:5000/index');
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
    .then(response => response.text())
    .catch(error => console.error(error));
    window.location.reload('http://127.0.0.1:5000/index');
}

