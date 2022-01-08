# Loop Habit Tracker Data Analysis

---

## Overview

This project is designed to analyse the habit data that is outputted in a csv format from the android Loop Habit Tracker application. 

Application link - https://play.google.com/store/apps/details?id=org.isoron.uhabits&hl=en_GB&gl=US

Although the Loop Habit Tracker provides comprehensive in app infographics for each habit, it is difficult to see the completion rate against user defined thresholds for all the tracked habits together. This project was created to address this as well as provide insights that are not available in the application. 

The final output of this project is an xlsx file and a number of charts collectively showing key statistics for each of the habits against user specified thresholds.

This could help the user optimise their habit completion rates. 

Randomly generated habit data has been used for this project.

## Project Composition

---

The scripts below are described in the order in which they should be run.

Filename: Script - RandomHabitsDataGenerator.py

Description: Creates random habit data in the same output format as the Loop Habit app. Unfortunately, Loop Habit includes additional non-delimiter ‘,’ and other string information in the output csv file. This results in the data having to be cleaned and standardized to enable analysis.
Run order: 1 (or optional if the user has their own Loop Habit data).

Filename: Script - LoopHabitStandardize.py

Description: Standardises and cleans the outputted csv file from the user’s Loop Habit app (or the random habit data from the script above). This enables the data to be easily analysed at a later date. Habit values of 2 indicate the habit was completed whereas 0 indicate that the habit was not undertaken. 
Run order: 2 – Required

Filename: Script - Loop Habit Data Analysis.ipynb

Description: Analyses standardized Loop Habit data providing insight into habit completion rates based on user defined thresholds. An xlsx file and a number of charts are outputted collectively showing key statistics for the tracked habits.
Run order: 3 – Required

## Acknowledgment

---

Thank you to the developers of the Loop Habit Tracker for creating the application. 


## Licence

---

© Adam George
