#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##importing numpy pandas
import pandas as pd
import numpy as np

def creatingDataFrame():

    ##current dataset abs path
    # path="/home/dreams/PycharmProjects/PycharmProjects/webScraping/IntroductionMachineLearning/dataset/spotifyDataset/spotify_churn_dataset.csv"
    #defining new path
    path="/home/dreams/Projects/webScraping/IntroductionMachineLearning/dataset/spotifyDataset/spotify_churn_dataset.csv"

    # ##reading dataset
    dataset=pd.read_csv(path)
    # print(dataset)
    ##creating dataframe
    dfAge=pd.DataFrame(data={
        "gender":dataset['gender'],
        "age":dataset['age'],
        'country':dataset['country'],
        "listeningTime":dataset['listening_time'],
        'subscriptionType':dataset['subscription_type'],                   
    })



    dfListen=pd.DataFrame({  
        'deviceType':dataset['device_type'],
        "listeningTime":dataset['listening_time'],
        "songsPlayedPerDay":dataset['songs_played_per_day'],
        'skipRate':dataset['skip_rate'],
        'adsListenedPerWeek':dataset['ads_listened_per_week'],
        'offlineListening':dataset['offline_listening'],
    })

    #looking up dataset columns
    return dfAge,dfListen

    # dfAge.dropna(inplace=True,ignore_index=True)
    # dfListen.dropna(inplace=True,ignore_index=True)

    # dfAge.info()
    # dfListen.info()



# In[ ]:


def datavisualization(dfAge,dfListen):

    ## it isn't correct

    import matplotlib.pyplot as plt
    import numpy  as np
    import pandas as pd

    # print(dfAge[dfAge['Gender']=='Male']['Age'])


    x1=dfAge[dfAge['gender']=='Male']['age']
    x2=dfAge[dfAge['gender']=='Female']['age']
    x3=dfAge[dfAge['gender']=='Other']['age']




    plt.figure()
    plt.hist([x1,x2,x3],stacked=True,color=['r','g','b'],bins=50)
    plt.legend(['Male','Female','Other'],loc='upper left')
    plt.show()


    # print(df)
dfAge,dfListen=creatingDataFrame()
# datavisualization(dfAge,dfListen)


# In[ ]:


def dataEncoding():
    ##creating model 
    from sklearn.preprocessing import LabelEncoder

    ##look up unnumeric data and encode unnumeric data
    #dfAge.info()
    dfAge['gender']=LabelEncoder().fit_transform(dfAge['gender'])
    dfAge['country']=LabelEncoder().fit_transform(dfAge['country'])
    dfAge['subscriptionType']=LabelEncoder().fit_transform(dfAge['subscriptionType'])
    # dfAge.to_csv("example.csv")

    return dfAge



def dataPreprocessing(dfAge,dfListen):

    dataEncoding()
    ##importing required libraries
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler,StandardScaler

    ##defining normalization objects
    scaler=StandardScaler()
    minMaxScaler=MinMaxScaler()# Sscale down all featuers to a same range.

    selectedFeatures=['age','country','listeningTime','subscriptionType']

    X=dfAge[selectedFeatures]
    y=dfAge['gender']

    #reshaping current dataset  to 2D array shape
    # nx,ny=X.shape
    # X=X.reshape((nx*ny))

    # print(X.shape)

    xTrain,xTest,yTrain,yTest=train_test_split(X,y,test_size=0.2,random_state=42)
    # normalization with MinMaxScaler
    xTrainMinMax = minMaxScaler.fit_transform(xTrain[selectedFeatures])
    xTestMinMax  = minMaxScaler.fit_transform(xTest[selectedFeatures])



    # print("X train min max scaler array shape",xTrainMinMax.shape)
    # print("X test min max scaler array shape",xTestMinMax.shape)
    # print(xTestMinMax)

    return xTrainMinMax,xTestMinMax,yTrain,yTest

#     return xTrainMinMax,xTestMinMax,yTrain,yTest
xTrainMinMax,xTestMinMax,yTrain,yTest=dataPreprocessing(dfAge,dfListen)
# print(xTrainMinMax,xTestMinMax,yTrain,yTest)


# In[ ]:


def creatingModel():
    from sklearn.pipeline import make_pipeline
    from sklearn.linear_model import SGDClassifier
    from sklearn.preprocessing import StandardScaler
    model=make_pipeline(
        StandardScaler(),
        SGDClassifier(
            loss='log_loss',
            penalty='l2',
            alpha=0.0001,
            learning_rate="optimal",

        )    
    )
    return model

# model=creatingModel()


# In[ ]:


def modelTrainingAndEvulation(model,xTrainMinMax,xTestMinMax,yTrain,yTest)->object:

    from sklearn.metrics import accuracy_score,classification_report
    ##fitting current model
    fitting=model.fit(xTrainMinMax,yTrain)
    print(fitting)
    # yield fitting
    #predictions
    predictions=model.predict(xTestMinMax)
    # yield predictions
    print(predictions)

    print(classification_report(yTest,predictions))
    print("Predicted labels:",predictions)
    print("Accuracy:",accuracy_score(yTest,predictions))

    return fitting

# modelTrainingAndEvulation(model,xTrainMinMax,xTestMinMax,yTrain,yTest)


# In[ ]:


# Seriliazation model
def serilization(model):
    ##Saving current model
    import pickle
    pickle.dump(model,open("spotify_model.pkl","wb"))
    print('done')

# serilization(model)

