from flask import Flask,request,jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
app=Flask(__name__)
CORS(app)

@app.route("/result",methods=["POST","GET"])

def result():

    if request.method == "POST":
        # Your existing code for handling POST requests goes here
        Board = request.form.get('Board')
        total_marks = request.form.get("total_marks")

        if Board and total_marks:
            file = "D:/login_nodejs/views/database.csv"
            df = pd.read_csv(file)
            df = df.drop(["S No"], axis=1)
            maths_mean = df['Maths'].mean() 
            science_mean = df['Science'].mean()
            sst_mean = df['Social Science'].mean()
            english_mean = df['English'].mean()
            lsm_mean = df['Language Subject Marks'].mean()
            osm_mean = df['Optional Subject Marks'].mean()


            maths_std = df['Maths'].std()
            science_std = df['Science'].std()
            sst_std = df['Social Science'].std()
            english_std = df['English'].std()
            lsm_std = df['Language Subject Marks'].std()
            osm_std = df['Optional Subject Marks'].std()


            calculation = lambda row: (((row['Maths']-maths_mean)/maths_std)*50)+75


            # Add a new column to the DataFrame with the calculated values
            df['Maths'] = df.apply(calculation, axis=1)

            calculation = lambda row: (((row['Science']-science_mean)/science_std)*50)+75


            # Add a new column to the DataFrame with the calculated values
            df['Science'] = df.apply(calculation, axis=1)

            calculation = lambda row: (((row['Social Science']-sst_mean)/sst_std)*50)+75

            # Add a new column to the DataFrame with the calculated values
            df['Social Science'] = df.apply(calculation, axis=1)

            calculation = lambda row: (((row['English']-english_mean)/english_std)*50)+75

            # Add a new column to the DataFrame with the calculated values
            df['English'] = df.apply(calculation, axis=1)

            calculation = lambda row: (((row['Language Subject Marks']-lsm_mean)/lsm_std)*50)+75


            # Add a new column to the DataFrame with the calculated values
            df['Language Subject Marks'] = df.apply(calculation, axis=1)

            calculation = lambda row: (((row['Optional Subject Marks']-osm_mean)/osm_std)*50)+75


            # Add a new column to the DataFrame with the calculated values
            df['Optional Subject Marks'] = df.apply(calculation, axis=1)
            boards = pd.Categorical(df['Board'].unique())
            sum_dict = {}
            for i in boards:
                part_df = df[df['Board'] == i]
                sum = 0
                sum += part_df['Maths'].sum()
                sum += part_df['Science'].sum()
                sum += part_df['English'].sum()
                sum += part_df['Social Science'].sum()
                sum += part_df['Language Subject Marks'].sum()
                sum += part_df['Optional Subject Marks'].sum()
                sum_dict[i] = sum / (part_df.shape[0])
            dev_dict = {}
            df['Total'] = df['English'] + df['Maths'] + df['Science'] + df['Social Science'] + df['Language Subject Marks'] + df['Optional Subject Marks']
            for i in boards:
                part_df = df[df['Board'] == i]
                var = 0
                for index, row in part_df.iterrows():
                    var += (row['Total'] - sum_dict[row['Board']]) ** 2
                dev_dict[i] = (var / len(part_df)) ** 0.5
                dev_dict
            deviation = dev_dict[Board]
            mean = sum_dict[Board]

            z1 = (int(total_marks) - mean) / deviation
            standard = (z1 * 100) + 500
            return jsonify({"Data": standard})
        else:
            return jsonify({'error': 'Missing required parameters'})

    elif request.method == "GET":
        # Your code for handling GET requests goes here
        return jsonify({"message": "Hello from the GET method!"})

if __name__ == '__main__':
    app.run(debug=True, port=2000)