# Current transducer
Take RMS of current and voltage to get power

## Hardware connection
- NI 920x voltage input

## NIMax
- Task
    - New task > Acquire signal > Analog input
- Configure
    - 1 channel per signal

## Scaling
For LES 6-NP
- Voltage output 1.875 - 3.125 = -6 - 6 amps
- 2.5 V = 0 A
- (V out max/ Ip Max) * V output + (V output @ 0) = Current
    - For LTS 15 np:
        - (5V/48 Ip)* V_out + 2.5 V = I
        - I = 9.6*V -24
    - For LES 6np
        - 5V/18I + 2.5 = I
        - I = 3.6*V_out + 9

## Wiring
- White: output signal to 9201 channel 
- Red: 5V supply
- Black: 0V ground

## Considerations
1. Force and movement to actuate switch