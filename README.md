---

# Flask Client-Server Starter Kit with SQLite

## Project Structure

```plaintext
my_flask_template/
├── client/
│   ├── gui.py
│   ├── requirements.txt
├── server/
│   ├── app.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── environment_loader.py
│   │   ├── logging_config.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── models.py
│   ├── database/
│   │   ├── create_tables.py
│   │   ├── data.sql
│   ├── requirements.txt
├── README.md
```

## Setting Up the Project

### Server

1. **Navigate to the `server` directory**:

   ```bash
   cd server
   ```

2. **Create a virtual environment and activate it**:
   - On Windows:

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the SQLite database**:
   - **Create the database and tables**:

     ```bash
     python database/create_tables.py
     ```

   - **Load initial data**:

     ```bash
     sqlite3 database/app.db < database/data.sql
     ```

5. **Run the server**:

   ```bash
   python app.py
   ```

### Client

1. **Navigate to the `client` directory**:

   ```bash
   cd client
   ```

2. **Create a virtual environment and activate it**:
   - On Windows:

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the client**:

   ```bash
   python gui.py
   ```

## Detailed Setup Instructions

### Configuring SQLite in the Project

1. **Add the SQLite configuration in `server/models.py`**:

   ```python
   from flask_sqlalchemy import SQLAlchemy
   from app import create_app

   app = create_app()
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/app.db'
   db = SQLAlchemy(app)

   # Define your models here
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)

       def __repr__(self):
           return f'<User {self.username}>'
   ```

2. **Create the database tables in `database/create_tables.py`**:

   ```python
   from models import db, User
   from app import create_app

   app = create_app()
   app.app_context().push()
   db.create_all()

   # Optionally add some initial data
   if not User.query.first():
       admin = User(username='admin')
       db.session.add(admin)
       db.session.commit()
   ```

3. **Add initial data in `database/data.sql`**:

   ```sql
   INSERT INTO user (username) VALUES ('testuser');
   ```

### Running the Application

1. **Start the Server**:
   - Ensure you're in the `server` directory and the virtual environment is activated:

     ```bash
     python app.py
     ```

   - The server will run on `http://127.0.0.1:5000`.

2. **Start the Client**:
   - Ensure you're in the `client` directory and the virtual environment is activated:

     ```bash
     python gui.py
     ```

3. **Interacting with the Server**:
   - Use the client GUI to ping the server and verify it's running.
   - Access server endpoints, such as `/ping`, via the client or directly in a browser or API client like Postman.

## Adding New Features

### Adding New Routes

1. **Define the new route in `server/modules/routes.py`**:

   ```python
   @api_bp.route('/new_route', methods=['GET'])
   def new_route():
       return jsonify({'message': 'This is a new route'}), 200
   ```

2. **Update the client to interact with the new route**:

   ```python
   def access_new_route():
       try:
           response = requests.get('http://127.0.0.1:5000/new_route')
           if response.status_code == 200:
               print('New route message:', response.json().get('message'))
           else:
               print('Unexpected response from server:', response.text)
       except requests.ConnectionError:
           print('Server is down or cannot be reached')
   ```

3. **Add a button or trigger in the client GUI to call `access_new_route()`**.

### Adding New Models

1. **Define the new model in `server/models.py`**:

   ```python
   class Product(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(80), unique=True, nullable=False)

       def __repr__(self):
           return f'<Product {self.name}>'
   ```

2. **Run migrations or manually update the database**:
   - Update the database schema by running:

     ```bash
     python database/create_tables.py
     ```

### Committing Changes to the Template

1. **Initialize a Git Repository**:

   ```bash
   cd my_flask_template
   git init
   git add .
   git commit -m "Initial commit of Flask client-server template"
   ```

2. **Push to GitHub**:
   - Create a new repository on GitHub (e.g., `flask-client-server-template`).
   - Push the local repository to GitHub:

     ```bash
     git remote add origin https://github.com/yourusername/flask-client-server-template.git
     git branch -M main
     git push -u origin main
     ```

### Using the Template for New Projects

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/flask-client-server-template.git new_project_name
   cd new_project_name
   ```

2. **Rename the Project and Update Configurations**:
   - Modify the project name and any specific configurations in the `README.md` and other files.

3. **Set Up the New Project**:
   - Follow the setup instructions above to set up and run the server and client for your new project.

---
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
