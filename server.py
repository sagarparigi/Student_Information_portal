from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['studentDB']
collection = db['Info']

# Load Student Details API
@app.route('/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    skip = (page - 1) * page_size

    students = collection.find().skip(skip).limit(page_size)
    total_records = collection.count_documents({})

    result = []
    for student in students:
        result.append({
            'id': student['id'],
            'name': student['name'],
            'total_marks': student['total_marks']
        })

    return jsonify({
        'students': result,
        'total_records': total_records
    })

# Server-side Filtering API
@app.route('/students/filter', methods=['POST'])
def filter_students():
    filter_criteria = request.json
    try:
        if 'total_marks' in filter_criteria.keys():
            filter_criteria['total_marks'] = int(filter_criteria['total_marks'])
    except:
        print('no Total_marks')

    students = collection.find(filter_criteria)
    result = []
    for student in students:
        result.append({
            'id': student['id'],
            'name': student['name'],
            'total_marks': student['total_marks']
        })
    return jsonify(result)


# Render the HTML page
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
