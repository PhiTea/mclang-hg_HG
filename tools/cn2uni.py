import pyperclip

LastOrigin = ""
LastUnicode = ""
LastCUnicode = ""
while True:
    origin = input("> ")
    if origin.split(" ")[0] == "copy" and len(origin.split(" ")) == 2:
        if origin.split(" ")[1] == "ori":
            pyperclip.copy(LastOrigin)
            print("copied.")
        elif origin.split(" ")[1] == "uni":
            pyperclip.copy(LastUnicode)
            print("copied.")
        elif origin.split(" ")[1] == "cuni":
            pyperclip.copy(LastCUnicode)
            print("copied.")
        else:
            print("wrong input.")
    else:
        LastOrigin = origin
        LastUnicode = str(origin.encode("unicode-escape"))
        LastCUnicode = str(origin.encode("unicode-escape"))[2:].replace("\'","").replace("\\\\","\\")
        print("Origin: " + LastOrigin)
        print("Unicode: " + LastUnicode)
        print("Unicode(CHANGED): " + LastCUnicode, end = "\n\n")