from flask import Blueprint
from flask import render_template,render_template_string,jsonify,request
import numpy as np
import pickle

#defining blueprint object
bp=Blueprint("predict",__name__)



def pretrainedModel():
    
    model=pickle.load(open('/home/dreams/Projects/Projects/webScraping/IntroductionMachineLearning/webIntegration/ufoExample/ufo-model.pkl','rb'))
    return model
    

@bp.route('/predict',methods=['POST'])
def predict():
    #defining list comprehension
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]

    #defining pre-trained model
    model=pretrainedModel()
    #predicting result
    prediction=model.predict(final_features)

    output=prediction[0]
    countries=['Australia','Canada','Germany','UK','US']



    return render_template(
        'index.html',prediction_text="Likely country: {}".format(countries[output])
        )
    
    