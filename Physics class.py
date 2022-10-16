
import os

# Option menu Function
def choose_programm():
    print("Welcome to The Physics Calculator v1.0")
    print("")
    print("Options to Choose")
    print("Temp C")
    print("Temp F")
    print("Newton")
    print("Joules")
    print("Bomb")
    print("")
    user_input_choose_program = input("Type in your choice:")

    # Fahrenheit to Celsius
    if user_input_choose_program == "Temp C":
        print("")
        print("Temperature Calculator - Fahrenheit to Celsius")
        print("")

        # Fahrenheit input
        fahrenheit_input = input("Type Temperature in Fahrenheit:")

        # Fahrenheit to Celsius Function
        def f_to_c(f_temp):
            temp_celsius = (f_temp - 32) * 5/9
            return(temp_celsius)

        f_in_celsius = f_to_c(float(fahrenheit_input))
        print("Your temperature in Celsius:", f_in_celsius)
        print("")

        #///Return Menu///
        print("Want to Return to Menu?")
        choose_return = input("Y/N: ")
        if choose_return == "Y":
            os.system('cls')
            choose_programm()
        else:
            print("Have a nice Day.")

    # Celsius to Fahrenheit Function
    elif user_input_choose_program == "Temp F":
        print("")
        print("Temperature Calculator - Celsius to Fahrenheit")
        print("")

        # Celsius Input
        celsius_input = input("Type Temperature in Celsius:")

        # Celsius to Fahrenheit Function
        def c_to_f(c_temp):
            temp_fahrenheit = c_temp * (9/5) + 32
            return temp_fahrenheit
        
        c_in_fahrenheit = c_to_f(float(celsius_input))
        print("Your Temperature in Fahrenheit:", c_in_fahrenheit)
        print("")

        #///Return Menu///
        print("Want to Return to Menu?")
        choose_return = input("Y/N: ")
        if choose_return == "Y":
            os.system('cls')
            choose_programm()
        else:
            print("Have a nice Day.")

    # Newton Calculator
    elif user_input_choose_program == "Newton":
        print("")
        print("Newton Calculator")
        print("")

        newton_mass_input = input("Type in Mass:")
        newton_acc_input = input("Type in Acceleration:")
        print("")

        # Newton Function
        def get_force(mass, acceleration):
            return mass * acceleration

        newton_force = get_force(float(newton_mass_input), float(newton_acc_input))
        
        print("Your Newton force:", newton_force)

        #///Return Menu///
        print("Want to Return to Menu?")
        choose_return = input("Y/N: ")
        if choose_return == "Y":
            os.system('cls')
            choose_programm()
        else:
            print("Have a nice Day.")

    # Joules Calculator
    elif user_input_choose_program == "Joules":
        print("")
        print("Joules over Distance")
        print("")

        joules_mass_input = input("Type in Mass:")
        joules_acc_input = input("Type in Acceleration:")
        joules_dis_input = input("Type in Distance in meters:")
        print("")

        #Joules Function
        def get_joules(mass, acceleration, distance):
            return (mass * acceleration) * distance
        
        joules_over_distance = get_joules(float(joules_mass_input), float(joules_acc_input), float(joules_dis_input))
        
        print("")
        print("Your Joules over Distance:", joules_over_distance)
        print("")

        #///Return Menu///
        print("Want to Return to Menu?")
        choose_return = input("Y/N: ")
        if choose_return == "Y":
            os.system('cls')
            choose_programm()
        else:
            print("Have a nice Day.")

    # Bomb Calculator
    elif user_input_choose_program == "Bomb":
        print("")
        print("Bomb to Joules")
        print("")

        bomb_mass_input = input("Type in Mass(KG) of the Bomb:")

        def get_bomb_energy(mass):
            c = 3*10**8
            return mass*c

        bomb_energy = get_bomb_energy(float(bomb_mass_input))
        print("")
        print("A", bomb_mass_input, "kg bomb supplies", bomb_energy, "Joules.")
        print("")
        
        #///Return Menu///
        print("Want to Return to Menu?")
        choose_return = input("Y/N: ")
        if choose_return == "Y":
            os.system('cls')
            choose_programm()
        else:
            print("Have a nice Day.")

    # Invalid command
    else:
        print("Invalid Input.")
        choose_programm()
choose_programm()