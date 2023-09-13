#My Python Flask API

##Introduction
This is an API created with python flask, using the flask run command. This API lets you perform CRUD (create, read, update, delete) operations on a database. 
It is a simple and powerful tool used for managing your data.

##Getting Started
To set up your development environment and get started with this API, follow these steps:
 ###prerequisites-
 Please check the requirements file for installation packages and any other dependencies.

### Installation
1. Clone this repository to your local machine.
2. Navigate to the project folder using the command line.
3. Create a virtual environment (optional but recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate 
 #On Windows, use: venv\Scripts\activate

Install the required dependencies using pip:
pip install -r requirements.txt

Running the API
To run the API locally, use the following command:
python app.py

The API will start running on http://localhost:5000.

How to Use the API
The API provides the following endpoints:

Create a person (POST)
Endpoint: /api
Send a POST request with JSON data to create a new record.

Read person (GET)
Endpoint: /api
Send a GET request to retrieve all records from the database.

Update a person (PUT)
Endpoint: /api/<string:user_id>
Send a PUT request with JSON data to update a specific person by ID.

Delete a person (DELETE)
Endpoint: /api/<string:user_id>
Send a DELETE request to remove a specific record by ID.

For more detailed information on how to use each endpoint, check the API documentation file.

