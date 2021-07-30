from scipy import spatial

model_width = 224
half_model_width = int(model_width * .5)
est_location = 200
#half_est_location = int(est_location * .5)

#return distance between vector points
def vector_dist(v1, v2):
    return spatial.distance.cdist(v1, v2)
    
#return value from x/y index
def return_xy(randx, randy, idx):
    t_x = randx[idx : idx + 1]
    t_y = randy[idx : idx + 1]
    return int(t_x), int(t_y)
    
#slices image 
def get_img_slice(t_img, x, y, model_width):
    t_array = t_img[y: y + model_width, x: x + model_width, :]
    return t_array

#middle pixel in, returns starting point half model and half location est away from pix, same with ending points
def start_lines(pix_x, pix_y, half_est_location):
    x_start = pix_x - half_est_location - half_model_width 
    x_finish = pix_x + half_est_location + half_model_width
    y_start = pix_y - half_est_location - half_model_width 
    y_finish = pix_y + half_est_location + half_model_width
    return x_start, x_finish, y_start, y_finish