# serial-keyer
RS232 serial port interface to morse code keyer, or any switch, simulates key down/up using DSR and CTS lines.

This code came about as a cheapskate way to get a morse keyer (cw morse code) input into a computer without buying an adapter. I had a pile of cheap, USB to RS232 adapters waiting to be thrown out, but hey, now they are useful again! 

The code initially sets RTS high to provide a common source of 8 or 12v+. All you need to do is "switch" RTS to the CTS and/or DSR pins to simulate keydown/keyup events. Common combinations include _z_ and _x_ for iambic paddle input, _space_bar_, left and right _ctrl_ keys. Just set the mapping to your desired key and DSR or CTS lines.

Wire your CW key such that the pins close and open the connection between (RTS and DSR), (RTS and CTS). 

## On a standard RS232 DB9 connector
```
RTS = PIN 7
DSR = PIN 6
CTS = PIN 8
```
### Wiring to Key
Wire the common to PIN 7 RTS, which will provide the +12 or +8 volts needed. Wire PIN 6 DSR to one of the paddles, Wire PIN 8 CTS to the other paddle. Order really doesn't matter since you can change the keyboard key mappings to wharever you need. If a single straight key, just pick DSR or CTS and leave the other PIN disconnected.

## Running
```
pip install -r requirements.txt
python3 ./serial-keyer.py
```
In your operating system, you're going to need to allow this application to take over HID control. In MacOS, you need to give your terminal program Accessability access. You should get a popup into System Settings and a switch control next to the terminal or iterm application or whatever shell you are running this under.


## Where To Use This Key Now?
Here are some of my favorite morse code training tools that have a "transmit" tool.

- https://morse.halb.it/
- https://lcwo.net/transmit
- https://didahdit.com/

