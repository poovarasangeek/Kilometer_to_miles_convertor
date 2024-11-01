conversion_factor=0.621371
while True:
    k_m=float(input("Enter the distance in KiloMeters:\n"))
    def miles_convertor(k_m):
        if k_m==0:
            print("Please enter the distance correctly")
        else:
            print(k_m,"km is equal to",k_m*conversion_factor,"Miles")
    miles_convertor(k_m)        
    ui=input("Do you want to continue? yes/no\n")    
    if ui.lower()=="yes":
        pass
    else:
        break