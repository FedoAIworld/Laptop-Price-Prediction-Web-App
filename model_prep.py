import pickle as pkl
import numpy as np

# Random Forest Regressor Model
model = pkl.load(open('RF_model.pkl', 'rb'))



class Price_Prediction:
    """
    Initialize model attributes for price prediction
    """
    
    def __init__(self, brand, typename, ram, opsys, weight, touchscreen, ips, inches, resolution, cpu, gpu, hdd, ssd):
        self.brand = brand
        self.typename = typename
        self.ram = ram
        self.opsys = opsys
        self.weight = weight
        self.touchscreen = touchscreen
        self.ips = ips
        self.inches = inches
        self.resolution = resolution
        self.cpu = cpu
        self.gpu = gpu
        self.hdd = hdd
        self.ssd = ssd
        self.organize()

    def organize(self):
        list_attributes = [0] * 13
        
        list_attributes[0] = self.brand
        list_attributes[1] = self.typename
        list_attributes[2] = self.ram
        list_attributes[3] = self.opsys
        list_attributes[4] = self.weight
        list_attributes[5] = self.touchscreen
        list_attributes[6] = self.ips
        list_attributes[7] = self.inches
        list_attributes[8] = self.resolution
        list_attributes[9] = self.cpu
        list_attributes[10] = self.gpu
        list_attributes[11] = self.hdd
        list_attributes[12] = self.ssd

        self.predict(list_attributes)

    def predict(self, laptop_features): 
        array_predict = np.array([laptop_features])
        self.final_prediction = model.predict(array_predict)