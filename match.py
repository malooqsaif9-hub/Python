x = int(input("enter your number: "))
match x:
    
    case 0:
        print("x is zero ")
        
    case 1: 
        print("case is 1")
    
    case 4:
        print("case is 4")
    case _: # default case "note if any case matches then its below cases will not run "
        print(x)