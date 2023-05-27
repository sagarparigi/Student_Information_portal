# Student Details Grid System

The Student Details Grid is a web application that allows users to view and filter student details using a grid system.
It provides backend APIs for loading student details with pagination and server-side filtering.

# Requirements

- Python 3.7 or above
- Flask
- pymongo
- MongoDB

or 

- It provides a backend API built with Flask and a frontend user interface built with HTML, CSS, and JavaScript.
- The application utilizes MongoDB as the database for storing student information.


# Usage

1. Load Student Details API:

   - The API endpoint for retrieving student details is : '/students'.
   - Method : GET
   - Parameters:
     - `page` (optional): Specifies the page number for pagination. Default is `1`.
     - `page_size` (optional): Specifies the number of records per page. Default is `10`.
   - Example usage:

     ```
     GET /students?page=1&page_size=10
     ```

2. Server-side Filtering API:

   - The API endpoint for server-side filtering is : '/students/filter'.
   - Method: POST
   - Request body: JSON object containing the filter criteria.
   - Example usage:
   
     ```
     POST : /students/filter
     Content-Type : application/json
     {
       "name": "John",
       "total_marks": 90
     }
     ```
     
3. Frontend:

   - Open the `index.html` file in a web browser to access the Student Details Grid.
   - The grid displays student details with columns for ID, Name, and Total Marks.
   - Use the filter form to input filter criteria and click "Apply Filter" to filter the student details.
   - Click the "Reset Filter" button to clear the filters and display all student details.
   - The grid supports pagination, with the number of records per page specified in the backend API.

4. Database:
   
   - MongoDB (NoSQL Database)


# Other necessary files : 

Here I have written two python scripts :

   - create_randomData.py : This script is used to generate the random data ( ID , Name , Total Marks ) and will store in csv file for further process.
   - push_data_toMongo.py : This script is used to push data in CSV file to the MongoDB local database and we will use that database for our tasks.


# Configuration

MongoDB Connection:

- By default, the Flask application assumes that the MongoDB server is running on `localhost` at the default port `27017`. 
- If your MongoDB setup differs, modify the connection URL in the Flask code (`app.py`).
  
  
# Installation and Setup

- Clone the repository : git clone https://github.com/sagarparigi/Student_Information_portal.git
- Install the required dependencies using pip.
- Start the MongoDB server. Make sure it is running on localhost at the default port 27017.

# Last Step 

- Start the Flask server : python app.py

