celcius = float(input('Enter Celsius temperature: '))
fahrenheit = (celcius * 1.8) + 32
print('→ Fahrenheit temperature is', fahrenheit)
kelvin = (celcius + 273.15)
print('→ Kelvin temperature is', kelvin)

# reverse case
fahrenheit = float(input('Enter Fahrenheit temperature: '))
celsius = (fahrenheit - 32) / 1.8
print('→ Celcius temperature is', celsius)