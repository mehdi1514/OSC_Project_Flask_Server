from flask import Flask, render_template, request
import astar
from predict_disease import predict_heart_disease
app = Flask(__name__)

@app.route('/')
def hello_world():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    
    end1 = (13, 15)
    path1 = astar.astar(maze, start, end1)

    end2 = (2, 8)
    path2 = astar.astar(maze, start, end2)

    end3 = (6, 7)
    path3 = astar.astar(maze, start, end3)
    nearest_hospital = (0,0)
    nearest_length = 0
    if len(path1) < len(path2):
        if len(path1) < len(path3):
            nearest_hospital = end1
            nearest_length = len(path1)
        else:
            nearest_hospital = end3
            nearest_length = len(path3)
    else:
        if len(path2) < len(path3):
            nearest_hospital = end2
            nearest_length = len(path2)
        else:
            nearest_hospital = end3
            nearest_length = len(path3)
    return render_template('index.html', maze=maze, start=start, end1=end1, path1=path1, end2=end2, path2=path2, end3=end3, path3=path3, nearest_hospital=nearest_hospital, nearest_length=nearest_length)

@app.route('/direction')
def direction():
    return render_template("direction.html")

@app.route('/hospitals')
def hospitals():
    return render_template("hospitals.html")

@app.route('/predict', methods=['GET'])
def predict():
    """
    * age: The person's age in years
    * sex: The person's sex (1 = male, 0 = female)
    * chest pain: (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
    * blood pressure: The person's resting blood pressure (mm Hg on admission to the hospital)
    * cholestrol: The person's cholesterol measurement in mg/dl
    * thalach: The person's maximum heart rate achieved
    """
    #input_data = {'age': [63], 'gender': [1], 'chest pain': [3], 'blood pressure': [145], 
    # 'cholestrol level': [233], 'max heart rate': [150]}
    #input_data = {'age': [62], 'gender': [0], 'chest pain': [2], 'blood pressure': 
    # [130], 'cholestrol level': [263], 'max heart rate': [97]}
    age = request.args.get('age')
    gender = request.args.get('gender')
    chest_pain = request.args.get('chest_pain')
    bp = request.args.get('bp')
    chol = request.args.get('chol')
    mhr = request.args.get('mhr')
    input_data = {'age': [age], 'gender': [gender], 'chest pain': [chest_pain], 'blood pressure': [bp], 'cholestrol level': [chol], 'max heart rate': [mhr]}
    output = predict_heart_disease('/Users/muntazir/Desktop/colg/ai/model/', input_data)
    return render_template("result.html", result=output[0])

if __name__ == "__main__":
    app.run(debug=True)