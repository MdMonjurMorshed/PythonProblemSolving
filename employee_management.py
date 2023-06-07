class Employee:
    def __init__(self,name,id,salery,department) :
        self.name=name
        self.id=id
        self.salery=salery
        self.department=department

    def calculate_salery(self,working_hours):
        overtime=0
        if working_hours>50:
            overtime=working_hours-50
        self.salery= self.salery+(overtime*self.salery/50)        
    
    def assign_department(self,emp_department):
        self.department=emp_department

    def print_empDetails(self):
        print(f"employee name:{self.name}\nemployee id:{self.id}\nemployee department:{self.department}\nemployee salery:{self.salery}")  

emp1=Employee('tahi',123,18000,'app development') 
emp1.assign_department("web development")
emp1.calculate_salery(80)
emp1.print_empDetails()         