# Accelerometer

## Hardware connection
- Connect accelerometer with x, y, z cables.
- NI 9234: 4 channel SW selectable IEPE and AC/DC

## NIMax
- Task
    - New task > Acquire signal > Analog input > Acceleration > IEPE
    - Select 3 ports for x, y, z
- Configure
    - 3 channel, 1 for each axis
    - Min and max in [g]
    - Sensitivity from calibration data [mVolts/g]
