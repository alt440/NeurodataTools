# NeurodataTools
Some libraries from the Neurodata event that I got to know and experience.

Note: I used Pycharm to code this. I learned a simple way to add libraries to your projects using Pycharm:
Go to File > Settings > Project Interpreter. Click on the + icon that you see
from this view. Search for the library you want to add. If you do not find it,
then you need to use virtual environment to put it in the venv folder of your
project.

# MGC
This library can find relationships between some variables. It can find correlations that are not so easy to find, like relations that are spiral. Using MGC-X, you can also establish relationships from functions using time series (displacing functions by starting them sooner or later on the X-axis so that the functions can become most similar)
See more at https://neurodata.io/mgc/. (Slides + Docs) Go to Install section to install.

I had an issue when I tried integrating MGC. It complained about a certain file named Python.h. What I had to do was this command:
sudo apt-get install libpython3.7-dev

(Change 3.7 to your version of Python)

# SPORF
This library classifies data. It creates some forests. Not only can it divide data using straight lines, but it can also divide it diagonally.
See more at https://neurodata.io/sporf/. (Slides + Docs) Go to Install section to install.

I had an issue when I tried integrating SPORF. It complained about a certain file that was part of the Eigen3 package. I had to install it with this command:
sudo apt-get install libeigen3-dev

# GraSPy
This library estimates the probability of finding a new node in a certain area, as well as the probability a certain node connects a node type A to a node type B.
See more at https://neurodata.io/graspy/. (Slides + Docs) Go to Install section to install.

# reg
I also was made aware of this library, although it has not been included in the projects I did. This library finds relevant points in an image, so that you can distort it and find a way to backtrack your work to return to the original image. I believe it was mentioned that you cannot backtrack if two points go onto the same coordinate. Every time you start distorting the image, there is some form of data structure that will record the movements that were made for each pixel as a vector (direction and length), so that you can backtrack step by step to the original image. New features are being added. See more at https://neurodata.io/reg/. (Slides + Docs) Go to Install section to install.

# ndmg
Also known as nutmeg. This tool allows you to create a 3D image from multiple images from different angles. See more at https://neurodata.io/ndmg/. (Slides + Docs) Go to Install section to install.

For more information on these libraries, go to neurodata.io.
