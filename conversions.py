
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2)

def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15

def convertFahrenheitToCelsius(fahrenheit):
    return round((fahrenheit-32)/1.8, 2)

def convertFahrenheitToKelvin(fahrenheit):
    return round((fahrenheit + 459.67)/1.8, 2)

def convertKelvinToFahrenheit(kelvin):
    return round((kelvin * 1.8) - 459.67, 2)
