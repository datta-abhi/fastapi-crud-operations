from fastapi import FastAPI
from data_models import Emp,UpdateEmp

# create instance of FASTAPI
app = FastAPI(
    title = "CRUD operations",
    description= "This API will implement the CRUD operations"
)

# create employee db as dictionary
employees = {
    1: {'name': 'Bob', 'age': 24, 'position': 'manager'},
    2: {'name': 'Alice', 'age': 30, 'position': 'developer'},
    3: {'name': 'Charlie', 'age': 28, 'position': 'designer'},
    4: {'name': 'Diana', 'age': 35, 'position': 'analyst'},
    5: {'name': 'Eve', 'age': 26, 'position': 'tester'}
}

# homepage
@app.get('/')
def index():
    return "Welcome to our API service"

@app.get('/employees')
def get_all():
    return employees

@app.get('/employee/{emp_id}')
def get_emp_info(emp_id:int):
    if emp_id not in employees:
        return f"No employee found with employee ID {emp_id}"
    else:
        return employees[emp_id]

# adding new employee (POST)
@app.post('/add-employee')
def add_employees(emp:Emp):
    if not employees:
        new_id = 1
    else:
        new_id = max(employees.keys())+1         
    employees[new_id] = emp.model_dump()
                
    return employees[new_id]

# updating existing employee info
@app.put('/update-employee/{emp_id}')
def update_employee(emp_id:int, emp: UpdateEmp):
    if emp_id not in employees:
        return f"No employee found with employee ID {emp_id}"
    else:
        if emp.name is not None:
            employees[emp_id]['name'] = emp.name
        if emp.age is not None:
            employees[emp_id]['age'] = emp.age
        if emp.position is not None:
            employees[emp_id]['position'] = emp.position
            
        return employees[emp_id]    # returns updated employee info
                    