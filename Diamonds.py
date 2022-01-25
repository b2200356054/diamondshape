import sys
try:
    repeat = int(sys.argv[1])
except IndexError:
    print("Write a number!")
a = repeat
writelist = ["*"]  
def diamond():
    global a
    try:
        if a == 0:
            writelist.remove("*"*2)
            diamondlow()
            return None
        print("{}".format(" "*(a)), end="")
        for x in writelist:
            print(x, end="")
        print("{}".format(" "*(a)))
        writelist.append("*"*2)
        a = a-1
        diamond()
    except:
        print("Error!")
def diamondlow():
    global a 
    global repeat
    try:
        a = a+1
        if a == repeat:
            return None
        writelist.remove("*"*2)
        print("{} ".format(" "*(a)), end="")
        for x in writelist:
            print(x, end="")
        print("{}".format(" "*(a)))
        diamondlow()
    except:
        print("error here")
diamond()  