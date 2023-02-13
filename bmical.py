def bmi_cal():
    """The body mass index is calculated by dividing an
    individual’s weight in kilograms by their height in meters, 
    then dividing the answer again by their height."""
    
    height=float(input("Enter your height in centimeters: "))
    weight=float(input("Enter your Weight in Kg: "))
    height = height/100
    bmi = weight / (height**2)
    print("Your body mass Index is : --> ", bmi)
    
    if bmi > 0:
        if bmi <= 16:
            print("You are severely underweight")
        elif bmi <= 18.5:
            print("You are underweight")
        elif bmi <= 25:
            print("You are Healthy")
        elif bmi <= 30:
            print("You are overweight")
        else:
            print("You are severly Overweight")
    else:
        print("Enter a valid details")
        
bmi_cal()
