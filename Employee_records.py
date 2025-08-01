data=[("Alice","QA",50000),("Bob","Dev",75000),("Charlie","QA",45000),("David","Devops",60000)]
for name,dept,salary in data:
    print(name,dept)
employees = {} #creating a dictionary
for name,dept,sal in data:
    employees[name] = {"department":dept,"salary":sal}
#print(employees)
#print(employees.keys())
#print(employees.values())
#no. of employees in each department
for info in employees.values():
    print(info)