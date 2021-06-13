import numpy as np


class StabilityRegulator:
    def __init__(self):
        # przepływ powietrza
        self.air_max_regulation = (1900, 3500)
        #self.air_max_step = 800 # 
        #self.air_min_time = 10 # sec
        self.air_max_step = 80 # 
        self.air_min_time = 1 # sec
    
        # zawartość tlenu
        self.oxy_max_regulation = (65, 81)
        #self.oxy_max_step = 2
        #self.oxy_min_time = 150
        self.oxy_max_step = 0.8
        self.oxy_min_time = 60
        
        # dmuch
        self.puff_max_regulation = (40, 70)
        #self.puff_max_step = 10
        #self.puff_min_time = 5
        self.puff_max_step = 2
        self.puff_min_time = 1
        
        #pyły
        self.dust_max_regulation = (13, 27)
        self.dust_max_step = 13
        self.dust_min_time = 5*60
    
    def __call__(self, prev, new):
        prev_air, prev_oxy, prev_puff, prev_dust = prev
        new_air, new_oxy, new_puff, new_dust = new
        
        dest_air = prev_air
        dest_oxy = prev_oxy
        dest_puff = prev_puff
        dest_dust = prev_dust
        
        dest_air += np.min([np.abs(new_air), self.air_max_step]) * np.sign(new_air)
        dest_oxy += np.min([np.abs(new_oxy), self.oxy_max_step]) * np.sign(new_oxy)
        dest_puff += np.min([np.abs(new_puff), self.puff_min_time]) * np.sign(new_puff) 
        dest_dust += np.min([np.abs(new_dust), self.dust_min_time]) * np.sign(new_dust) 
        
        dest_air = np.clip(dest_air, *self.air_max_regulation)
        dest_oxy = np.clip(dest_oxy, *self.oxy_max_regulation)
        dest_puff = np.clip(dest_puff, *self.puff_max_regulation)
        dest_dust = np.clip(dest_dust, *self.dust_max_regulation)
        
        return np.array([dest_air, dest_oxy, dest_puff, dest_dust])
