#Demo program for selection structure
#Remember to have same indentation for each substructures!

temperature = int(input('Enter the temperature you want to convert: '))
scale = input('Scale of the temperature [c-Celsius] [f-Fahrenheit]: ')

if scale.lower() == 'c':
    fahrenheit = ((9/5)*temperature+32)
    if fahrenheit > 50:
        print("Wow, that is too hot!")
    elif fahrenheit > 25 and fahrenheit <=50:
        print("Still too hot.")
    else:
        print("Nice temperature!")
    print("The Fahrenheit equivalence is " + str(fahrenheit))
elif scale.lower() == 'f':
        celsius = ((5/9)*(temperature-32))
        if celsius > 50:
              print("Wow, that is too hot!")
        elif celsius > 25 and celsius <=50:
            print("Still too hot.")
        else:
            print("Nice temperature!")
        print("The Celsius equivalence is " + str(celsius))

else:
    print("That is not a valid choice.")

          
          
        
