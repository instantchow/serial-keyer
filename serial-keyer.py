#!/usr/bin/env python3

import serial
import time
from pynput.keyboard import Controller, Key

# ===== CONFIGURATION =====
SERIAL_PORT = '/dev/tty.usbserial-ABCD1234'  # Serial port name
BAUD_RATE = 9600                          # Baud rate
CTS_KEY = 'z'                             # Key to press when CTS is high
DSR_KEY = 'x'                             # Key to press when DSR is high

# For left Control:
#CTS_KEY = Key.ctrl_l
# For right Control:
#CTS_KEY = Key.ctrl_r

POLL_INTERVAL = 0.01                      # Polling interval in seconds (10ms)
# =========================


# Initialize keyboard controller
keyboard = Controller()

# Open the serial port
port = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)

# Set RTS and DTR
port.rts = True
port.dtr = True

print("Monitoring CTS and DSR... Press Ctrl+C to exit")

# Track previous state to detect changes
previous_cts = port.cts
previous_dsr = port.dsr

try:
    while True:
        current_cts = port.cts
        current_dsr = port.dsr
        
        # CTS monitoring
        # Detect rising edge (False -> True transition)
        if current_cts and not previous_cts:
            print(f"CTS went HIGH - Holding '{CTS_KEY}' down")
            keyboard.press(CTS_KEY)
        
        # Detect falling edge (True -> False transition)
        elif not current_cts and previous_cts:
            print(f"CTS went LOW - Releasing '{CTS_KEY}'")
            keyboard.release(CTS_KEY)
        
        # DSR monitoring
        # Detect rising edge (False -> True transition)
        if current_dsr and not previous_dsr:
            print(f"DSR went HIGH - Holding '{DSR_KEY}' down")
            keyboard.press(DSR_KEY)
        
        # Detect falling edge (True -> False transition)
        elif not current_dsr and previous_dsr:
            print(f"DSR went LOW - Releasing '{DSR_KEY}'")
            keyboard.release(DSR_KEY)
        
        previous_cts = current_cts
        previous_dsr = current_dsr
        
        # Small delay to avoid excessive CPU usage
        time.sleep(POLL_INTERVAL)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    port.close()
    print("Serial port closed")
