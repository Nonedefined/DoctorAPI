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
```
name: admin
password: admin
```
## Endpoints
1. Endpoint GET /direction/
- Run this in your local browser by entering ```http://127.0.0.1:8000/direction/```
- This endpoint allows you to get all directions.
2. Endpoint GET /doctor/
- Run this in your local browser by entering ```http://127.0.0.1:8000/doctor/```
- This endpoint allows you to get all doctors with pagination 2 per page. For example ```http://127.0.0.1:8000/doctor/?page=2```
- Also you can filter it by directions or experience and order by birthdate or experience. For example ```http://127.0.0.1:8000/doctor/?directions=Psychiatrists&experience_min=5&experience_max=20&ordering=birthdate```
3. Endpoint GET /doctor/<int:pk>/
- Run this in your local browser by entering ```http://127.0.0.1:8000/doctor/1/```
- This endpoint allows you to get information about doctor by ID.

