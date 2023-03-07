var menuItem = document.getElementsByClassName("menu-item") 

function redirectItem(itemId) {
    if (itemId === "dashboard") {
        window.location.href = 'http://127.0.0.1:5000/admin';
        
    } else if (itemId === "users") {
        //window.location.href = 'http://127.0.0.1:5000/users';

        function usersList() {
            fetch('/users_list', {
                method: 'POST',
                body: {}
            })
            .then(response => response.json())
            .then(data =>{

                if(data.success){
                    theData = JSON.stringify(data.userslist);
                    console.log(theData)
                    //window.location.href = 'http://127.0.0.1:5000/users';
                    fetch('/users', {
                        method: 'GET'
                    })

                }
                else{}
            })
            .catch(error => console.error(error));
        }

        usersList();

    } else {
      // handle unknown item ID
        console.log("Unknown menu item clicked");
    }
}
