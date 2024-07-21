Simulation

Under simulation file view

. I1 = idealized file Idealization simplifies geometry: anything in this file does not go back to 000 file. Great for removing features if you don’t want them in simulation.
Fem: put all mesh, material properties, thickness
Sim: put on constrains and run sim
Simulation File View (to navigate between files

Applications  > Pre/Post > Simulation navigator
go to different file types by double clicking on them
Modal analysis

New simulation

Pre/post > New FEM/Sim > Add revision letter > Ok
Check "Create idealized part"
Double click revision on sim to match
Setup solution

Pick desired name
Solver: Simcenter Nastran
Analysis type: Structural
2D solid option: None
Solution Type: SOL 103 Real Eigenvalues
Ok
In Idealized file (i1, i2, i3, etc)

Simulation Navigator > Simulation File View
Double click on idealized file.
Promote bodies. Select the ones you want > Ok
Resource bar > Part Navigator (to see all promoted bodies.
Hide all parts and show promoted bodies.
Thin plate method

For bodies you want to extend both directions:

Geometry Preparation > Create mid surface pairs
Select bodies
Auto create face pairs (icon with 2 yellow/orange) curved layers.
For bodies you want to extend only one

Geometry Preparation > More > offset surface
Select "Single Face" from selection drop down.
Extend edge so it touches
Geometry Preparation > More > Extend Sheet
Select Edges
Select Face
Trim portions
Insert plane: More > Datum plane
Select faces
Select boundary (the plane you created)
In FEM file (fem1, fem2, etc)

Hide all bodies before getting started. (Ctrl + w)
Create 2D mesh

Initial 2D mesh
Home > 2D Mesh
Set 2D Mesh options
Type: CQUAD4
Make sure destination collector is the same > unselect automatic creation
Ok
Make mesh more visible
2D collectors> thin shell > right click 2d mesh > edit display > shaded edge color > set color to white.
Do mesh mating:
Stitch edge > manual > edge to face > select edge and face > apply
Update (in upper left)
If mesh error:
Play around with tolerances
Create new mesh collector to apply thicknesses

One collector for each thickness
Create Mesh collector if Meshes are not already organized
Mesh collector > 2D, thin shell, Pshell, and name something useful
Drop mesh into collector
Drag and drop mesh into Base / support
Definite collector thicknesses
Next to pshell click edit wrench.
Input default thickness
View thicknesses
Right click on collector > edit display > select > element thickness and offset
Create mass representation

Nodes and elements > Element Create
Element family: 0D
Type: CONM2
Click on option window and enter mass, Ok
Nodes and Points, click point dialog and input coordinates
Node labels: anything useful
Change display
Change color
Add "Marker type" to actually see it.
Add Mass and inertia values
0D Mesh > Edit Mesh Associated Data > Select Mesh
RBE3

RBE2 vs 3:

Reality is somewhere in between. Try both and compare.
RBE3- distribute out weight, RBE2 - adds stiffness 
Home > 1D connection
Node to Node
Source and target
Source : mass
Target: select all anchors! (not just one)
Type: RBE3
Mesh Check

Duplicate elements:
Checks and information > Duplicate elements
SIM

Add constraints

Constraint type > User defined constraint
Select face
Select all fixed
Make sure fix is correct:
For bolts: pick nodes and fix mesh at bolt holes.
Solve

Solution > Solution
Definite solution
Name: Anything
Solver: Simcenter Nastran
Analysis type: Structural
Solution: 103 Real Eigenvalues
Create solution > Ok > Ok ? (just click through)
Step:
Create Step:
Eigenvalue method: Lanczos
 Click edit wrench next to Lanczos data field
Number of desired modes: 10
Solve > Ok
Solution > Solve
Finishes and Checks

Solid properties check
Checks and information > More > Solid properties check
Highlight everything: check total mass and confirm it matches expected
"Duplicate elements": any element that are coincidence and not connected.
"Duplicate notes": any notes on top of each other but not connected. 
Can select "Displayed" to do whole object!
Solid properties check": Make sure solid properties (mass, CM, etc) match expected.
Look at strain energy and kinetic energy to know where mass can be removed and where it should be added.

Daniel Rodriquez to learn about spring force comb.



Next level

Bolts (way to represent bolt as single point). 

RBE2 Bolt spiders
Insert RBE2 element at each modelled hole. 
1D Connection > Point to Edge > Select Arcs > Select collector
Bolt Node
Nodes and Elements > Translate > Copy and Translate > 5 or 10? mm in appropriate dimension > ok
Bolt CBUSH