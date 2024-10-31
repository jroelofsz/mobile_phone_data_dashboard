from flask import Flask, render_template, send_file
import psycopg2
import pandas as pd
import plotly.express as px
import scipy.stats as st
import plotly 
import plotly.utils 
import json
import numpy as np


#Connect to the database
conn_string = "host='localhost' dbname='phone_usage_db' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)

print("Database opened successfully")
cursor = conn.cursor();
query = 'select * from phone_user_behavior'
cursor.execute(query)

colnames = [desc[0] for desc in cursor.description]
phone_df = pd.DataFrame(cursor.fetchall(), columns=colnames)


# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def hello_world():
    #render phone battery chart
    phone_df_battery = phone_df.copy()
    bins = [18, 25, 35, 50]
    labels = ["18-25", "25-35", "35-50"]
    phone_df_battery['age_groups'] = pd.cut(phone_df_battery['age'], bins, labels=labels)

    # Calculating mean battery drain for each age group
    mean_battery_age = phone_df_battery.groupby(["age_groups"])["battery_drain_mah_per_day"].mean()
    mean_battery_age_df = pd.DataFrame({"age_groups": mean_battery_age.index, "average_battery_drain": mean_battery_age.values})

    # Creating a bar chart using Plotly
    fig = px.bar(
        mean_battery_age_df,
        x="age_groups",
        y="average_battery_drain",
        #title="Average Battery Drain Per Age Group",
        labels={"age_groups": "Age Groups", "average_battery_drain": "Battery Drain (mah/day)"},
        text_auto=True
    )

    # Customizing the figure's appearance
    fig.update_layout(
        #xaxis_title="Age Groups",
        yaxis_title="Battery Drain (mah/day)",
        yaxis_range=[0, mean_battery_age.max() + 500],
        template="plotly_white"
    )
    
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', graph_json=graph_json)
    

    

@app.route('/api_docs')
def api_docs():
    return render_template('api_docs.html')

@app.route('/api/v1/all')
def all():
    return 'Will contain JSON of all records.'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
