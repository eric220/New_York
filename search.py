import numpy as np
from keras.preprocessing import image
import utils
import models

model_width = 224
half_model_width = int(224 * .5)
est_location = 200
half_est_location = int(est_location * .5)

#searchs all pixels within small window
def narrow_search(img, x_start, x_finish, y_start, y_finish, goal):
    dist_array = []
    t_i = []
    t_j = []
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            test_slice = utils.get_img_slice(img, i, j, model_width)
            test_img = image.array_to_img(test_slice)
            dist_array.append(utils.vector_dist(goal, models.get_pred(test_img))[0][0])
            t_i.append(i)
            t_j.append(j)
    
    return t_i[np.argmin(dist_array): np.argmin(dist_array) + 1][0], t_j[np.argmin(dist_array): np.argmin(dist_array) + 1][0] 

def deviation_assisted_search(tee_ny, rand_x_start, rand_x_fin, rand_y_start, rand_y_fin, goal, num_samples):
    x, y = std_dev_search(tee_ny, rand_x_start, rand_x_fin, rand_y_start, rand_y_fin, goal, num_samples)
    x, y = std_dev_search(tee_ny, x - 100, x + 100, y - 100, y + 100, goal, 25)
    x, y = std_dev_search(tee_ny, x - 50, x + 50, y - 50, y + 50, goal, 25)
    x, y = std_dev_search(tee_ny, x - 25, x + 25, y - 25, y + 25, goal, 25)
    x, y = std_dev_search(tee_ny, x - 10, x + 10, y - 10, y + 10, goal, 25)
    x, y = narrow_search(tee_ny, x - 5, x + 6, y - 5, y + 6, goal)
    return x, y

#dev assisted search returns x, y coordinates
def std_dev_search(img, x_start, x_finish, y_start, y_finish, goal, num_samples):
    rand_x = np.random.randint(x_start, x_finish, num_samples)
    rand_y = np.random.randint(y_start, y_finish, num_samples)
    dist_array = []
    for i in range(len(rand_x)):
        test_slice = utils.get_img_slice(img, rand_x[i], rand_y[i], model_width)
        test_img = image.array_to_img(test_slice)
        dist_array.append(utils.vector_dist(goal, models.get_pred(test_img))[0][0])
    #print('STD',np.std(dist_array), 'Mean',np.mean(dist_array), 'Value',dist_array[np.argmin(dist_array): np.argmin(dist_array)+1][0], 'arg',np.argmax(dist_array))
    if dist_array[np.argmin(dist_array): np.argmin(dist_array)+1] < (np.mean(dist_array) - (np.std(dist_array))):
        return utils.return_xy(rand_x, rand_y, np.argmin(dist_array))
    else:
        print('do it again')
        #return return_xy(rand_x, rand_y, np.argmin(dist_array))
        
#random search of narrowing windows
#search
def narrowing_search():
    x, y = random_search(tee_ny, rand_x_start, rand_x_fin, rand_y_start, rand_y_fin, 100)
    x, y = random_search(tee_ny, x - 100, x + 100, y - 100, y + 100, 100)
    x, y = random_search(tee_ny, x - 50, x + 50, y - 50, y + 50, 100)
    x, y = narrow_search(tee_ny, x - 5, x + 6, y - 5, y + 6)
    return x, y
        

#randomly searches to narrow down search window
def random_search(img, x_start, x_finish, y_start, y_finish):
    num_samples = 500
    rand_x = np.random.randint(x_start, x_finish, num_samples)
    rand_y = np.random.randint(y_start, y_finish, num_samples)
    dist_array = []
    for i in range(len(rand_x)):
        test_slice = get_img_slice(img, rand_x[i], rand_y[i], model_width)
        test_img = image.array_to_img(test_slice)
        dist_array.append(vector_dist(goal_pred, get_pred(test_img))[0][0])
    return return_xy(rand_x, rand_y, np.argmin(dist_array))