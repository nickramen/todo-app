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
                            <ion-icon name="trash-sharp" class="icon" style="color:red;"></ion-icon>
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


    // $.ajax({
    //     url: '/users_list',
    //     type: 'GET',
    //     dataType: 'json',
    //     success: function(data) {
    //         var tableBody = $('#table-body');
    //         tableBody.empty();
    //         $.each(data, function(index, row) {
    //             var tr = $('<tr>');
    //             $.each(row, function(key, value) {
    //                 var td = $('<td>').text(value);
    //                 tr.append(td);
    //             });
    //             tableBody.append(tr);
    //         });
    //     },
    //     error: function(jqXHR, textStatus, errorThrown) {
    //         console.log(textStatus, errorThrown);
    //     }
    // });
});