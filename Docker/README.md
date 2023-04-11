# Docker 

## About this directory:
This directory contains the Docker and Python files required to build the Docker image. And instructions to pull and run the image on Docker Desktop. 

## Build the Docker image:
```shell
$ docker build -t data-challenge . 
```
## Run the Docker image (starts the container)
```shell
$ docker run -t -i jasonhaoshengjiang/data-challenge
```
Inputs can be chose from:
---
<br> agency : ['DSNY', 'NYPD', 'EDC', 'DHS', 'DOT', 'DPR', 'DOHMH', 'DCA', 'TLC',
       'DEP', 'HPD', 'DOB'] 

<br> complaint_type : ['APPLIANCE', 'DOOR/WINDOW', 'ELECTRIC', 'FLOORING/STAIRS',
       'GENERAL', 'HEAT/HOT WATER', 'PAINT/PLASTER', 'PLUMBING',
       'UNSANITARY CONDITION', 'ELEVATOR', 'WATER LEAK', 'SAFETY',
       'OUTSIDE BUILDING']

# Results:
Tables and visualizations are located in the 'data' folder within the 'Container' section of Docker Desktop, or through the equivalent shell command.

