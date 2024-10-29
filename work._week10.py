# Group memebers: Abel Sanchez, Lorenzo Gasca, Diego Padilla 
  
    #Question 17 Bank loan approval
income = int(input("what is your income per month: "))
credit = int(input("what is your credit score: " ))
if credit >= 600:
    if credit >= 700 and income > 3000 :
        print("approved for high loan")
    elif income >=2000 and income <=3000:
        print("Approved for medium loan")
    if credit == 600 or credit <=699:
        if income > 3000:
            print("approved for medium loan")
        if income < 3000:
            print("approved for low loan")
else:
    print("Loan not approved")

    #Question 16 Gym Membership Access

premium = input("Do you have premium yes or no: ").lower()
class_a = input("Are you attending a class Y or N: ").lower() 
if premium == "yes":
    if class_a == "y":
        print("Free access to class included.")
    if class_a == "n":
        print("Access to all facilities.")
if premium == "no":
    if class_a == "y":
        print("Class fee applies to basic members.")    
    if class_a == "n":
        print("Access to gym facilities only.")

    
    