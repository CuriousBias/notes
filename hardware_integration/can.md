# CAN
Controller Area Network
- Communication bus on vehicles.
- Look at schematics for pin outs. 

## Hardware

### Connector
- Connect via DB9 connector
    1. Pin 7 - CAN_P or CAN_H - positive (high)
    2. Pin 2 - CAN_N or CAN_L - negative (low)

### Dongles
- Red/gray band: CAN
- Yellow band: LIN

### Terminator
- Second 120 Ohms resister on other end of the CAN bus (end with DBC connector)
- The first 120 Ohms resistor is on other end. 
- Both resistors work to drop voltage to 0 quickly, but not too much resistance to drive to 5V. 

## Signal

### CAN signal
- 5V bus as example
- 0 (on bus): Difference of 5V
    - CAN low: -2.5V
    - CAN high +2.5V
- 1 (on bus): 
    - Wires to go 0V
