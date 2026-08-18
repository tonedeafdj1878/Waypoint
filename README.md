1. Clone the Repository
Bash

git clone https://github.com/tonedeafdj1878/Waypoint.git
cd Waypoint

2. Create and Activate a Virtual Environment
Bash

python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

3. Install Dependencies
Bash

pip install -r requirements.txt

4. Run Database Migrations
Bash

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional for Admin Access)
Bash

python manage.py createsuperuser

6. Run the Development Server
Bash

python manage.py runserver

Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
Running Tests

To execute the automated unit test suite:
Bash

python manage.py test
