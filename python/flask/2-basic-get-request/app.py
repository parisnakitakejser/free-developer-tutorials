from flask import Flask, jsonify

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

# http://localhost:5000/
@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/employees')
def get_employees():
    return jsonify({
        'employees': employees
    })

@app.route('/employees/<int:id>')
def get_employee(id):
    return_value = {}

    for employee in employees:
        if employee['id'] == id:
            return_value = employee

    return jsonify(return_value)

app.run(port=5000)