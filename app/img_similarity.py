# coding=utf-8

import cv2
import numpy as np
import urllib.request
import ssl


# 计算两个图片相似度函数ORB算法
def calc_image_similarity(img1_url,img2_url):
    try:
        # 读取图片
        img1 = get_img(img1_url)
        img2 = get_img(img2_url)

        # 初始化ORB检测器
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # 提取并计算特征点
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        # knn筛选结果
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

        # 查看最大匹配点数目
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        similary = len(good) / len(matches)
        return round(similary, 3)

    except Exception as e:
        print(e)
        return '0'


def get_img(img_url):
    ssl._create_default_https_context = ssl._create_unverified_context
    res = urllib.request.urlopen(img_url)
    img = np.asarray(bytearray(res.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img


if __name__ == '__main__':
    img_url1 = "https://img0.baidu.com/it/u=2857226888,1505709671&fm=253&fmt=auto&app=138&f=JPEG?w=751&h=500";
    img_url2 = "http://mms2.baidu.com/it/u=66080015,3878690024&fm=253&app=138&f=JPEG&fmt=auto&q=75?w=748&h=500";
    value = calc_image_similarity(img_url1, img_url2)
    print(value)