NX

Setup

File > Preferences > User Interface
Theme > Type > Dark
Resource Bar (Bar on Left)
Roles
Content: Role Advanced
Presentation: 4k
Right click, select "Constraints Navigator"
Select everything else too
Go to each top bar menu (Curve, Surface, Assembly, etc)
Select carrots and show all options. 

To view/hide all things: ctrl + W
Part Navigator

Children: blue
Parents: pink
Turn on persistent relations if you want to make the relation permanent!

Convert parts from mm to in: ug_convert_part -mm C:\Users\kiz\Documents\082933_01.prt

Color - Right click on body > Assign feature color

Update "Associativity manager" - but use with caution!

Constrains: None, use as needed.

Sketching: Hide

Order of sketches/features: chronological (feature groups mess this up)

Color: Assign color in 201 file.

Check in/out: Checked in means someone else can edit. Tree cannot be collapsed to check in/out.

Released: Done working on it.

Changes: Make new file number. Some people wont look at release number.

Duplicate parts (for fasteners) Assemblies > Move Component

Select component: select whole bolt.
Motion: dynamic
Check "Move Handles only"
Mode: Copy
Specific Orientation: click on "Point Dialog" click on mating surface (mating radius) click "OK"
Uncheck "Move handles only"
Select desired point for new fastener ()
Click apply
Suppression: Suppression > select layout file. (will keep part suppressed when you open layout file).

Render issues: View > Fit

Prefer Sequential Timestamp Order customer default, which will automatically rearrange features to preserve that order (File tab→Utilities→Customer Defaults→Modeling→Feature Group→Prefer Sequential Timestamp Order).



Start building up a folder to work in

Drag folder from search results to your folder
Teamcenter

Folder in home menu:
Just for organizing work
Create new folder: file, new, folder (don’t enter a name first, just next) then enter name - might show up in Newstuff folder first
Search:

Search for items - use * at end to search for everything with the proceeding numbers
Icons:

Flag (checkered black) - Production release
Flag (checked yellow) - Development release (no review needed)


File types

Don’t worry too much about all different file types.

Import ones are "production part" and "Production part revision" with "UGMASTER" in it!

Production Part: For release
Name convention: XXXXXXX-000/XX
-000: Layout file -
-0XX: Part file - single part with many bodies
-2XX: Assembly file - for many parts
Reference Part: Not for release
Name convention: XXXXXXX
Usually first two are 00
COTS Part: Common Off The Shelf
 from suppliers like McMaster
"Triple zero" structure

Use Wave link geometry:
In layout file in Assembly navigator
Select part as work object
Insert > Associate Copy > Wave Geometry Linker
Select body from drop down
Select the body (not in menu, in main window)
Wave links will not update in part files if geometry is updated in layout file.

Release process (if someone else will be making)

Assign "Commodity (Material Group)" field in all pointers  (Need to checkout to modify)
Check in everything (check all drop downs) If releasing layout. Everything in layout needs to be released.
Select all files to be released (select all pointers only)
Start release workflow
File > new > workflow process
Development release process > OK
Complete release workflow
Right side bar > My worklist > open carrot > tasks to perform > Viewer tab > perform > False for no reviewers > OK
Select item under task to perform > Complete > apply
Impact analysis

To find higher level models and see how parts relate to overall structure.

Search for known part number.
"Impact analysis" tab ??
All lower levels can be found by looking up these high level assembly part number in either TC or NX