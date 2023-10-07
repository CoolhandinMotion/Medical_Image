from dataclasses import dataclass, field
from collections import defaultdict
from typing import List
import numpy as np
import numpy.typing as npt


# add caching?
class Cluster:
    def __init__(self, index: int, members: List[npt.NDArray]):
        self.index = index
        self.members = members

    def calculate_features(self):
        array = np.asarray(self.members)
        array = np.reshape(array, (len(array),3))



class Initiate:
    @staticmethod
    def build_image_2_array_dict(img):
        image_data_2_array_dict = defaultdict()
        rows = img.shape[0]
        cols = img.shape[1]
        for i in range(rows):
            for j in range(cols):
                image_data_2_array_dict[(i, j)] = np.asarray([i, j, img[i][j]])
        return image_data_2_array_dict

    @staticmethod
    def build_image_array(img):
        image_array = [[t, k, img[t][k]] for t in range(img.shape[0]) for k in range(img.shape[1])]
        return np.asarray(image_array)

    @staticmethod
    def build_data_2_cluster_dict(cluster_2_data_dict):
        data_2_cluster_dict = defaultdict()
        for cluster in cluster_2_data_dict:
            for data_point in cluster_2_data_dict[cluster]:
                data_2_cluster_dict[tuple(data_point)] = cluster
        return data_2_cluster_dict