# coding=utf-8

import time
import os


def get_info(file_name, split_tag):
    temp_list = []
    with open(file_name,'r',encoding='UTF-8') as f:
        if split_tag != "":
            for i in f:
                temp = i.strip().split(split_tag)
                temp_list.append(temp)
        else:
            temp_list = [i.strip() for i in f]
    return temp_list


def get_screenshot_file(file_name):
    sys_time = time.strftime("%Y%m%d%H%M%S")
    # 截图名称：时间+后缀
    png_name = file_name + sys_time + ".png"
    dir_path = os.path.dirname(__file__)
    # 截图存放位置
    png_file = os.path.join(dir_path, "..", "result", png_name)
    return png_file


def get_source_file(file_name):
    dir_path = os.path.dirname(__file__)
    source_file = os.path.join(dir_path, "..", "source",file_name)
    return source_file