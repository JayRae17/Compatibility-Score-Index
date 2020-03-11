# Compatibility-Score-Index

Starter Code for Capstone Project

Steps to properly install dependencies on local machine are as follows in VS Code Terminal:

1.  Clone Repository from Alauna-97 Compatibility Score Index by running this command
    git clone https://github.com/Alauna-97/Compatibility-Score-Index.git Compatibility-Score-Index

2.  Check python version:  
    python --version

    # Python 3 and over should be installed on your local machine

3.  Create Virtual Environment :
    cd Compatibility-Score-Index
    python3 -m venv venv

4.  Install Dependencies:
    pip install -r requirements.txt

5.  Create Branch to work on your specific task (etc).

6.  # Look in the app folder and click init.py. Line 7 shows that we are using Mysql and the name of the database is csi.

    # In VS Code, you can create the database by using conventional methods (mysql -u root --> create database csi --> use csi)

7.  # Models.py has the Python Classes used to create tables in CSI Database. To create these tables in CSI on your local machine, run the following commands.

    # N.B. Ensure you are in the Compatibility-Score-Index Folder.

    python flask-migrate.py db init
    python flask-migrate.py db migrate
    python flask-migrate.py db upgrade

    # When we go back to the CSI Database, we should see the same tables in our models.py file and alembic version table.

8.  # To post to the DB, type the following commands:

    python
    from app import db
    from app.models import User, Regular <!--(whichever table you want to add records to, ensure to use the same class names in models.py) -->
    user = Organizer([attribute name] = [attribaute value])
    db.session.add(user)
    db.session.commit()

9.  To view the webpage:
    python run.py

    # Go to your web browser and go to localhost

10.  To activate the virtual environment:
    .\venv\scripts\activate
    # (venv) should appear before Folder path in the terminal
