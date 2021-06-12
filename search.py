import numpy as np
from keras.preprocessing import image

#random search returns x, y coordinates

#slices image 
    def get_img_slice(t_img, x, y, model_width):
    t_array = t_img[y + half_est_location: y + model_width + est_location - half_est_location, x + half_est_location: x + model_width + est_location - half_est_location, :]
    return t_array

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

#searchs all pixels within small window
def narrow_search(img, x_start, x_finish, y_start, y_finish):
    dist_array = []
    t_i = []
    t_j = []
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            test_slice = get_img_slice(img, i, j, model_width)
            test_img = image.array_to_img(test_slice)
            dist_array.append(vector_dist(goal_pred, get_pred(test_img))[0][0])
            t_i.append(i)
            t_j.append(j)
    
    return t_i[np.argmin(dist_array): np.argmin(dist_array) + 1][0], t_j[np.argmin(dist_array): np.argmin(dist_array) + 1][0] 

#runs random search twice (narrowing window), then runs narrow search 
def target_search(tee_ny, rand_x_start, rand_x_fin, rand_y_start, rand_y_fin):
    #x, y = random_search(tee_ny, x_start_num, x_finish_num, y_start_num, y_finish_num)
    x, y = random_search(tee_ny, rand_x_start, rand_x_fin, rand_y_start, rand_y_fin)
    x, y = random_search(tee_ny, x - 50, x + 50, y - 50, y + 50)
    x, y = narrow_search(tee_ny, x - 5, x + 6, y - 5, y + 6)
    return x, y