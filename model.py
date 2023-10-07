from dataclasses import dataclass, field
from collections import defaultdict
from typing import List
import numpy as np
import numpy.typing as npt

GRAVITY_ONE_DIMENSIONAL = 2.5066282746310002
GRAVITY_THREE_DIMENSIONAL = 7.8748049728612095


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

    @staticmethod
    def build_1d_cluster_ref_dict(cluster_2_data_dict, control_value):
        cluster_ref_dict = defaultdict()
        for cluster in cluster_2_data_dict:
            members = cluster_2_data_dict[cluster]
            num = len(members)
            # to prevent dividing by zero or calculating mean of empty array
            if num <= 2:
                continue
            arr = np.reshape(np.array(members), (num, 3))
            mean_1d = np.mean(arr[:, -1], axis=0)
            std_1d = np.std(arr[:, -1], axis=0)
            gravity_1d = GRAVITY_ONE_DIMENSIONAL * (std_1d ** 3) * (control_value ** 2) * np.exp(
                (control_value ** 2) / 2)
            cluster_ref_dict[cluster] = [mean_1d, std_1d, gravity_1d]
        return cluster_ref_dict

    @staticmethod
    def build_3d_cluster_ref_dict(cluster_2_data_dict, control_value):
        # take into account the feedback k
        # correct the way gravity is calculated according to the paper
        cluster_ref_dict = defaultdict()
        for cluster in cluster_2_data_dict:
            members = cluster_2_data_dict[cluster]
            num = len(members)

            arr = np.reshape(np.array(members), (num, 3))
            mean_3d = np.mean(arr, axis=0)
            std_3d = np.std(arr, axis=0)
            gravity_3d = ...
            cluster_ref_dict[cluster] = [mean_3d, std_3d, gravity_3d]
        return cluster_ref_dict