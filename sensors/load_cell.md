# Load cell
- Button load cell experience

## Hardware connection
- NI 9237
- Pins (on RJ-50 cable)
    1. White - 2 (+ output)
    2. Green - 3 (- output)
    3. Red - 6 (+ excitation)
    4. Black -7 (- excitation)
- Side loading and moment considerations
    - Safe side-load 
        1. (5lbf - 1K lbf): 100% capacity
        2. (2K lbf - 10K lbf): 30% capacity
    - Safe, load axis moment
        1. (5lbf - 1K lbf): 100% capacity x 1 in
        2. (2K lbf - 10K lbf): 30% capacity x 1 in

## NIMax
- Task
    - New task > Acquire signal > Analog input > 
- Configure
    - 1 channel per load cell
    - Max and min based off scaled limits
    - Bridge: Full bridge
    - Vex source: Internal
    - Vex value: Excitation voltage 10 V (3.3 V really, but 10 V okay)
    - Bridge resistance: from data sheet ~ 350
    - Configure scale
        - Set electrical [mV/V] and physical [Pounds] first and second values from data sheet




