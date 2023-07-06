def primary():
    
    
        x = int(input("please enter a number : "))
        for i in range(1,x):
            if x%i==0:
                return False
            else:
                return True
            

print(primary())