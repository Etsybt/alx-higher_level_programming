#!/usr/bin/python3
if __name__ == "__main__":
    import sys

# Remove the script name (first argument) from sys.argv
    arguments = sys.argv[1:]

    num_arguments = len(arguments)

    if num_arguments == 0:
	print("0 arguments.")
    elif num_arguments == 1:
	print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i, arg in enumerate(arguments, start=1):
	print("{}: {}".format(i, arg))


