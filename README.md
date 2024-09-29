**Abstract**

Gradrotate.uk is an online web application that was created to streamline the automatic allocation of interns into placement positions; ensuring the allocated placement is suitable for the intern whilst delivering value to the employer.

It allows the Intern to identify the most suitable roles using their profile, recommending placement positions, and for the employer to identify the most suitable intern for each position so that they are productive during their placement.

The Gale-Shapely, Hungarian, Pareto and Random Serial Dictatorship algorithms can be selected to accurately match the intern with the placement position.
Gradrotate.uk is more effective than the former manual process as it reduces bias, in- creases accuracy and is more time efficient.

**Website**

The code is hosted on the Website: https://gradrotate.uk/

**Local setup**

This GitLab repository includes a Django application, with all dependencies listed on the requirements.txt. 

To run this software locally: 
1. Create a Python virtual machine environment: ```$python3 -m venv env```
2. Install Django: ```$pip install Django```
3. Clone the git repository: ```$git clone git@git.cs.bham.ac.uk:projects-2022-23/jxd965.git```
4. Install all dependencies listed on requirements.txt: ```$pip install -r requirements.txt -v```
5. Create new API keys for the google charts and Tom-Tom map APIs
6. Make database migrations: ```$python3 manage.py makemigrations --settings=gradRotate.local  ```
7. Migrate the changes on the database: ```$python3 manage.py migrate --settings=gradRotate.local  ```
8. Create a superuser with your credentials: ```$python3 manage.py createsuperuser --settings=gradRotate.local  ```
10. Create the correct groups: ```$python manage.py creategroup Intern Admin Manager --settings=gradRotate.local  ```
11. Start the Django development server: ```$python manage.py runserver --settings=gradRotate.local  ``` 
12. The development server should now be available on port 127.0.0.1:8000 on the browser

**Remote setup with CI/CD**

To deploy the local software to a web server:
1. Set up a Ubuntu web server on Digital Ocean with the spec: Docker 19.03.12 on Ubuntu 20.04 (1GB / 1CPU)
2. Ensure a GitLab runner is installed https://docs.gitlab.com/runner/
3. Generate a pair of RSA keys and link the server with GitLab
4. Generate a domain name with the appropriate DNS records 
5. Set up a GitLab repository 
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
    - Clone the git repository: ```$git clone git@git.cs.bham.ac.uk:projects-2022-23/jxd965.git```
    - Change the remote to the newly setup GitLab repository: ```$git remote set-url origin (YOUR REPO URL)```
    - Push all of the code to the GitLab repository: ```$git push -u origin master```
6. Complete local software steps for the application setup



