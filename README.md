We can create a todo list by logging in from the admin panel on our website and add categories and tags.


## Usage

**Preferably use `virtualenv`:**

```bash
# Create a virtual environment
virtualenv todo_vnv

# Activate the virtual environment
todo_vnv\Scripts\activate
pip install -r requirements.txt
# Apply the migrations to the database 
py manage.py migrate 
py manage.py createsuperuser # Follow the prompts to add an admin user
py manage.py makemigrations
py manage.py migrate
py manage.py runserver   		
```
![Ekran görüntüsü 2024-08-04 233316](https://github.com/user-attachments/assets/d56150b3-0296-44c1-ac9b-df38aa6e1078)


Can be edited locally with 127.0.0.1/admin

![Ekran görüntüsü 2024-08-04 233420](https://github.com/user-attachments/assets/7318b8d6-7c92-42a4-b81a-341b48bcf9c6)
