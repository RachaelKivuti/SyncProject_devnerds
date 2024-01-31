#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum
from uuid import uuid4
from urllib import parse
from sys import argv


class BaseModel:
    
    
    def to_dict(self):
        obj = {}
        for key, value in self.__dict__.items():
            obj[key] = value
        return obj

Base = declarative_base()

class Employee(Base, BaseModel):
    """Class defining the employee table"""
    __tablename__ = 'employees'
    employee_id = Column(String(36), primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    employee_email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    jobs = relationship("Job", back_populates="employee")

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
    job_state = Column(Enum("bid_on", "bid_off"))
    number_of_bids = Column(Integer, nullable=False, default=0)
    description = Column(String(250), nullable=False)
    budget = Column(Integer, nullable=False, default=0)
    cont_id = Column(String(36), ForeignKey('contractors.contractor_id'), nullable=False, unique=True)
    emp_id = Column(String(36), ForeignKey('employees.employee_id'), nullable=True, unique=True)

    contractor = relationship("Contractor", back_populates="jobs")
    employee = relationship("Employee", back_populates="jobs")


user = argv[1]
print(user)
pwd = argv[2]
pwd  = parse.quote(pwd, safe='')
database = argv[3]

engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}")
Base.metadata.create_all(engine)