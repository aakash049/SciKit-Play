# SciKit-Play

A python based program which uses Scikit-learn (Python's machine learning library), PIL to detect and win32api to play a candy crush game on its own.

The aim of this project is to illustrate "Supervised" machine learning.
## Steps to run:
 1. Just run `Scikit-Play-GUI.py` to run the Graphical User Interface.
 2. Click on "START Your Game!" button.
 3. Click on "CLICK to get the coordinates" button, it will cause an external application to run named "Wheres my cursor".
 4. Hover your mouse on the upper left and bottom right corners of the board and note down their respective coordinates.
 5. Enter those coordinates in the GUI itself.
 6. Click on "SciKit-Play". Congrats you are a GOD now!

 ## The following steps take place under the hood:

 1. Take a screenshot of the desktop
 2. Extract the game-board from it, using the coordinates given by the user. If the game-board is not found, then the game has ended or there is some error.
 3. Divide the game-board in cells and extract each cell
 4. Using a classification algorithm determine what candy is in which cell
 5. Store this information in a 2-d array
 6. Compute the best move using a greedy-like algorithm
 7. Wait for the board to stabilize and all the movement to stop
 8. Go to 1


NOTE : This branch contains the training data for the board Recognizer, which is an experimental addition to the project