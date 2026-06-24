
# Write a Python script that converts a temperature in degrees
# celcius to the corresponding temperature in degrees fahrenheit
# 𝑇f = 𝑇c×1.8 + 32

def celcius_to_fahrenheit(temperature_celcius: float) -> float:
    return (temperature_celcius * 1.8) + 32


if __name__ == "__main__":
    print(celcius_to_fahrenheit(0))
    print(celcius_to_fahrenheit(10))
    print(celcius_to_fahrenheit(25))