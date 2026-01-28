<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/73d73621-85b1-4626-989e-32fa1c9a1c6f" /># Task Management System
This is a simple API to help teams manage their tasks. It is built using FastAPI and saves data in two ways at the same time: in JSON files and a SQLite Database.

## How the project is organized
I followed a modular structure to keep the code clean:

- main.py: The start of the application. It connects everything together.

- routers/: Contains the logic for Users and Tasks.

- schemas/: Contains the rules for our data (Validation).

- utils/: Helper files for saving data to JSON and the Database.

## Main Features
1. Smart Validation: The system automatically checks your data. For example, Task titles must start with a Capital letter.

2. User Roles: You can create users as admin, manager, or team_member.

3. Dual Storage: When you create something, it saves to a .json file and a .db file so your data is safe.

4. Search: You can find tasks by User ID or find which User is working on a specific Task.

## How to use it

1. Install the tools: Open your terminal and type: pip install fastapi uvicorn sqlalchemy

2. Run the app: Type: uvicorn main:app --reload

3. Open the Dashboard: Go to http://127.0.0.1:8000/docs in your browser. This is the Swagger UI where you can test the API.

## HTML page

<img width="1920" height="778" alt="Screenshot (185)" src="https://github.com/user-attachments/assets/d7230cb4-26bb-4e44-a8d9-2a98a8411579" />

<img width="1906" height="560" alt="Screenshot (186)" src="https://github.com/user-attachments/assets/b9c5d3e8-0fb5-4397-883f-164a17b72dca" />

