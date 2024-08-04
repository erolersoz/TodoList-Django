Usage
preferably use virtualenv
virtualenv todo_vnv
todo_vnv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser # add admin user
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
    		
