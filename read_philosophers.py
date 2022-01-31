def main():
    infile = open("philosophers.txt","r")
    ##readsallcontents without \n
    #file_contents = infile.read()

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
    
    print(line1)
    print(line2)
    print(line3)
def add_my_name():
    outfile= open('philosophers.txt','a')

    outfile.write('Hal Coronado\n')

    outfile.close()


main()
add_my_name()