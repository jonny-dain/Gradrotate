This repository was provided by the University of Birmingham to host the final year project code. 

Website: https://gradrotate.uk/


This repository includes a Django application, with all dependencies listed on the requirements.txt. 

To run this software locally: 
- Create a Python virtual machine environment: $python3 -m venv env
- Install Django: $pip install Django
- Clone the git repository: git clone git@git.cs.bham.ac.uk:projects-2022-23/jxd965.git
- Install all dependencies listed on requirements.txt: $pip install -r requirements.txt -v
- Create new API keys for the google charts and Tom-Tom map APIs
- Make database migrations: $python3 manage.py makemigrations
- Migrate the changes on the database: $python3 manage.py migrate
- Create a superuser with your credentials: $python3 manage.py createsuperuser 
- Create the correct groups: python manage.py creategroup Intern Admin Manager
- Start the Django development server: $python manage.py runserver --settings=gradRotate.local   
- The development server should now be available on port 127.0.0.1:8000 on the browser


To deploy the local software to a web server:
- Set up a Ubuntu web server on Digital Ocean with the spec: Docker 19.03.12 on Ubuntu 20.04 (1GB / 1CPU)
- Ensure a GitLab runner is installed https://docs.gitlab.com/runner/
- Generate a pair of RSA keys 
- Set up a GitLab repository 
    - Go to Settings > CI/CD > Runner
    - Follow the steps to link your hosted GitLab Runner.
    - Go to Settings > CI/CD > Variables
    - Create a new variable DATABASE_NAME: the database the django app will use
    - Create a new variable DATABASE_PASS: the password to create for DATABASE_USER
    - Create a new variable DATABASE_USER: the postgresql user
    - Create a new variable DJANGO_SUPERUSER_PASSWORD
    - Create a new variable SECRET_KEY: the django secret key for production
    - Create a new variable SSH_PRIVATE_KEY: the SSH private key
    - Create a new variable SSH_PRIVATE_KEY_PASSWORD: the SSH key password
    - Create a new variable UBUNTU_SERVER: the IP address of the Digital Ocean Ubuntu droplet
    - Push all of the code to the GitLab repository: $git push -u origin master
    - Complete local software steps for the application setup



