from evdev import InputDevice, categorize, ecodes
import pdb
from statsd import StatsClient

c = StatsClient(host=GRAPHITE_URL, port=8126, prefix=None)

dev = InputDevice('/dev/input/event0')

for event in dev.read_loop():
  if event.type == ecodes.EV_KEY:
    if event.value == 01:
      c.incr('keystroke', count=1, rate=1)


