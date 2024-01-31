from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from engine import Base, Employee, Contractor, Job
from uuid import uuid4
from sys import argv
import urllib

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}'
db = SQLAlchemy(app)

@app.route('/employee', methods=["POST","GET"])
def employee():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            employee_email = request.form['email']
            password = request.form['password']
        except KeyError as e:
            return jsonify({'message': f'please fill in all the require fields {e}'})
        id = str(uuid4())
        try:
            new_employee = Employee(
                employee_id = id,
                first_name = first_name,
                last_name = last_name,
                employee_email = employee_email,
                password = password
            )
            db.session.add(new_employee)
            db.session.commit()
            return jsonify({'message': f'employee {first_name} created'})
        except Exception as e:
            return jsonify({"message": f"Error: {str(e)}"})
    return render_template('signin.html')