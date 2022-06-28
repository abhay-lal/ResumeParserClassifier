from tensorflow import keras
class Model:
    def __init__(self, text):
        self.normalize(text) 
    #Creating a function to run the model and classify the resume text
    def predict_out(self, text):
        model = keras.models.load_model('Notebooks/Model/DNN Model-final.ipynb')
        pred = model.predict(text)
        return pred
    
    #Creating a function to return a list of outputs based on the proabilities of each class
    def normalize(self, text):
        pred = self.predict_out(text)
        list_out = []
        for j in pred:
            if j>=0.5:
                list_out.append(1)
            else:
                list_out.append(0)
        return list_out
        
    
        
          