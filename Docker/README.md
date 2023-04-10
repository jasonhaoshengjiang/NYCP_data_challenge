#Docker 

##About this directory:
This directory contains the Docker and Python files required to build the Docker image. And instructions to pull and run the image on Docker Desktop. 

## Build the Docker image:
```shell
$ docker build -t data-challenge . 
```
## Run the Docker image (starts the container)
```shell
$ docker run -t -i data-challenge:
```
Inputs can be chose from: <br> {agency: ['DSNY', 'NYPD', 'EDC', 'DHS', 'DOT', 'DPR', 'DOHMH', 'DCA', 'TLC',
       'DEP', 'HPD', 'DOB'] <br> complaint_type:['APPLIANCE', 'DOOR/WINDOW', 'ELECTRIC', 'FLOORING/STAIRS',
       'GENERAL', 'HEAT/HOT WATER', 'PAINT/PLASTER', 'PLUMBING',
       'UNSANITARY CONDITION', 'ELEVATOR', 'WATER LEAK', 'SAFETY',
       'OUTSIDE BUILDING']}

#Run image and access files in container via Docker Desktop:
-> Open Docker Desktop 
-> Ctrl+K 
  -> Type in: jasonhaoshengjiang 
    -> look for: jasonhaoshengjiang/data-challenge
      ->Actions
        ->Run 
          -> Optional Settings: Environment Variables -> Enter Inputs 
-> Containers
  -> Index column: Image 
    -> jasonhaoshengjiang/data-challenge -> Actions: Start 
      -> files 
        -> data 
All files required from Task 1 - 4 can be found and downloaded from this folder 
