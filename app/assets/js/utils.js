// ALERTS
export function myAlertMessage(message, type){
    const alertDiv2 = document.getElementById('login-alert');

    if(type == 'error'){
        alertDiv2.style.display = 'block';
        alertDiv2.innerText = '';
        alertDiv2.classList.remove('alert-success');
        alertDiv2.classList.add('alert-danger');
        alertDiv2.innerText = message;
    }

}