import cv2 as cv 
import numpy as np
import random

HEIGHT = 800
WIDTH = 800 

x_0 = (HEIGHT - 1) / 2
y_0 = (WIDTH - 1) / 2

def rad_distortion(img, k1, k2, k3):
    rad_dist_img = np.zeros((HEIGHT,WIDTH,3), np.uint8) 
    img = cv.resize(img, (HEIGHT, WIDTH))

    for i in range(HEIGHT):
        for j in range(WIDTH):
            
            x = i - x_0
            y = j - y_0

            r1 = pow(x, 2) + pow(y,2)
            r2 = pow(r1, 2)
            r3 = pow(r2, 2)
            x_d = (1 + k1 * r1 + k2 * r2 + k3 * r3) * x 
            y_d = (1 + k1 * r1 + k2 * r2 + k3 * r3) * y

            x_d = int(x_d + x_0)
            y_d = int(y_d + y_0)

            if (x_d >= 0 and x_d < WIDTH) and (y_d >= 0 and y_d < HEIGHT):
                rad_dist_img[i][j][0] = img[x_d][y_d][0] 
                rad_dist_img[i][j][1]  = img[x_d][y_d][1] 
                rad_dist_img[i][j][2]  = img[x_d][y_d][2] 
        
    return rad_dist_img


def tan_distortion(img, p1, p2):
    tan_dist_img = np.zeros((HEIGHT,WIDTH,3), np.uint8) 
    img = cv.resize(img, (HEIGHT, WIDTH))

    for i in range(HEIGHT):
        for j in range(WIDTH):
            
            x = i - x_0
            y = j - y_0

            r1 = pow(x, 2) + pow(y,2)

            x_d = 2 * p1 * x * y + p2 * (pow(r1, 2) + 2 * pow(x,2))
            y_d = 2 * p1 * x * y + p2 * (pow(r1, 2) + 2 * pow(y,2))

            x_d = int(x_d + x_0)
            y_d = int(y_d + y_0)

            if (x_d >= 0 and x_d < WIDTH) and (y_d >= 0 and y_d < HEIGHT):
                tan_dist_img[i][j][0] = img[x_d][y_d][0] 
                tan_dist_img[i][j][1]  = img[x_d][y_d][1] 
                tan_dist_img[i][j][2]  = img[x_d][y_d][2] 

    return tan_dist_img

k1_top = 1e-10
k1_down = 1e-12

k2_top = 1e-15
k2_down = 1e-16

k3_top = 1e-19
k3_down = 1e-21

p1_top = 1e-1
p1_down = 1e-3

p2_top = 1e-5
p2_down = 1e-7

k1 = random.uniform(k1_down, k1_top)
k2 = random.uniform(k2_down, k2_top)
k3 = random.uniform(k3_down, k3_top)

p1 = random.uniform(p1_top, p1_down)
p2 = random.uniform(p2_top, p2_down)

path = "PATH"
img_name = "IMAGE"
img = cv.imread(path + img_name)

rad_dist_img = rad_distortion(img, k1, k2, k3)
tan_dist_img = tan_distortion(img, p1, p2)

rad_dist_img = cv.resize(rad_dist_img, (512,512))
tan_dist_img = cv.resize(tan_dist_img, (512,512))

cv.imshow('test', tan_dist_img)
cv.waitKey(1500)

cv.imwrite(path + 'test.jpg', tan_dist_img) # this can be changed to rad_dist_img 

