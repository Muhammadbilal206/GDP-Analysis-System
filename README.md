# GDP-Analysis-System
To design and implement a data-driven GDP analysis system using functional programming principles in Python, while enforcing the Single Responsibility Principle (SRP) and introducing configuration-based behavior.


Added data.csv file to load data from and to test the project.
Added data_loader.py file
Added data_processor.py file
Added dashboard.py file
Added config.json file

CONFIGURATION>JSON CHANGES:

- Modified config.json file and added configuration settings.


DATA_LOADER.PY CHANGES:
- Added the json loader function.
- Added the csv loader function to load the data from .csv file



DATA_PROCESSOR.PY CHANGES:
- Added function to preocess data according to the configuration file
- Added function to get filtyered data for plotting in charts


DASHBOARD.PY CHANGES:
- Added the plotting function for bar chart
- Added the plotting function for line chart
- Added execution function for the main as well
