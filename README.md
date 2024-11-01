# Mobile Device Usage Dashboard

This project is a web-based application that visualizes data through interactive charts powered by Plotly. We designed it with app developers in mind, aiming to empower them to gain a deeper understanding of the market before committing to the development of an app, product, or hardware.

We offer two distinct methods for accessing this data:

1. Pre-generated Charts: Users can view the data through five different pre-generated chart perspectives.

2. API Access: Users can utilize our API to retrieve the data independently and conduct their own analyses.

## Features

- **Custom API**: Allows users to retrieve the entire dataset used in the visualizations, as well as specify a start age and end age to gather all matching records, allowing a more extensive and thorough analysis.
- **Interactive Dropdown**: Allows user to select which type of chart they would like to visualize, we then serve this chart back.


## Technologies Used

- **Python (Flask)**: Backend framework for handling requests and passing data to the template.
- **Pandas**: Used for data processing and manipulation.
- **Plotly**: Generates interactive charts for data visualization.
- **HTML, CSS, JavaScript**: For the frontend structure and behavior.
- **psycopg2**: Used for connecting to the database and loading data into the application

## Considerations
This project utilizes a dataset from Kaggle to drive its visualizations. You can reference the original dataset and its authors [here](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset).

Please note that this dataset does not contain any personal or identifying information about the users included. However, if you plan to replicate this project, please consider any applicable laws and regulations surrounding the use of the data you will be utilizing.
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

## References
The original creator of this dataset is [vala khorasani](https://www.kaggle.com/valakhorasani).

You can reference their work at [https://www.kaggle.com/valakhorasani](https://www.kaggle.com/valakhorasani)
