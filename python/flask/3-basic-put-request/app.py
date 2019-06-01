from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [{
    'name': 'Hugo',
    'area': 'DE',
    'id': 1
}, {
    'name': 'Lars',
    'area': 'DK',
    'id': 2
}, {
    'name': 'Paris',
    'area': 'DK',
    'id': 3
}]

# GET - http://localhost:5000/
@app.route('/')
def hello_world():
    return 'Hello world'

# GET - http://localhost:5000/employees
@app.route('/employees')
def get_employees():
    return jsonify({
        'employees': employees
    })

# PUT - http://localhost:5000/
@app.route('/employess', methods=['PUT'])
def insert_employees():
    post_data = request.get_json()
    print(post_data)
    employees.insert(0, {
        'name': post_data['name'],
        'area': post_data['area'],
        'id': post_data['id']
    })

    return "Success"

# GET - http://localhost:5000/employees/3
@app.route('/employees/<int:id>')
def get_employee(id):
    return_value = {}

    for employee in employees:
        if employee['id'] == id:
            return_value = employee

    return jsonify(return_value)

app.run(port=5000)