from keras.preprocessing import image

def get_image(filename):
    return image.load_img(filename)

    