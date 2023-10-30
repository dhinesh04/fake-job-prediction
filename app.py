from flask import Flask, request, render_template

app=Flask(__name__)

import pickle
import numpy as np
model = pickle.load(open('job.pkl', 'rb'))

@app.route('/input', methods=['GET','POST'])
def input():
    msg=""
    if request.method=="POST":
        details=request.form
        title = details['title']
        benefits = details['benefits']
        company_profile = details['company_profile']
        description = details['description']
        requirements = details['requirements']
        text = str(title)+str(benefits)+str(company_profile)+str(description)+str(requirements)
        predict=model.predict([[text]])
        predict = [1]
        if predict[0]==1:
            msg="Job seems fake. Be aware!"

        elif predict[0]==0:
            msg="Job seems legitimate. Give it a try!!"
        
    return render_template('output.html',msg=msg)

@app.route('/')
def main():
    return render_template('home.html')
    return render_template('input.html')

@app.route('/predict')
def predict():
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)