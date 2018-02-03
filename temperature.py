#Demo for a function
#Temperature converter

"""A module for converting temperature from Celsius to Fahrenheit and vice versa."""


def main():
    temp = int(input("Temperature: "))
    scale = input("Scale [C][F]: ")
    if(scale.lower() == 'f' or scale.lower() == 'c'):
        if(scale.lower() == 'c'):
            print("CELSIUS: ", temp, " degree Celsius")
            print("FAHRENHEIT: ", convert_fahrenheit(temp), " degree Fahrenheit")
        else:
            print("CELSIUS: ", convert_celsius(temp), " degree Celsius")
            print("FAHRENHEIT: ", temp, " degree Fahrenheit")
    else:
        print("The scale is invalid.")
#DOCSTRING

def convert_celsius(temperature):
    """Converts the value of the 'temperature'
variable into Celsius. It returns the Celsius value."""
    celsius = (5/9)*(temperature - 32)
    return celsius

def convert_fahrenheit(temperature):
    """Converts the value of the 'temperature'
variable into Fahrenheit. It returns the Fahrenheit value."""
    fahrenheit = (9/5) * temperature + 32
    return fahrenheit

#Not recommended
#main()

#Recommended
if __name__ == "__main__":
    main()






    
