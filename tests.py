import unittest
from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertKelvinToCelsius
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToFahrenheit

class ConversionsTestCase(unittest.TestCase):
    def test_C_to_K(self):
        """Will 300.00C be properly converted to 573.15K?"""
        self.assertEqual(convertCelsiusToKelvin(300.00), 573.15)  # add assertion here
        self.assertEqual(convertCelsiusToKelvin(0.00), 273.15)
        self.assertEqual(convertCelsiusToKelvin(100.00), 373.15)
        self.assertEqual(convertCelsiusToKelvin(-273.15), 0.00)
        self.assertEqual(convertCelsiusToKelvin(20.00), 293.15)


    def test_C_to_F(self):
        """Will 300.00C be properly converted to 572.00F?"""
        self.assertEqual(convertCelsiusToFahrenheit(300.00),572.00)  # add assertion here
        self.assertEqual(convertCelsiusToFahrenheit(0.00), 32.00)
        self.assertEqual(convertCelsiusToFahrenheit(100.00), 212.00)
        self.assertEqual(convertCelsiusToFahrenheit(20.00), 68.00)
        self.assertEqual(convertCelsiusToFahrenheit(-17.78), 0.00)



    def test_K_to_C(self):
        self.assertEqual(convertKelvinToCelsius(573.15), 300.00)
        self.assertEqual(convertKelvinToCelsius(273.15), 0.00)
        self.assertEqual(convertKelvinToCelsius(373.15), 100.00)
        self.assertEqual(convertKelvinToCelsius(0.00), -273.15)
        self.assertEqual(convertKelvinToCelsius(293.15), 20)



    def test_F_to_C(self):
        self.assertEqual(convertFahrenheitToCelsius(572.00), 300.00)
        self.assertEqual(convertFahrenheitToCelsius(32.00), 0.00)
        self.assertEqual(convertFahrenheitToCelsius(212.00), 100.00)
        self.assertEqual(convertFahrenheitToCelsius(0.00), -17.78)
        self.assertEqual(convertFahrenheitToCelsius(68.00), 20.00)



    def test_F_to_K(self):
        self.assertEqual(convertFahrenheitToKelvin(572.00), 573.15)
        self.assertEqual(convertFahrenheitToKelvin(32.00), 273.15)
        self.assertEqual(convertFahrenheitToKelvin(212.00), 373.15)
        self.assertEqual(convertFahrenheitToKelvin(-459.67), 0)
        self.assertEqual(convertFahrenheitToKelvin(0), 255.37)
    def test_K_to_F(self):
        self.assertEqual(convertKelvinToFahrenheit(573.15), 572.00)
        self.assertEqual(convertKelvinToFahrenheit(273.15), 32.00)
        self.assertEqual(convertKelvinToFahrenheit(373.15), 212.00)
        self.assertEqual(convertKelvinToFahrenheit(0), -459.67)
        self.assertEqual(convertKelvinToFahrenheit(255.37), 0)



if __name__ == '__main__':
    unittest.main()
