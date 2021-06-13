import joblib
import numpy as np


class HMG:
    def __init__(self, model_path='./models/hmg.pkl'):
        self.hmg_model = joblib.load(model_path)
    
    def __call__(self, manipulated_variables, disturbing_variables, disturbed_variables, prev_furnace_state):
        # zmienne: manipulowane, zakłócające, zakłócane, poprzedni stan pieca
        input_parameters = np.array([*manipulated_variables, *disturbing_variables, 
                                     *disturbed_variables])#, *prev_furnace_state])
             
        heat = self.hmg_model.predict([input_parameters])
        
        return heat

