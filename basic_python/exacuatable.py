import time

def f1(text):
    print(text)

def f2(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total


# if __name__ == "__main__" checks to see if file __name__ (magic or dunder) is the __main__ 
# Since it always is, proceeds to execute code below.
# The line signals to other people that this is an executable .py file 

if __name__ == "__main__":

    text = "hello world"
    f1(text)

    output = f2(1,2,3)

    print(output)