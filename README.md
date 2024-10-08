# TestApp

## About
Cross-platform application to learn how to cover web apps with autotests.

## Application Description
Simple test management system. It provides features to create, update, delete, run and view list of test cases.
It is possible to view list of all test runs and get stats of all test cases in the system.
Demo features designed additionally to give automation test engineers possibility to handle 
long waitings and multiple ajax requests

### Features
- Registration
- Login
- View Test Stats
- List test cases
- Create test case
- Update test case
- Delete test case
- Run test case (make it pass or fail)
- Download test cases to csv file
- Upload test cases as csv file  
- List test runs
- Open page after specified delay
- Open page and wait specific number of ajax requests handled
- Handle HTTP 500 errors
- Rest API for API and performance testing
- iFrame in demo pages

## API
[Api doc in postman](https://documenter.getpostman.com/view/27990079/2s93sgV9xC)

## Application has:  
- Web UI
- Mobile version of web UI
- coordinates in UI header for location tests   
- REST services
- SQLite DB to work with DB without installing 3rd party services
- Page with different input types to play with

## Preconditions
- Python 3.10+
- Install Django using `pip install -r requirements.txt`
- Free network port 8000

## How to run
1. Open CLI
2. Navigate to project folder
3. Execute command: `python manage.py runserver`  

Server will be started at http://127.0.0.1:8000  

## Default users
| Name         | Password  |
|--------------|-----------|
| default      | QADqwerty | 
| secondary    | QASqwerty | 
