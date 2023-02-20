# weekly to-do list by nickramen
weekly to-do list is an app that helps you organize the things you have to do during your week. It has an intuitive interface that makes it easy for you to get started.

## Main features:
- Tasks management: You can create tasks for a certain day of the week and assign it a catergory. You can also delete tasks you will no longer be doing. Finally, you can check the tasks that you have already done.
- Dashboards: Get reports in form of graphs of your overall activity.

## Includes:
- User dashboard
- Admin dashboard

## Other:
- Field validations
- Session validations


The app is still in construction, so there are more features I will be adding.

## "I downloaded your repo and want to try the app!"

This is a flask app built using Python and JS mainly. As for the database, I am using sqlite so far.

### Follow the steps down below:

- First we need to activate the virtual environment. For that, we are going to look for the following folder in our terminal and paste the activation command:

  - Folder: /db
  - Command: .\env\Scripts\activate

- Then we need to create the database. There might be already a database created but I would recommend you to create it again using the script so you can have better visualizations:

- Delete the existing database found in the folder /db/src/database
- Go back to /db/src and using the terminal you have previously activated run the script 'initial_data.py' with this command: python initial_data.py. (You need to have Python installed in you computer previously) 
- Finally, to run the app go to this folder: /app and run the script 'app.py' with this command: python app,py

### User credentials

Now that you have launched the app it will load in your localhost. Visit: http://127.0.0.1:5000/login and the login page will show up. Use the following credentials for you to start testing the appp, or create your own user account in the signup form.

#### Administrator
- username: admin
- password: admin1234

#### Users
- username: nickramen
- password: nickramen

- username: nicole
- username nicole

Use the two users above since they have data assigned to them in the initial data.


### Questions of Feedback?

Feel free to contact me if you have any questions or any feedback after testing the app.



Thank you so much for reading and coming to my profile!!!