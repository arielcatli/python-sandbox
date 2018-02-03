#Working with files. Writing a CSV file.

import random
def main():
    create_csv("sample.csv",1000,10,0,100)
    print("------->")
    print(read_csv("sample.csv"))

def create_csv(filename,lines,columns,min,max):
    with open(filename, "a") as write_file:
        for line in range(0,lines):
            for value in range(0, columns):
                write_file.write(str(random.randint(min,max)))
                write_file.write(",")
            write_file.write("\n")


#Creates a list from the CSV file
def read_csv(filename):
    read_list = []
    with open(filename) as read_file:
        for line in read_file:
            read_list.append(line.replace("\n",""))
    return read_list

if __name__ == "__main__":
    main()
