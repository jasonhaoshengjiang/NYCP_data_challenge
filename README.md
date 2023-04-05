# NYCP_data_challenge

## About this reporsitory: 

This repository consists entirely of Jupyter notebooks that can be run using the 'run all' command. The Python notebooks require two values to be input as command line arguments to complete the tasks. The SQL database was created on Amazon AWS RDS cloud, and the notebooks showcase the contents of the database. The process for creating the databases is captured and documented within the notebooks.

**Folders in this repository:** 
1. Python Notebook :
    This folder contains answers to the Task 1- 4.  
3. SQL Notepad :
    This folder contains answers to the Task 5 -6. 
6. data :
    This folder acts as target /data folder where stores all the files throughout the tasks. 

**One pull request:** 
1. After uploading the Python code for Task 1 - 4, I went back to proofread my work and found that there were multiple points for one ntacode. Since the Neighborhood Tabulation Area boundaries imply that these points should enclose an area, it would be more appropriate to perform a spatial join of the sample_311 location points inside these boundary lines in order to obtain the matching ntacode. Additional details and the process for doing so are included in the notebook.
2. As an associate data engineer, I believe it would be beneficial to discuss this issue with the team and potentially consider emailing the Office of Planning for further guidance.

**Suggested order:** 

1. [Python: Task 1-4](https://github.com/jasonhaoshengjiang/NYCP_data_challenge/blob/main/Python_Notebook/Task%201%20-%204.ipynb)

2. [Python: join_by_polygons](https://github.com/jasonhaoshengjiang/NYCP_data_challenge/blob/join_by_polygons/Python_Notebook/join_by_polygons.ipynb)

3. [SQL: Task 5-6](https://github.com/jasonhaoshengjiang/NYCP_data_challenge/blob/main/SQL%20Notepad/Task%205%20-%206.ipynb)



