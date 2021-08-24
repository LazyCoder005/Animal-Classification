'''
author: AaryaPanchal
'''

import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import  image

class animals:
    def __init__(self,filename):
        self.filename =filename


    def predictionanimals(self):
        # load model
        model = load_model('Model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        output = np.argmax(result)

        classes = ['butterfly','cat','chicken','cow','dog','elephant','horse','sheep','spider','squirrel']

        if output == 0:
            return [{'Predicted Animal is' : classes[0]}]

        elif output == 1:
            return [{'Predicted Animal is' : classes[1]}]

        elif output == 2:
            return [{'Predicted Animal is' : classes[2]}]

        elif output == 3:
            return [{'Predicted Animal is' : classes[3]}]

        elif output == 4:
            return [{'Predicted Animal is' : classes[4]}]

        elif output == 5:
            return [{'Predicted Animal is' : classes[5]}]

        elif output == 6:
            return [{'Predicted Animal is' : classes[6]}]

        elif output == 7:
            return [{'Predicted Animal is' : classes[7]}]

        elif output == 8:
            return [{'Predicted Animal is' : classes[8]}]

        else:
            return [{'Predicted Animal is' : classes[9]}]