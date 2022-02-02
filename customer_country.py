import csv
from os import sep
from tkinter.ttk import Separator
customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)
outfile = open('customers_country.csv','w')
outfile.write('First Name,Last Name,Country'+'\n')
counter = 0

for record in customer_file:
    outfile.write(record[1]+','+record[2]+','+record[4]+'\n')
    counter = counter+1

print(counter)
outfile.close()