newCalculation = True;
while newCalculation:
    
    while True:
        try:
            initialPosition = float(input("Enter initial position: "));
            initialVelocity = float(input("Enter initial velocity: "));
            acceleration = float(input("Enter acceleration: "));
        
            break;
        except ValueError:
            print("please enter a valid float");


    time = float(input("Enter time: "));
    while time < 0:
        print("please enter a number greater than or equal to 0");
        time = float(input("Enter time: "));


    print(initialPosition);
    print(initialVelocity);
    print(acceleration);


    calculation = initialPosition + initialVelocity * time + 0.5 * acceleration * time * time;
    print(calculation);

    again = input("If you want to play again type y: ");
    if again != "y":
        newCalculation = False
