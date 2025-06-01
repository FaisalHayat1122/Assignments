# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32  

print(TemperatureConverter.celsius_to_fahrenheit(25))  