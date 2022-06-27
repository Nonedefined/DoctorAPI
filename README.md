# DoctorAPI

## Setup
Clone the repository
```
git clone https://github.com/Nonedefined/doctorAPI.git
cd doctorAPI
```
Create a virtual environment to install dependencies in and activate it
```sh
python3 -m venv venv
source env/bin/activate
```
Then install the dependencies
```
cd doctorAPI
pip install -r requirements.txt
```
You can you use it without database settings because it is on remote server.
Now you can run server
```
python3 manage.py runserver
```
Data for admin panel
name: admin
password: admin

## Endpoints
1. Endpoint: GET /direction
Run this in your local browser by entering http://127.0.0.1:8000/direction/
This endpoint allows you to get all direction
2. Endpoint: GET /doctor
Run this in your local browser by entering http://127.0.0.1:8000/doctor/
This endpoint allows you to get all doctors
3. Endpoint: GET /doctor/<int:pk>/
Run this in your local browser by entering http://127.0.0.1:8000/doctor/1/
This endpoint allows you to get doctor by ID

