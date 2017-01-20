import os
from os import listdir
import sys

file_list = []

def make_dict_count(file_list):
    dict_counts = dict()

    for filename in file_list:
        file_split = filename.split("_")
        subject = file_split[0] + "_" + file_split[1]
        if subject not in dict_counts.keys():
            dict_counts.update({subject : 0})
        dict_counts[subject] = dict_counts[subject] + 1
    return dict_counts

def get_mode_group_size(dict_counts):
    dict_mode = dict()
    group_sizes = dict_counts.values()
    for size in group_sizes:
        if size not in dict_mode:
            dict_mode.update({size : 0})
        dict_mode[size] = dict_mode[size] + 1

    mode_size = 0
    num_groups = 0
    for element in dict_mode.items():
        if element[1] > num_groups:
            num_groups = element[1]
            mode_size = element[0]

    if num_groups == len(dict_counts.keys()):
        print True

    mode_group_size = mode_size

    return mode_group_size

def outlire_file_groups(dict_counts, mode_group_size):
    #f = open("output_file_groups.txt", "wb")
    #f.write("Most group sizes = " + str(mode_group_size) + "\n")
    #for key in dict_counts.keys():
        #if dict_counts[key] != mode_group_size:
            #f.write("Group " + key + ": has size " + str(dict_counts[key]) + "\n")
    for key in dict_counts.keys():
        if dict_counts[key] == mode_group_size:
            del dict_counts[key]
    if len(dict_counts) == 0:
        print True
    else:
        print False
        print dict_counts

if __name__ == "__main__":
    file_path = sys.argv[1]
    file_list = os.listdir(file_path)

    dict_counts = make_dict_count(file_list)
    mode_group_size = get_mode_group_size(dict_counts)
    print "Most group sizes = " + str(mode_group_size)

    outlire_file_groups(dict_counts, mode_group_size)









