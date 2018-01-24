#Using regular operations
'''fahrenheit=int(input('enter the value'))
fahrenheit_to_celcius_temp=(fahrenheit-32)/1.8

print(fahrenheit_to_celcius_temp)

celcius=int(input('enter the value'))
celcius_to_fahrenheit=((celcius*1.8)+32)
print(celcius_to_fahrenheit)'''

#Using functions
def fahrenheit_to_celcius_temp(fValue):
    celcius = (fValue-32)/1.8
    return celcius

def celcius_to_fahrenheit(cValue):
    fahrenheit = (cValue*1.8)+32
    return fahrenheit

reason = input("What you want to convert")
temp = int(input("Enter the temp"))

if reason == 'celcius to fahrenheit':
    c = celcius_to_fahrenheit(temp)
    print(c)
else:
    f = fahrenheit_to_celcius_temp(temp)
    print(f)


