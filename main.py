import sys
from token import *

def main():

    #Handles cmdline args
    if len(sys.argv) != 2:
        print('Incorrect num commandline args: ' + str(len(sys.argv)))
        sys.exit(1)
    elif '.pc' not in sys.argv[1]:
        print('Incorrect file input')
        sys.exit(1)

    file_str = ''

    try:
        with open(sys.argv[1], 'r') as file:
            file_str = file.read()
    except FileNotFoundError:
        print("File '" + sys.argv[1] + "' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(tokenize(file_str))


if __name__ == "__main__":
    main()
