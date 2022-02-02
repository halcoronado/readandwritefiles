import csv
customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')

#to skip a line if the file contains a header record
next(customer_file)
outfile = open('customers_country.csv','w')

for record in customer_file:
    #outfile.write("Full Name:"record[1],record[2]))
    #outfile.write("Country:", record[4])


    
    #print("Last Name:",record[2])

    #print(type(record))

