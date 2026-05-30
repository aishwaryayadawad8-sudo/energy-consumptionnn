@echo off
echo ========================================
echo SDG 7 Dashboard - Starting Server
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Running migrations...
python manage.py migrate
echo.
echo Starting development server...
echo Open your browser and visit: http://127.0.0.1:8000/
echo.
python manage.py runserver
