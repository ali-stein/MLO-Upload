# My Learning Organizer -- MLO

## Installation
1. Create a virtual environment--Type py -m venv env\mylearning
2. Type .\env\mylearning\Scripts\activate to enter the virtual environment
3. Add the modules into the virtual environment based off the requirements.txt file
    Make sure that you're in the mylearning directory that has the manage.py file.
    Type--pip install -r requirements.txt--This will install all of the required modules for the project.
4. Add the Subjects fixtures to the project 
    Type django-admin loaddata subjects.json (or just subjects)
5. Create a superuser
    Type py -m manage createsuperuser<username of your choice>
6. Once all is ready, start the django server by typing
    py -m manage runserver
7. Go to the link that is provided and you'll be taken to the page.
