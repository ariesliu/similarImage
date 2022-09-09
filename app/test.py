# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from util.util import *
from app.img_similarity import *

# 百度识图地址
baidu_page = 'https://graph.baidu.com/pcpage/index?tpl_from=pc'
# 目标图片地址
img_url = "https://img0.baidu.com/it/u=2857226888,1505709671&fm=253&fmt=auto&app=138&f=JPEG?w=751&h=500"
# 图片相似度阈值
similarity_threshold = 0.6

def search_similar_images(browser, image_url):
    # 上传图片url
    browser.get(baidu_page)
    url_upload_textbox = browser.find_element_by_xpath(r'//*[@id="app"]/div/div[1]/div[7]/div/span[1]/input')
    url_upload_textbox.send_keys(image_url)
    time.sleep(1)

    # 开始识图
    search_image_button = browser.find_element_by_xpath(r'//*[@id="app"]/div/div[1]/div[7]/div/span[2]')
    search_image_button.click()
    time.sleep(5)

    try:
        # 滑块验证码
        block = browser.find_element_by_class_name('vcode-slide-button')
        ActionChains(browser).click_and_hold(block).perform()
        ActionChains(browser).move_by_offset(300, 0).perform()
        ActionChains(browser).release().perform()
        time.sleep(3)
    except Exception as e:
        print(e)

    # 相似图片列表
    graph_similar_list = browser.find_element_by_class_name('graph-similar-list')
    time.sleep(3)

    # 读取数据文件
    source_path = get_source_file("data")
    list = get_info(source_path, "=")

    for i in list:
        index = i[1].strip()
        # 点击图片
        pic = graph_similar_list.find_element_by_css_selector('div > div:nth-child('+index+') > a:nth-child(1)')

        # 验证图片相似度
        similar_image_url = pic.find_element_by_css_selector("img").get_attribute("src")
        similarity = calc_image_similarity(similar_image_url, img_url);
        if similarity >= similarity_threshold:
            print("the pic_" + index + " is similar with a similarity of " + str(similarity))
        else:
            print("the pic" + index + "is not similar with a similarity of " + str(similarity))

        # 点击目标图片
        pic.click()
        time.sleep(3)

        # 切换到子窗口
        browser.switch_to.window(browser.window_handles[1])
        # 截图
        browser.get_screenshot_as_file(get_screenshot_file("pic"))


if __name__ == "__main__":
    browser = webdriver.Chrome()
    time.sleep(1)

    try:
        # 获取百度识图结果
        search_similar_images(browser, img_url)
    except Exception as e:
        print("search failed")

    browser.quit()






