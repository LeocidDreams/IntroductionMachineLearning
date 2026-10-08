from flask import Blueprint,render_template,jsonify,request
from typing import List
import numpy as np

bp=Blueprint('routes',__name__)

@bp.route('/routes',methods=['GET','POST'])
def routes():

    if request.method=='POST':
        # return "{}".format(request.method)
        # return "{}".format(isinstance(request.form.get('subscription-type'),str))
        predict=prediction(request.form)
        return """
                prediction:\t{}
                """.format(predict)
        

    else:
        return f"{'bcd'}"
    
# defining new json format

countries={
    "CANADA":('CA',),  
    "GERMANY":('DE',),
    "UNITED KINGDOMS":('UK',),
    "UNITED STATES":('US'),
    "AUSTRALIA":('AU'),
    "FRANCE":('FR'),
    "INDIA":('IN'),
    "PAKISTAN":('PK'),
}


# filter_=np.where(DF1['country']==curr)
# index_=DF1[filter_]
# print(ENCODED[index_])



def prediction(formElements):
    '''
    Docstring for prediction
    Args:
        formElements:including all required elements
    Return:
        Gender[str]
    '''

    # importing pickle serialization and deserialization purposes
    import pickle
    #calling current pre-trained model
    model_filename="/home/dreams/Projects/webScraping/IntroductionMachineLearning/webIntegration/SpotifyWebIntegration/spotify_model.pkl"
    model=pickle.load(open(model_filename,'rb'))
    # return dir(model)
    #calling dataset
    import pandas
    path="/home/dreams/Projects/webScraping/IntroductionMachineLearning/dataset/spotifyDataset/spotify_churn_dataset.csv"

    intFeatures=np.array([])

    #traversing int form elements
    for name in ['listening-time','age']:
        intFeatures=np.append(intFeatures,int(formElements[name]))
    
    finalFeatures=np.array([])
    finalFeatures=np.append(finalFeatures,intFeatures)

    #traversing string form elements
    for name in ['country','subscription-type']:
        # curr=formElements.get(name).strip('-').lower()
        curr=formElements.get(name)

        

        from dataAnalysis import creatingDataFrame,dataEncoding
        DF1,_=creatingDataFrame()
        ENCODED=dataEncoding()
        # print(DF1,ENCODED)

        
    
        

        
        if name=='country':
            # DF1['country'] #show  country columns
            # finalFeatures=np.append(finalFeatures,ENCODED[index_])
            # finalFeatures=np.append(finalFeatures,ENCODED.loc[name:index_])
            keys=DF1[name].unique() #np.array
            ENCODED=ENCODED[name].unique() #np.array #

            
            # index_=ENCODED[np.where(keys==curr)[0][0]]#?
            element=ENCODED[np.where(keys==curr)[0][0]]
            finalFeatures=np.append(finalFeatures,element)

            # return (keys)

            # yield (element,finalFeatures)


        # #     dfAge['subscriptionType']=LabelEncoder().fit_transform(dfAge['subscriptionType'])
        elif name=='subscription-type':
            #finding index by using np.where
            camelCase='subscriptionType'
            keys=DF1[camelCase].unique() #np.array
            ENCODED=ENCODED[camelCase].unique() #np.array #

            element=ENCODED[np.where(keys==curr)[0][0]]
            finalFeatures=np.append(finalFeatures,element)

            # return ({"camelCase":camelCase,"keys":keys,"ENCODED":ENCODED,"finalFeatures":finalFeatures,"numpy.where":np.where(keys==curr)[0]})
        #     # return 'abc'

        # else:
        #     return type(name)
        

    # finalFeatures=np.append(finalFeatures,curr)
        
    

    #predicting...
    prediction=model.predict(finalFeatures.reshape(1,-1))
    
    from dataAnalysis import dataEncoding,creatingDataFrame
    df1,_=creatingDataFrame()
    ENCODED=dataEncoding()

    
    gender='gender'
    keys=DF1[gender].unique()
    ENCODED=ENCODED[gender].unique()

    if prediction in ENCODED:
        index_=np.where(ENCODED==prediction)[0][0]
        return keys[index_]
    
    #return 'abc'
    #result
    # return 