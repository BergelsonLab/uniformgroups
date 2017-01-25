import unifgroup
import os
from os import listdir
import sys

#Input is "path to folder" with files to analyze
def check_unique_groups(input):
    res_dict = dict()

    file_list = os.listdir(input)
    dict_counts = unifgroup.make_dict_count(file_list)
    mode_group_size = unifgroup.get_mode_group_size(dict_counts)

    for key in dict_counts.keys():
        if dict_counts[key] == mode_group_size:
            res_dict.update({key : (True, None)})
        else:
            res_dict.update({key : (False, dict_counts[key])})
    return res_dict

def group_size_check_list(input):
    res_list_non_outlires = []
    res_list_outlires = []

    file_list = os.listdir(input)
    dict_counts = unifgroup.make_dict_count(file_list)
    mode_group_size = unifgroup.get_mode_group_size(dict_counts)

    for key in dict_counts.keys():
        if dict_counts[key] == mode_group_size:
            res_list_non_outlires.append(key)
        if dict_counts[key] != mode_group_size:
            res_list_outlires.append(key)
    if unifgroup.outlires_exist(dict_counts, mode_group_size) == True:
        return res_list_outlires
    if unifgroup.outlires_exist(dict_counts, mode_group_size) == False:
        return res_list_non_outlires