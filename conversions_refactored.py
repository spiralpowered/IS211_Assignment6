class ConversionNotPossible(Exception):
    pass
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    return round((celsius * 1.8) + 32, 2)

def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15


def convertFahrenheitToCelsius(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 2)


def convertFahrenheitToKelvin(fahrenheit):
    return round((fahrenheit + 459.67) / 1.8, 2)


def convertKelvinToFahrenheit(kelvin):
    return round((kelvin * 1.8) - 459.67, 2)


def mile_to_yard(miles):
    return miles * 1760


def yard_to_mile(yards):
    return yards / 1760


def yard_to_meter(yards):
    return round(yards * 0.9144, 2)


def meter_to_yard(meters):
    return round(meters / 0.9144, 2)


def meter_to_mile(meters):
    return round(meters / 1609.34, 5)


def mile_to_meter(miles):
    return round(miles * 1609.34, 3)

def convert(fromUnit, toUnit, value):
    conversion_map = {
        'CelsiusKelvin': convertCelsiusToKelvin,
        'CelsiusFahrenheit': convertCelsiusToFahrenheit,
        'KelvinCelsius': convertKelvinToCelsius,
        'KelvinFahrenheit': convertKelvinToFahrenheit,
        'FahrenheitCelsius': convertFahrenheitToCelsius,
        'FahrenheitKelvin': convertFahrenheitToKelvin,
        'MilesYards': mile_to_yard,
        'MilesMeters': mile_to_meter,
        'YardsMiles': yard_to_mile,
        'YardsMeters': yard_to_meter,
        'MetersMiles': meter_to_mile,
        'MetersYards': meter_to_yard
    }
    conversion = str(fromUnit) + str(toUnit)
    if conversion in conversion_map:
        units = conversion_map[conversion]
        return float(units(value))
    else:
        raise ConversionNotPossible("Invalid or Incompatible units were entered.")


if __name__ == '__main__':
    nl = '\n'
    u1 = input(f"Choose one of the available units{nl}(Celsius, Kelvin, Fahrenheit, Miles, Yards, Meters): ")
    while True:
        value = input("Enter the value of the chosen unit: ")
        if value.isnumeric() is True:
            value = float(value)
            break
        else:
            print("Invalid value entered.")
    u2 = input("Which unit do you want to convert to? ")
    print(convert(u1, u2, value))
