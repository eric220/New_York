import keras
from keras.layers import Flatten, MaxPooling2D
from keras.models import Model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input

#return model
def get_model():
    res_model = ResNet50(include_top=False, weights = 'imagenet', input_shape = (224, 224, 3))
    #res_model = ResNet50(include_top=False, weights = 'imagenet', input_shape = (224, 224, 3), pooling = 'max')
    max_pool = MaxPooling2D()(res_model.output)
    max_pool2 = MaxPooling2D()(max_pool)
    flat_1 = Flatten()(max_pool2)
    #flat_1 = Flatten()(max_pool)
    model = Model(inputs = res_model.inputs, outputs = flat_1)
    model.compile(optimizer = 'rmsprop', loss = "categorical_crossentropy", metrics = ['accuracy'])
    return model

#return prediction
def get_pred(t_img):
    t_test = image.img_to_array(t_img)
    t_test = np.expand_dims(t_test, axis=0)
    t_test = preprocess_input(t_test)
    return model.predict(t_test)