# SCPI

- Standard Commands for Programmale Instruments.
- Syntax for communication with devices.
- Superset which includes IEEE commands as well.

Device: Power supply, wave form, laser, etc
Connection interface: LAN, USB, GPIB, etc. 
Syntax: SCPI + IEEE (standard ASCII message construction)
Communication layer: VISA, TCP

### Resorces
0. See device specific programming guide.
1. Connection interface: https://lxistandard.org/Documents/Articles/HiSLIP%20for%20Fast%20Remote%20Control%20of%20LXI%20Instruments_final.pdf

## Direct Socket
Communication without VISA.

#### Pros
1. No other installs.

#### Cons
2. Requires LAN interface.

### Lanugage Depdendencies

#### Python
1. socket

### Resources
1. python + socket: https://www.keysight.com/zz/en/assets/7018-06563/white-papers/5992-3827.pdf

## VISA
- Virtual Instrument Software Architecture. 
- API for communication with instruments. 
- Provides standardization of operations. 

#### Pros
1. Flexibility at connection interfact: LAN, USB, GPIB, ect.

#### Cons
1. Requires installations on host. 

### Host dependencies
1. IVI Shared Components: provided by IVI foundation.
2. VISA Shared components: provided by vendor.

#### KeySight
Keysight provides all-in-one I/O library which bundles all required host installs.

#### NI VISA
National Instruments provides NI VISA library which similarly bundles all host installs.

#### pyvisa-py
Alternate python visa backend. Does not seem as reliable.

### Language dependencies

#### Python
1. pyvisa
2. pyvisa-py (if trying to use pure python backend).
3. zeroconf + psutil (seems to be necessary for LAN interface)
