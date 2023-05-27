# importing the modules
import csv
import random

# Generate random student data
def generate_student_data(num_students):
    student_data = []
    for i in range(1, num_students + 1):
        student = {
            'id': i,
            'name': f'Student {i}',
            'total_marks': random.randint(50, 100)
        }
        student_data.append(student)
    return student_data

# Save student data to CSV file
def save_to_csv(data, file_path):
    keys = data[0].keys()
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Generate and save random student data to CSV file
num_students = 500  # Change the number of students as per your requirement
student_data = generate_student_data(num_students) # we are calling the method to generate the random data
file_path = 'student_data.csv'  # Replace with the desired file path
save_to_csv(student_data, file_path) # save file to the folder