# pyRBAbu04

- Python 3.6m
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