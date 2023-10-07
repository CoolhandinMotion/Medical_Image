import cv2
import numpy as np
from model import Model
import json
import numpy.typing as npt

GRAVITY_ONE_DIMENSIONAL = 2.5066282746310002
GRAVITY_THREE_DIMENSIONAL = 7.8748049728612095



class Gravity:
    ...


def calculate_1d_gravity(data_list: list[npt.NDArray], control_value: float):
    num = len(data_list)
    arr = np.reshape(np.array(data_list), (num, 3))
    std_1d = np.std(arr[:, -1], axis=0)
    gravity = GRAVITY_ONE_DIMENSIONAL * (std_1d ** 3) * (control_value ** 2) * np.exp((control_value ** 2) / 2)
    return gravity

def calculate_1d_force(data_point: npt.NDArray, cluster_mean_array: npt.NDArray):
    return np.absolute(data_point-cluster_mean_array)**3

