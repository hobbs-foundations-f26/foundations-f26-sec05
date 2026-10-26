import sys

if len(sys.argv) == 1:
    print('too few arguments, please name a file to print')
else:
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        print(file.read())