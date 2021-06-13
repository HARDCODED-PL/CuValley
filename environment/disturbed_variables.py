import joblib
import numpy as np


class DisturbedVariables:
    def __init__(self, model_path='./models/disturbed_variables_model.pkl'):
        self.disturbed_variables_model = joblib.load(model_path)
    
    def __call__(self, manipulated_variables, disturbing_variables, prev_disturbed_variables):
        # zmienne: manipulowane, zakłócające, zakłócane (poprzedni stan)
        input_parameters = np.concatenate([manipulated_variables, 
                                           disturbing_variables, 
                                           prev_disturbed_variables])
             
        disturbed_variables = self.disturbed_variables_model.predict([input_parameters])
        
        return disturbed_variables[0]
