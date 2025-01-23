from fastapi import FastAPI
import uvicorn
import numpy as np
import pickle
from pydantic import BaseModel


app=FastAPI()


with open('decision_classifier_model.pkl', 'rb') as file:
    model = pickle.load(file)

class InputRequest(BaseModel):
    features : list


@app.get('/index/{name}')
async def index(name:str):
    return f'Hello {name} : This is Iris Classifier  '

@app.post('/predict/{input}')
async def predict(input_features: InputRequest):
    input = np.array(input_features.features).reshape(1,-1)
    prediction = model.predict(input)
    if prediction==0:
        return 'Setosa'
    elif prediction==1:
        return 'Versicolor'
    else:
        return 'virginica'



if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)





