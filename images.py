from keras.preprocessing import image

#display full image with tee_ny (arbitrary) area selected
#plt.figure(figsize = (15,15))
#plt.gca().add_patch(Rectangle((5000, 8250), 2000, 2000, linewidth = 3, edgecolor = 'r', facecolor = 'none'));
#plt.imshow(np.asarray(img));

def get_image(filename):
    return image.load_img(filename)

    