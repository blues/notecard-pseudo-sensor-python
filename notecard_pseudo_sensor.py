import notecard
from periphery import I2C
import random

class NotecardPseudoSensor:
  def __init__(self):
    port = I2C("/dev/i2c-1")
    self.card = notecard.OpenI2C(port, 0, 0)

  # Read the temperature from the Notecard’s temperature
  # sensor. The Notecard captures a new temperature sample every
  # five minutes.
  def temp(self):
    temp_req = {"req": "card.temp"}
    temp_rsp = self.card.Transaction(temp_req)
    return temp_rsp["value"]

  # Generate a random humidity that’s close to an average
  # indoor humidity reading.
  def humidity(self):
    return round(random.uniform(45, 50), 4)
