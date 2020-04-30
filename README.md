# Calculator GUI
# Created by Gavin Uhran

## Instructions of Use
### Download the 'calculatorGUI.py' and run the file using Python3
Buttons on the calculator serve the purpose of the typical 4-function calculator. Enter an equation using the built-in buttons, then press '=' to calculate the equation. 

## Most recent update: April 29, 2020
### Added Executable (.exe) File!
Calculator GUI no longer requires a Python3 path on your device to run the program! Using the Python library 'pyinstaller', Calculator GUI now has an executable (.exe) file. This means that any modern Windows OS user will be able to use Calculator GUI by running the executable file on their desktop! Enjoy the new ease of access!

### Updates to GUI
The calculator has an updated look! Changes in background and font color of the 'operation' buttons gives Calculator GUI a sleek design! The changes in colors are designed to help a user identify the buttons they seek in less time.

### Patched Errors with Negative Numbers
Reported errors from negative numbers revealed that the calculator's functionality to handle inputs containing negative numbers was not complete. This update contains a patch that allows users to receive the correct response when inputting negative numbers into their equation.

## Previous Updates
### April 28, 2020
#### Added Order of Operations (PMDAS)
The calculator now calculates properly! Isn't that great? This update gave the calculator the functionality of differentiating between different operations, prioritizing in the following order: parenthesis, multiplication, division, addition, and lastly, subtraction. This is a huge milestone, because it is very important that a user is given an output that matches the typical order of operations they would expect from a 4-function calculator!

#### Limitless Parenthesis
The calculator now has the ability to read inside an endless amount of parenthesis, so long as they are all matched with closing parenthesis. A user can now enclose parts of their equation, or even the whole equation, in as many parenthesis as they wish and the calculator will strip all the parenthesis away to reach the contents inside, then calculate from there. 

((((7*3)+8))+9) will now equal 38, which it would not have before.

#### Error Messages
While hopefully a user will never encounter any error messages, an error message will now be displayed to the user if their input is improper. This a helpful for the user because it allows them to correct any issues with their input after clearing the display. This functionality also serves as prevention from letting any improper input crash the calculator.

### April 25, 2020
#### Using recursion and string manipulation, the '=' button now has functionality!
When pressed, the '=' button will take the user's equation and display an answer!

#### Flawed functionality
The implementation of the '=' button's functionality is still under development. While the parenthesis do currently hold the highest order of operations, no further order of operations (following PEMDAS) has been implemented. This will be the goal of the next update. Additionally, the method of calculating a response does not throw any error messages to the user. This has been recognized and will also be a major goal in future updates.

#### Improvements to the Square Root Button
The square root button now throws an error messages when appropriate! This was fixed by checking that operation was only being performed on integers and floats.
