How Members Should Use:
- members should only use the master account to add themselves as contributors
- members should use their own accounts to push/pull/edit

Backend:

Done:
Intial django server set up
Defined models for reservation and room table
Defined API methods for reservation and room table

Need to work on:
Set up Oauth Authentication and openID
Define Roles

## 🛠 set-up

1. Set up local virtual enviroment

   ```sh
   python3 -m venv venv
   ```
   ```sh
   source venv/bin/activate
   ```

2. Install the dependencies from requirement.txt

   ```sh
   pip install -r requirement.txt
   ```
3. Migrate and connect to your database

   connect to your database through backend/cfehome/settings.py 

4. Start the development server

   ```sh
   python3 -m manage.py runserver
   ```

frontend:
