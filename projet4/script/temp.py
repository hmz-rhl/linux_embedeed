from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature_from_pressure()

print(round(temp,2))

