# django-login-logout
In this project, we implement a simple user authentication system by using the Django ```auth``` module. This system can handle the below mentioned functionalities. 
1. New user registration
2. User login
3. Logout
4. Dynamic home page 
5. Change password for existing user
6. Recommend secure password to user while signing up
7. Dynamic profile page for each user - profile includes username, details, display picture and bio 
8. Edit/Update profile (display picture, bio) for logged-in user

For more details on this, you can check out our [blog post](https://helloml.org/implementing-a-user-registration-system-in-django-sign-up-login-and-logout/) on [hello ML](https://helloml.org). 

## Instructions to use
1. Clone the repo. 
```bash
git clone https://github.com/hellomlorg/django-login-logout.git
```
2. Create a virtual environment and activate it. Not required but highly recommended. 
```bash
python -m venv env
.\env\Scripts\activate
```
The above command is for Windows only. For Linux based operating systems, use the below mentioned command. 
```bash
python3 -m venv env
source env/bin/activate
```
3. Now, install the requirements. 
```bash
pip install -r requirements.txt
```
4. Now, migrate changes to the database and start the server. 
```
python manage.py migrate
python manage.py runserver
```
5. Head to [127.0.0.1:8000](http://127.0.0.1:8000/) and you should be able to see the development version of our app live. 

## Any Questions?
Feel free to raise an issue. We'll try to answer this as soon as we can. 

## Contributing Guidelines
If there is any valid contribution, please raise an issue and feel free to create a pull request. We will review it and merge it to the main branch. 

## Author
This README is contributed by [Vishnu S Reddy](https://helloml.org/author/vishnusreddy007/) and the code is contributed by [Dhruv Bothra](https://helloml.org/author/dhruvbothra/) and [Ajit Singh](https://helloml.org/author/ajit_iiitg/). 
 
