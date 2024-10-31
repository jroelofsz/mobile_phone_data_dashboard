from flask import Flask, render_template, jsonify
import psycopg2
import pandas as pd
import plotly.express as px
import plotly 
import plotly.utils 
import json


#Connect to the database
conn_string = "host='localhost' dbname='phone_usage_db' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)

print("Database opened successfully")
cursor = conn.cursor();
query = 'select * from phone_user_behavior'
cursor.execute(query)

colnames = [desc[0] for desc in cursor.description]
phone_df = pd.DataFrame(cursor.fetchall(), columns=colnames)

cursor.close()
print('Database closed successfully!')

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def hello_world():
    ############
    ## Average Battery Drain Chart
    ############
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
    
    battery_drain_graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    ###########
    ## OS Type per Age Group Chart
    ###########
    os_types_df = phone_df.copy()
    bins = [18, 25, 35, 50]
    labels = ["18-25", "25-35", "35-50"]
    os_types_df['age_groups'] = pd.cut(os_types_df['age'], bins, labels=labels)

    grouped_os_types_df = os_types_df.groupby(['age_groups', 'operating_system'])['user_id'].count().to_frame('user_count')

    # Rename columns in place without assignment
    grouped_os_types_df.index.set_names(['Age Groups', 'Operating System'], inplace=True)

    fig = px.bar(
        grouped_os_types_df.reset_index(),  # Temporarily reset index for plotting
        x='Age Groups',
        y='user_count',
        color='Operating System',
        barmode='group',
        labels={'user_count': 'Number of Users', 'age_groups': 'Age Groups'}
    )
    
    os_type_graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template(
        'index.html', 
        battery_drain_graph_json=battery_drain_graph_json, 
        os_type_graph_json=os_type_graph_json
    )
    

    

@app.route('/api_docs')
def api_docs():
    return render_template('api_docs.html')

@app.route('/api/v1/all')
def all():
    api_all_data_df = phone_df.copy()

    json_data = api_all_data_df.to_json(orient='records')
    
    return jsonify(json.loads(json_data))

@app.route('/api/v1/<start_age>/<end_age>')
def ageReturn(start_age, end_age):
    #convert input to int
    start_age = int(start_age)
    end_age = int(end_age)
    
    #copy dataframe
    age_data_df = phone_df.copy()
    
    #filter dataframe to return results between and including the start and end age
    age_filtered_df = age_data_df[(age_data_df['age'] >= start_age) & (age_data_df['age'] <= end_age)]
    
    #convert to JSON
    json_data = age_filtered_df.to_json(orient='records')
    
    #return to APi
    return jsonify(json.loads(json_data))

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    

