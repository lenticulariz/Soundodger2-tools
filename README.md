**For the files to work you will also need to download writeIn.txt and SDformat.py, put them all in the same folder.**

# Soundplotter
This file transfers a set of coordinates into a bullet with a specific location on soundodger 2

It works via "drawing a line" from the center to your coordinates, 
-For distance it finds the length of that line.
-For angle it takes the arctan of the x and y position.


Also moderate knowledge of python is required to use, you input the points that you want to plot in the FunctionToSD.py script, (something like: arena_to_coord(500, 500, 1).
Then when ran the script will output the xml data into writeIn.txt, where you can then paste it into the level's xml

startOffset is the time that it spawns the bullet
0, 0 is the center of the screen

# DomePatternCreator
This file creates domes in a specific pattern for you \
The shapes include: \
-circle \
-square \
-pendulum \
-parametric equation (preset) \
-parametric equation animation (preset)

When running the file it will output the xml lines into writeIn.txt, which you can then paste into your xml file
