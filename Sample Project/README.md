# Sample App

Sample App loads data from [jsonplaceholder.com](http://jsonplaceholder.typicode.com/users) and shows a list of all users, including their name, username, email, and address. If you click on the name entry for a given user, you will navigate to a second page with detailed information on the user.  

I used Flask (for routing) and HTML/JQuery (for loading and displaying data). This was my first Flask project. I wasn't sure how to use a build tool to run/develop/deploy the application, but I'd love to learn.

To run the app on your local machine, type in the following in the terminal after unzipping the application:
* pip install -r requirements.txt
* export FLASK_APP=run.py