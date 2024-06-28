from fastapi import FastAPI

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

@app.post('/add_employees')
def add_employees(name: str,age: int,position: str):
    if not employees:
        new_id = 1
    else:
        new_id = max(employees.keys())+1         
        employees[new_id]['name'] = name
        employees[new_id]['age'] = age
        employees[new_id]['position'] = position
        
        return employees[new_id]