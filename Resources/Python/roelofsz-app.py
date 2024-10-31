from flask import Flask, render_template, send_file
import psycopg2
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import io

#configure matplotlib
matplotlib.use('Agg')

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
    plot_battery_graph()
    return render_template('index.html')

def plot_battery_graph():
    phone_df_battery = phone_df.copy()
    
    bins = [18,25,35,50]
    labels = ["18-25","25-35","35-50"]
    phone_df_battery['age_groups'] = pd.cut(phone_df_battery['age'], bins, labels=labels)
    
    mean_battery_age = phone_df_battery.groupby(["age_groups"])["battery_drain_mah_per_day"].mean()
    
    #Bar chart for Average Battery Drain vs. Age 
    mean_battery_age_df = pd.DataFrame({"average_battery_drain": mean_battery_age})
    reset_df_battery = mean_battery_age_df.reset_index()
    reset_df_battery["average_battery_drain"].astype(int)
    x_axis = np.arange(len(mean_battery_age))
    plt.figure(figsize=(10, 6))
    plt.bar(x_axis, reset_df_battery["average_battery_drain"], color ='blue', alpha=0.5, align="center")
    plt.xlim(-0.75,len(x_axis)-0.25)
    plt.ylim(0,max(mean_battery_age)+500)
    tick_locations = [value for value in x_axis]
    plt.xticks(tick_locations, reset_df_battery["age_groups"])
    plt.title("Average Battery Drain Per Age Group")
    plt.xlabel("Age Groups")
    plt.ylabel("Battery Drain (mah/day)") 
    
    plt.savefig('static/images/battery_drain_graph.png')
    plt.close()
    

    

@app.route('/api_docs')
def api_docs():
    return render_template('api_docs.html')

@app.route('/api/v1/all')
def all():
    return 'Will contain JSON of all records.'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
