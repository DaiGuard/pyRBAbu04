# pyRBAbu04

this library is Dual channel 12 bit ADC + DAC converter for Raspberry Pi to controller by python library.

[2 チャンネル 12ビット アナログ-デジタル変換器/DAC Raspberry Pi Zero用](https://www.robotshop.com/jp/ja/2-channel-12-bit-analog-to-digital-converter-dac-raspberry-pi-zero.html)

![RB-Abu-04](https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/2/-/2-channel-12-bit-analog-to-digital-converter-dac-raspberry-pi-zero.jpg)

- Python 3.9
- Raspberry Pi 4

## Installation

```bash
pip install git+https://github.com/DaiGuard/pyRBAbu04.git
```

## Example

```python
import pyRBAbu04
import time

# device open
pyRBAbu04.open()

# output full voltage
pyRBAbu04.open(0, 1.0)
time.sleep(5)

# output zero voltage
pyRBAbu04.open(0, 0.0)
time.sleep(5)

# output half voltage
pyRBAbu04.open(0, 0.5)
time.sleep(5)

# output zero voltage
pyRBAbu04.open(0, 0.0)
time.sleep(5)

# device close
pyRBAbu04.clse()
```