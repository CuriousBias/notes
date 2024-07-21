Document the process for executing a vibration test from the test design engineer perspective.  

Vibration Input Specifications

Start any test with the input profile specifications. Random is more demanding than sine.

Force limiting. Limits over testing of spacecraft. Force limiting limits input force into spacecraft. Similar to if accelerometers are placed at each mounting point (but then you have just created a load cell).
Notching: Notching is possible for device, but not a good idea for fixture below 100 Hz. Notching fixture stiffness to further decrease 1st mode will result in uncontrolled testing to different portions of the vehicle. Some will be undertested or some will be over tested. Or all will be over tested. Input to experienced frequency transfer function will no longer be 1:1. Notching fixture frequency will be necessary for random.
Test

QTP Sine

ATP Sine

QTP Random	ATP Random
Frequency range [Hz]

5 - 100 (standard)

5 - 100

20 - 300 (standard)	20 - 300
Maximum acceleration + margin

 Value (g) +  50% margin

Value (g) + 50% margin

Value (Grms) + margin (dB)	Value (Grms) + margin (dB)
Input graph (Freq vs Acceleration)	


Frequency vs G^2/Hz graph

Fixture Design

CAD Design

Fixture design is driven by test frequency range. Fixture first mode (fixture + device) should be 2x max frequency in range, but decreased to 1.5x to make vertical fixture feasible.

Modal Analysis

Compare mass and massless fixtures
Massless = maximum possible stiffness with design
Look at strain energy to see where material not being used and can be removed.
Kuiper bolt spreadsheet? Kuiper bolt calculator
Dynamoment stiffness - from technical data
Table Hardware Specifications

Shaker choice is driven by frequency range, maximum acceleration, total moving mass, overturning moment , and fixture footprint. 

Determine highest frequency of test.
Determine maximum G for sine, or Grms for random.
Calculate total moving mass (table + armature + bearings + fixture + device)
Calculate force rating: F = m*a
Determine peak to peak motion requirements (2 - 3 inches)
Calculate maximum overturning moment (sets the number and location of bearings required)
Calculated as simple moment (fixture + device mass) * distance (center of gravity to table)
Calculate yaw moments if applicable
Ideally fixture + device are centered on table. 
Pick table with 
Or should displacement vs frequency plot not limits above
Force rating, 
Fixture foot print
Peak to peak displacement
Armature frequency range (usually limited if big)
Design Process Log

Record progress in design log. Ideal it to document progress and communicate results. 

Background
Motivator for design
Fixture requirements
Orientation of device
Minimum resonance first mode.
Other hardware and hardware mounting requirements (ex: dynamometers).
Full Mass of system
Mounting and lifting requirements.
Fixture design
Fixture analysis
FEM design and features
Mesh, CBUSH, Connectors, etc. 
FEM results
First few modes with graphics (displacement)
1st mode elaboration (strain energy graphic)
Compare mass and massless fixtures
Fixture use
Physical movement and lifting
Crane capacity
Ceiling limits
Attachment process
Appendix
Material properties
Vehicle and fixture properties table (Mass, center of mass, volume requirements, overall length dimensions).