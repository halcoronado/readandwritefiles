def main():
    infile = open("clients.txt",'r')
    ##read line by line with for loop
    
    count= 1
    for client in infile:
        print(count,'. ',client.rstrip('\n'), sep="")
        count+=1

main()