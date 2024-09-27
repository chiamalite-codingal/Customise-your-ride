print("choose your ride:")
choice = int(input("Enter 1.car 2.bike"))
if choice == 1:
    carchoice = int(input("1. BMW 2.AUDI"))
    if carchoice == 1:
        print("we book ride with BMW")
    else:
        print("we book ride with AUDI") 
elif choice == 2:  
    bikechoice = int(input("1. HONDA 2.SCOOTER"))
    if bikechoice == 1:
        print("we book ride with HONDA") 
    else:  
        print("we book ride with SCOOTER")      
else:  
    print("Invalid")     