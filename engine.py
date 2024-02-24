#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from uuid import uuid4
from urllib import parse
from sys import argv



Base = declarative_base()

class BaseModel:
    
    def to_dict(self):
        obj = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_') and not isinstance(value, sqlalchemy.orm.collections.InstrumentedList):
                obj[key] = value
        return obj
    def __repr__(self):
        return f"<{self.__class__.__name__}  {self.__dict__}"


class Employee(Base, BaseModel):
    """Class defining the employee table"""
    __tablename__ = 'employees'
    employee_id = Column(String(36), primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    employee_email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    jobs = relationship("Job", back_populates="employee")
    employee_bids = relationship("Bid", back_populates="employee")

class Contractor(Base, BaseModel):
    """Class defining the contractors table"""
    __tablename__ = 'contractors'
    contractor_id = Column(String(36), primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    contractor_email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    jobs = relationship("Job", back_populates='contractor')

class Job(Base, BaseModel):
    """Class defining the jobs table"""
    __tablename__ = 'jobs'
    job_id = Column(String(36), primary_key=True, nullable=False)
    date_posted = Column(DateTime, nullable=False)
    job_state = Column(Enum("bid_on", "bid_off"), default="bid_on")
    number_of_bids = Column(Integer, nullable=False, default=0)
    description = Column(String(250), nullable=False)
    budget = Column(Integer, nullable=False, default=0)
    date_assigned = Column(DateTime, nullable=True)
    cont_id = Column(String(36), ForeignKey('contractors.contractor_id'), nullable=False, unique=False)
    emp_id = Column(String(36), ForeignKey('employees.employee_id'), nullable=True, unique=False)

    contractor = relationship("Contractor", back_populates="jobs")
    employee = relationship("Employee", back_populates="jobs")
    employee_bids = relationship('Bid', back_populates='job')
    milestones = relationship('Milestone', back_populates='job')

class Bid(Base, BaseModel):
    """Class defining the employee_bids to hold all the bids a user has"""
    __tablename__ = 'employee_bids'
    bid_id = Column(String(36), primary_key=True, nullable=False)
    job_id = Column(String(36), ForeignKey('jobs.job_id'), nullable=False)
    emp_id = Column(String(36), ForeignKey('employees.employee_id'), nullable=False)
    date_bid = Column(DateTime, nullable=False)


    employee = relationship('Employee', back_populates='employee_bids')
    job = relationship('Job', back_populates='employee_bids')


class Milestone(Base, BaseModel):
    __tablename__ = 'milestones'
    milestone_id = Column(String(36), primary_key=True, nullable=False)
    milestone_name = Column(String(100), nullable=False)
    job_id = Column(String(36), ForeignKey('jobs.job_id'), nullable=False, unique=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    job = relationship('Job', back_populates='milestones')


user = argv[1]
print(user)
pwd = argv[2]
pwd  = parse.quote(pwd, safe='')
database = argv[3]


engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}")
Base.metadata.create_all(engine)