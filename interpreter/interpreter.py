x ,y ,z = input("Expression: ").split()
match y:
    case "+":
        print("result is: ",float(int(x) + int(z)))
    case"-":
        print("result is: ",float(int(x) - int(z)))
    case "*":
        print("result is: ",float(int(x) * int(z)))
    case "/":
        if(int(z) == 0):
            print("the division is impossible")
        else:
            print("result is: ",float(int(x)/ int(z)))

