# importing the modules
import pymongo
import pandas as pd

# here we have written this script , inorder to add the details to the database (MongoDB).

# here we are creating connection to the database (This database is a Local Database) 
client = pymongo.MongoClient("mongodb://localhost:27017")

data = pd.read_csv("student_data.csv") # reading data from already generated file.
final_data = data.to_dict(orient="records") # here we are converting that in such a format that is easy to append to DB.
db = client['studentDB'] # We are creating a database named : studentDB
db.Info.insert_many(final_data) # Here we are writing a query inorder to add all the data to database with Collection named : Info

# and finally the data is in Database and we can perform given task.