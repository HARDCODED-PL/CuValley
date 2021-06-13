import joblib
import numpy as np


class DummyOperator:
    def __init__(self, model_path='./models/dummy_operator.pkl'):
        self.dummy_operator_model = joblib.load(model_path)
    
    def __call__(self, prev_manipulated_variables, disturbing_variables, disturbed_variables):
        # zmienne: manipulowane (stan poprzedni), zakłócające, zakłócane
        input_parameters = np.concatenate([prev_manipulated_variables, disturbing_variables, disturbed_variables])
             
        manipulated_variables = self.dummy_operator_model.predict([input_parameters])
        
        return manipulated_variables[0]
