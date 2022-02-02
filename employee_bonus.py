import csv

employee = open("EmployeePay.csv","r")

employee_file = csv.reader(employee, delimiter=',')
next(employee_file)
counter = 0


for record in employee_file:
    salary = int(record[3])
    bonus = float(record[4])
    total = salary+(bonus*salary)
    print("First Name:", record[1])
    print("Last Name:", record[2])
    print ("Salary:" +' $', format(salary,',.2f'), sep='')
    print ("Bonus:"+' $', format(bonus*salary,',.2f'), sep='')
    print ("Total Pay:"+' $', format(total,',.2f'),sep='')
    input()


    
    
    
