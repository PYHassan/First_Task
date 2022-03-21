# '''Exercise 4: Scraping Test'''
#import webdriver
from selenium import webdriver

#import time
from time import sleep

# create webdriver object
driver = webdriver.Chrome()

# get the website
driver.get("https://twitter.com/KMbappe")

# sleep for some time
sleep(3)

# get element through text
element = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span')
followers_count = element.text
print(followers_count)
