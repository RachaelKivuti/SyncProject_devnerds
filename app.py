from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from engine import Base, Employee, Contractor, Job, Bid, Milestone
from datetime import datetime
from uuid import uuid4
from sys import argv
import urllib

app = Flask(__name__)

user = ''
pwd = ''
database = ''

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}'
db = SQLAlchemy(app)

@app.route('/signup/employee', methods=["POST","GET"])
def employee():
    '''Method to create an employee'''
    if request.method == 'POST':
    
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        employee_email = request.form['email']
        password = request.form['password']
        if not first_name or not last_name or not employee_email or not password:
            return render_template('signin.html', error='Please fill all the required fields')
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
            return render_template('signin.html', error=e)
    return render_template('signin.html')


@app.route('/signup/contractor', methods=["POST", "GET"])
def contractor():
    '''End-point to create a new contractor'''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        if not first_name or not last_name or not email or not password:
            return render_template('contractor.html', error="Please fill all required fields.")
        id = str(uuid4())
        try:
            new_contractor = Contractor(
                contractor_id = id,
                first_name = first_name,
                last_name = last_name,
                contractor_email = email,
                password = password
            )
            db.session.add(new_contractor)
            db.session.commit()
            return jsonify({'message': f'contractor {first_name} successively created'})
        except Exception as e:
            return render_template('contractor.html', error=e)
    return render_template('contractor.html')


@app.route('/api/v1.0/employees')
def get_employees():
    '''Returns all the employees in the platform'''
    with db.session.begin():
        employees = db.session.execute(db.select(Employee).order_by(Employee.employee_email)).scalars()
    try:
        employee_list = [employee.to_dict() for employee in employees]
        return jsonify({'employees': employee_list})
    except Exception as e:
        return jsonify({'message': "Error querying the database"})

@app.route('/api/v1.0/employees/<string:id>', methods=['GET'])
def get_employee():
    '''Get details of a specific employee'''
    try:
        with db.session.begin():
            employee = db.session.execute(db.select(Employee).filter_by(employee_id=id)).scalar_one()
    except Exception as e:
        pass

@app.route('/api/v1.0/jobs', methods=["GET"])
def get_jobs():
    '''Retrieve all the jobs available in the platform'''
    with db.session.begin():
        jobs = db.session.execute(db.select(Job).filter_by(job_state='bid_on')).scalars()
        job_list = [job.to_dict() for job in jobs]
    return jsonify({'jobs': job_list})

@app.route('/api/v1.0/jobs', methods=['POST'])
def create_job():
    '''API to create a new job'''
    if request.method == 'POST':
        data = request.json
        state = data.get('job_state')
        description = data.get('description')
        budget = data.get('budget')
        cont_id = data.get('contractor_id')
        if not state or not description or not budget or not cont_id:
            return jsonify({'message': 'null fields'})
        job_id = str(uuid4())
        
        new_job = Job(
            job_id = job_id,
            date_posted = datetime.now(),
            job_state = "bid_on",
            description = description,
            budget = budget,
            cont_id = cont_id
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'new job created'})


@app.route('/api/v1.0/bid_job', methods=['POST'])
def bid_job():
    '''API for biding a job'''
    if request.method == 'POST':
        data = request.json
        bid_id = str(uuid4())
        job_id = data['job_id']
        emp_id = data['employee_id']
        new_bid = Bid(
            bid_id = bid_id,
            job_id = job_id,
            emp_id = emp_id,
            date_bid = datetime.now()
        )
        with db.session.begin():
            job = db.session.execute(db.select(Job).filter_by(job_id=job_id)).scalar_one()
            job.number_of_bids += 1
        db.session.add(new_bid)
        db.session.commit()
        return jsonify({'message': f'job bidded successively'})

@app.route('/api/v1.0/employee_bids/<string:emp_id>')
def get_bids(emp_id):
    '''API to retrieve all the bids that an employee has'''
    try:
        with db.session.begin():
            jobs = db.session.execute(db.select(Bid.job_id).filter_by(emp_id=emp_id).order_by(Bid.date_bid)).scalars()

        print(jobs)
        jobs = [job for job in jobs]
        print(jobs)
        bids_list = []
        for bid in jobs:
            job = db.session.execute(select(Job).filter_by(job_id=bid)).scalar_one()
            bids_list.append(job.to_dict())
        return jsonify({"employee_bids": bids_list})
    except Exception as e:
        return jsonify({"message": str(e)})


@app.route('/api/v1.0/add_milestone', methods=['POST'])
def add_milestone():
    '''API to add a new milestone for a specific job'''
    data = request.json
    job_id = data['job_id']
    milestone_name = data['milestone_name']
    start_date = data['start_date']
    end_date = data['end_date']
    milestone_id = str(uuid4())
    
    new_milestone = Milestone(
        milestone_id = milestone_id,
        milestone_name = milestone_name,
        job_id = job_id,
        start_date = start_date,
        end_date = end_date
    )
    db.session.add(new_milestone)
    db.session.commit()
    return jsonify({'message': 'milestone added successively'})

@app.route('/api/v1.0/employee_overview')
def employee_overview():
    '''API to return all the details of an employee, the jobs the person is working on/won the bid'''
    data = request.json
    employee_id  = data['employee_id']
    with db.session.begin():
        jobs = db.session.execute(db.select(Job).filter_by(emp_id=employee_id).order_by(Job.date_assigned)).scalars()
        job_list = [job.to_dict() for job in jobs]
        try:
            first_job = job_list[0]
        except IndexError:
            return jsonify({'message': 'no job currently assigned'})
        incoming_deadline = db.session.execute(db.select(Milestone).filter_by(job_id=first_job['job_id']).order_by(Milestone.end_date)).scalar_one()
    overview = {
        'jobs': job_list,
        'number_of_jobs': len(job_list),
        'incoming_deadline': incoming_deadline.end_date
    }
    return jsonify({'overview': overview})