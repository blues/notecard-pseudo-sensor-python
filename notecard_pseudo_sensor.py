import board
import busio
import notecard
import random
import sys

use_circuitpython = sys.implementation.name == 'circuitpython'

def NotecardExceptionInfo(exception):
    name = exception.__class__.__name__
    return sys.platform + ": " + name \
        + ": " + ' '.join(map(str, exception.args))

class NotecardPseudoSensor:
  def __init__(self):

    if use_circuitpython:
        try:
            port = busio.I2C(board.SCL, board.SDA)
        except Exception as exception:
            raise Exception("error opening port: "
                            + NotecardExceptionInfo(exception))

        try:
            self.card = notecard.OpenI2C(port, 0, 0, debug=True)
        except Exception as exception:
            raise Exception("error opening notecard: "
                            + NotecardExceptionInfo(exception))
    
    else:
        from periphery import I2C
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
