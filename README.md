# NotecardPseudoSensor

NotecardPseudoSensor provides an API interface to the internal sensors of the [Blues Wireless Notecard](https://shop.blues.io/collections/notecard). The goal of this abstraction is to offer a sensor to use with more advanced tutorials, which enables focus on basic Notecard transactions for those new to the platform.

## Installation

With `pip` via PyPi:

```
pip install notecard-pseudo-sensor
```

or

```
pip3 install notecard-pseudo-sensor
```


## Usage

``` python
import notecard
import notecard_pseudo_sensor

# How you connect to the Notecard varies based on your platform.
# See the note below.
from periphery import I2C
port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)

sensor = notecard_pseudo_sensor.NotecardPseudoSensor(card)
print(sensor.temp())
print(sensor.humidity())
```

> **NOTE**: The way you create the `port` and `card` differs based on platform. For details, check out the [`note-python` usage documentation](https://github.com/blues/note-python#usage), which contains [examples](https://github.com/blues/note-python/blob/main/examples).

## To learn more about Blues Wireless, the Notecard and Notehub, see:

- [blues.io](https://blues.io)
- [notehub.io](https://notehub.io)
- [dev.blues.io](https://dev.blues.io)

## License

Copyright (c) 2021 Blues, Inc. Released under the MIT license. See
[LICENSE](LICENSE.mit) for details.