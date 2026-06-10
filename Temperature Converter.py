print("Temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice=int(input("Enter your choice(1 or 2):"))
if choice==1:
    Celsius=float(input("Enter temperature in Celsius:"))
    Fahrenheit=(Celsius*9/5)+32
    print("Temperature in Fahrenheit is:",Fahrenheit)
elif choice==2:
    Fahrenheit=float(input("Enter temperature in Fahrenheit:"))
    Celsius=(Fahrenheit-32)*5/9
    print("Temperature in Celsius is:",Celsius)
else:
    print("Invalid choice!")
