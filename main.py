import cv2
import numpy as np
from model import  Initiate
from tile import Tiler
from control import calculate_1d_gravity


image_path = r"E:\PycharmProjects\Medical_Image\Picture1.png"
img = cv2.imread(image_path,0)
image_array = Initiate.build_image_as_1d_array(img)

# image to array dictionary may be redundant needs more investigation
image_data_2_array_dict = Initiate.build_image_2_array_dict(img)
cluster_2_data_dict = Tiler.grayscale_tile(img,20)
data_2_cluster_dict = Initiate.build_data_2_cluster_dict(cluster_2_data_dict)
cluster_reference_dict = Initiate.build_1d_cluster_ref_dict(cluster_2_data_dict, .8)

