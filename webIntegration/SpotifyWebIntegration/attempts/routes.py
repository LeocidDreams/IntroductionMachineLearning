from flask import Blueprint,render_template,jsonify,request
from typing import List
import numpy as np
# import ipynb
# # from ipynb.fs.full import dataAnalysis
# from ipynb.fs.defs.dataAnalysis import dataEncoding
# import ipynb.fs

# from .full.dataAnalysis import dataEncoding
# from .defs.dataAnalysis import dataEncoding

# from .defs.dataAnalysis import c

# #defining blueprint object
bp=Blueprint('routes',__name__)        
    

@bp.route('/routes',methods=['GET','POST'])
def routes():
    
    #Defining example serilization object
    abc={
        "age":12,
        "country":'US',
        "subscription-type":'Free',
        "listening-time":123,
    }

    if request.method=='POST':
        country=request.form.get('country')
        subscriptionType=request.form.get('subscription-type')
        listeningTime=int(request.form.get('listening-time'))
        age=int(request.form.get('age'))

        # predict=prediction(request.form.values())
        # key,value=prediction(request.form.values())
        # formElement=prediction(request.form.values())
        intFeature=prediction(request.form)

        # return "initFeatures:{}\n".format(next(predict))
        # return "key_subscription:\t{}\nvalue_subscription:{}".format(key,value)
        # return "form_elements:\t{}".format(next(formElement))
        return "intFeature:\t{}".format(intFeature)

        # return """
        #         {}:{}
        #         """.format(prediction(),request.form.values())



        
    else:
        return "{request.method}"

from ipynb.fs.full.dataAnalysis import dataEncoding
# print(type(dataEncoding()))

countries={
    'canada':'CA',
    'germany':'DE',
    'australia':'AU',
    'united states':'US',
    'united kingdom':'UK',
    'india':'IN',
    'france':'FR',
    'pakistan':'PK',

}

# defining predicting function
def prediction(formValues):
    '''
    Docstring for prediction
    Args:
        formValues:including all required elements
    Return:
        Gender[str]
    '''
    import pickle
    model_filename="/home/dreams/Projects/webScraping/IntroductionMachineLearning/webIntegration/SpotifyWebIntegration/spotify_model.pkl"
    model=pickle.load(open(model_filename,'rb'))
    #############################################
    #############################################
    
    import pandas as pd
    path="/home/dreams/Projects/webScraping/IntroductionMachineLearning/dataset/spotifyDataset/spotify_churn_dataset.csv"

    # ##reading dataset
    dataset=pd.read_csv(path)
    
    # Countries encoding
    keyCountries=dataset['country'].unique()
    valueCountries=dataEncoding()['Country'].unique()

    #Subscription type encoding
    keySubscription=dataset['subscription_type'].unique()
    valueSubscription=dataEncoding()['subscriptionType'].unique()
    # return keyCountries,valueCountries

    # return formValues

    # #defining intFeatures
    # intFeatures=np.array([])
    # #defining filter
    # filter_=None

    intFeatures=np.array([])
    #traversing int form elements 
    for name in ['listening-time','age']:
        intFeatures=np.append(intFeatures,int(formValues[name]))
    finalFeatures=np.array([])
    finalFeatures=np.append(finalFeatures)

    # appending str form elements
    for name in ['country','subscription-type']:
        finalFeatures=np.append(finalFeatures,formValues[name])

    prediction=model.predict(finalFeatures)
    output=prediction[0]

    return output

    

