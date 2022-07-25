k="yes"
while k==("yes"):
    order=input("read or write or create ?:")
    if order == "read":
        file_name=input("enter the file name:")
        try:
            file = open(file_name+".txt", "r")
            print(file.read())
            file.close()
        except:
            print("there is no file has this name")
    elif order =="write":
        file_name = input("enter the file name:")
        file = open(file_name+".txt", "a")
        file.write(("\n")+input("enter the note"))
        file.close()
    elif order == "create":
        file_name = input("enter the file name:")
        file = open(file_name + ".txt", "w")
        file.write(("\n") + input("enter the note:"))
        file.close()
    else:
        print("there is no action has this name")
    k=input("are you want to try again?")
    if k=="no":
        print("program finshed")
    elif k=="yes":
        print("lets try another time")
    else:
        print("wrong input")