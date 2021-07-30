from keras.preprocessing import image
#just kind of saving stuff

#display full image with tee_ny (arbitrary) area selected
#plt.figure(figsize = (15,15))
#plt.gca().add_patch(Rectangle((5000, 8250), 2000, 2000, linewidth = 3, edgecolor = 'r', facecolor = 'none'));
#plt.imshow(np.asarray(img));

#full image view and full image as array
#img = image.load_img("ny_resized.jpg")
#full_img = image.img_to_array(img)

def get_image(filename):
    return image.load_img(filename)

#return subarray (tee_ny) from full image, arbitrarily chosen
#tee_ny = full_img[8250: 10250, 5000:  7000, :]
#tee_ny_img = image.array_to_img(tee_ny)
#plt.figure(figsize = (15,15))
#plt.axvline(x= rand_x_start, color= 'red')
#plt.axvline(x= rand_x_fin, color= 'red')
#plt.axhline(y= rand_y_start, color= 'red')
#plt.axhline(y= rand_y_fin, color= 'red')
#plt.title('New York section with target pixel')
#plt.imshow(tee_ny);