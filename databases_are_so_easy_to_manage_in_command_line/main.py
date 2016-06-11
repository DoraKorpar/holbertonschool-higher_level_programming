import sys

list = ["create", "print", "insert", "delete"]

if len(sys.argv) < 2:
    print ("Please enter an action")
else:
    for i in list:
        if i == str(sys.argv[1]):
            print i
            sys.exit()
    print ("Undefined action %s" % sys.argv[1])

