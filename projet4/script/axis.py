from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(True, False, False)  # enable only the compass
north = sense.get_compass()
print(north)
m_x, m_y, m_z = sense.get_compass_raw().values()
