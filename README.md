# Chart Rendering Web Application

This project is a web-based application that visualizes data using interactive charts powered by Plotly. 

## Features

- **Average Battery Drain per Age Group**: Visualizes the average battery consumption for different age groups.
- **Operating System Popularity per Age Group**: Displays the distribution of users by age group and operating system.


## Technologies Used

- **Python (Flask)**: Backend framework for handling requests and passing data to the template.
- **Pandas**: Used for data processing and manipulation.
- **Plotly**: Generates interactive charts for data visualization.
- **HTML, CSS, JavaScript**: For the frontend structure and behavior.
- **psycopg2**: Used for connecting to the database and loading data into the application


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jroelofsz/mobile_phone_data_dashboard.git
   ```
2. Create a PostgreSQL database in your pgAdmin tool.
3. Run the ```Resources/SQL/Phone_User_Behavior.sql``` in your database to create the table.
4. Import the ```Resources/CSVs/user_behavior_dataset.csv``` into the table that was just created (phone_user_behavior).
5. Update connection string in the ```app.py``` file to use the correct credentials. The following will have to be updated depending on your settings:
    - host
    - dbname
    - user
    - password
6. Once complete with the steps above. You can run the ```app.py``` file in your environment with the following dependencies installed:
    - Python
    - Flask
    - Pandas
    - Plotly
    - psycopg2
