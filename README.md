# serial-keyer
RS232 serial port interface to morse code keyer, or any switch, simulates key down/up using DSR and CTS lines.

This code came about as a cheapskate way to get a morse keyer (cw morse code) input into a computer without buying an adapter for $20. I had a pile of cheap, USB to RS232 adapters waiting to be thrown out, but hey, now they are useful again! 

The code sets RTS high. All you need to do is "switch" RTS to the CTS and/or DSR pins to simulate keydown/keyup events. Common combinations include z and x for iambic paddle input, space bar, left and right ctrl key. Just set the mapping to your desired key and DSR or CTS lines.

Wire your CW key such that the pins close and open the connection between (RTS and DSR), (RTS and CTS). 

## On a standard RS232 DB9 connector
```
RTS = PIN 7
DSR = PIN 6
CTS = PIN 8
```
## Where to use?
Here are some of my favorite morse code training tools that have a "transmit" tool.

- https://morse.halb.it/
- https://lcwo.net/transmit
- https://didahdit.com/

