# Lab 01 - Snakes Cafe

**Author**: Tony Regalado
**Version**: 1.0.0

## Collaborations and Credit

* Help from TA Anthony Beaver
* [References](https://www.programiz.com/python-programming/methods/string/lower)
* [References](https://www.programiz.com/python-programming/methods/string/capitalize)

## Overview

CLI with the functionality of a POS restaurant system using Python.

### Feature Tasks & Requirements

* [x] When run, the program should print an intro message and the menu for the restaurant
* [x] The restaurant's menu should include appetizers, entrees, desserts, and beverages
* [x] The program should prompt the user for an order
* [x] When a user enters an item, the program should print an acknowledgement of their input
* [x] The program should tell the user how to exit
* [x] The program's content should match included sample exactly
  * [x] Actually, there's one tiny spot that should be different - see if you can spot it.
  * [x] The ```>``` character represents user input line and should be printed out with a trailing space

### Stretch Goals

* [x] Print out a summary of complete order
* [x] Only allow ordering items on the menu
* [ ] Allow ordering items not on menu but give custom reply

## Getting Started

Inside your terminal, navigate to the correct folder and run the following commands:

* ```poetry new snakes-cafe```
* ```cd snakes-cafe```
* ```poetry add black```
* ```touch snakes_cafe/snakes_cafe.py```
* ```mv README.rst README.md```
* ```git init```
* ```git add .```
* ```git commit -m "first commit"```

GitHub: create an empty repository called: ```snakes-cafe```

* Initialize without license, README or gitignore.
* Copy the "Quick Setup" on the following Github page.
* Paste in your terminal

## Change Log

06/14/2021:

* 1st commit
  * Lab started
  * initial commit

06/16/2021:

* 2nd Commit
  * added welcome & order print functions.
  * added menu list
  * added prompt for items that are not on the menu
  * added prompts for user when user types "quit"
  * added logic and functionality for the users order.
  * finished lab.

[PR for this lab submission](https://github.com/Edward-Regalado/snakes-cafe)

[Python Submission Instructions Link](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)