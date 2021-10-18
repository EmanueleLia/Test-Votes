# Test-Votes Tool
Welcome to Test-Votes tool, this is one of my first application that runs on Python pl. The main goals of this application are:
1. Collect the names of a class;
2. Collect the relative grades;
3. Generate a Json file that contains the name of the course and the average grade of the course;
4. Generate a Json file that contains the names of the course (as keys) and the correspondent grades (as values);
5. Search one name from the Json file and return the grade.

The entire tool was splitted in two main py files:
* The votiesameJson.py tool;
* The searchfromlibrary.py tool;

## votiesameJson.py
This tool is able to get all the inputs (Names and Grades) and save two Json files:
* mediacorso.Json file - This file collects the name of the course and the average grade;
* namelist.json - This file collects the Names and the correspondent grades with the rule key-value.

The user is also able to see what value has inserted in input.

## searchfromlibrary.py
This tool is able to get the namelist.json file in input and allow the user to execute research in it. Searching by Name it�ll be returned the grade.
This tool also allow to see the Keys and the Values of the namelist.json file.

