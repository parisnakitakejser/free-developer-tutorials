from flask import Flask, jsonify, request, redirect, Response
import json

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

def vlidate_put_data(data_object):
    if ('name' in data_object and 'area' in data_object and 'id' in data_object):
        return True
    else:
        return False


def vlidate_post_data(data_object):
    if ('name' in data_object and 'area' in data_object):
        return True
    else:
        return False


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

# PUT - http://localhost:5000/employees
@app.route('/employees', methods=['PUT'])
def insert_employees():
    post_data = request.get_json()

    if vlidate_put_data(data_object=post_data):
        employees.insert(0, {
            'name': post_data['name'],
            'area': post_data['area'],
            'id': post_data['id']
        })

        return redirect('/employees')
    else:
        response = Response(json.dumps({
            'error': 'Invalid employee data',
            'help-string': 'wrong input data'
        }), status=400, mimetype='application/json')

        return response

# GET - http://localhost:5000/employees/3
@app.route('/employees/<int:id>')
def get_employee(id):
    return_value = {}

    for employee in employees:
        if employee['id'] == id:
            return_value = employee

    return jsonify(return_value)

@app.route('/employees/<int:id>', methods=['POST'])
def update_employee(id):
    global employees

    request_data = request.get_json()
    if vlidate_post_data(data_object=request_data):
        new_employee = {
            'name': request_data['name'],
            'area': request_data['area'],
            'id': id
        }

        i = 0
        change = False
        for employee in employees:
            if employee['id'] == id:
                employees[i] = new_employee
                change = True

            i += 1

        if change:
            return redirect(f'/employees/{id}')
        else:
            return Response("", status=404)
    else:
        return Response("", status=400)

app.run(port=5000)