# Group memebers: Abel Sanchez, Lorenzo Gasca, Diego Padilla 
  
    #Question 17 Bank loan approval
income = int(input("what is your income per month: ")) # ask user what their income per month is 
credit = int(input("what is your credit score: " )) # ask user what their credit score is
if credit >= 600: # if credit score is mmore than or equal to 600
    if credit >= 700 and income > 3000 :
        print("approved for high loan") # the output of a credit score more or equal to 700, and and income of less than 3000
    elif income >=2000 and income <=3000: 
        print("Approved for medium loan") # the output of a credit score more or equal to 700, and income is in between 2000 and 3000
    if credit == 600 or credit <=699:
        if income > 3000:
            print("approved for medium loan") # the output of a credit score in between 600 and 699, and and income of more than 3000
        if income < 3000:
            print("approved for low loan") # the output of a credit score in between 600 and 699, and and income of less than 3000
else:
    print("Loan not approved") # the output of having a credit score under 600

    #Question 16 Gym Membership Access

premium = input("Do you have premium yes or no: ").lower() # this finds out if the have premium or basic
class_a = input("Are you attending a class Y or N: ").lower() # this asks the user whether they are attending a class or not
if premium == "yes":                 #if the user types yes then it moves it to the next section
    if class_a == "y":               #if the user does attend classes it prints that a free class is included since he has premium
        print("Free access to class included.") #prints that a free class is included since he has premium
    if class_a == "n":                  #If the user doesn't attend the class than 
        print("Access to all facilities.") #it says we have access to all facilities  
if premium == "no":          #If the user types no it doesnt have premium
    if class_a == "y":       #The user goes to the classes
        print("Class fee applies to basic members.")    #prints that the user has to pay since he has basic membership
    if class_a == "n":                              #user doesnt go to classes
        print("Access to gym facilities only.")     #since he doesnt go to classes he only has access to the gym 

    
    