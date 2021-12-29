#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag


# In[2]:


def login():
    username = driver.find_element_by_id("login-email")
    username.send_keys("username")
    password = driver.find_element_by_id("login-password")
    password.sed_keys("password")
    driver.find_element_by_id("login-submit").click()


# In[3]:


def goto_network():
    driver.find_element_by_id("mynetwork-tab-icon").click()


# In[4]:


def send_requests():
    n = input("Number of requests : ")
    for i in range(0,n):
        pag.click(880, 770)
    print("Done!!!")    


# In[5]:


def main():
    url = "http://linkedin.com/"
    network_url = "http://linkedin.com/mynetwork/"
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(url)


# In[7]:


if __name__ == "__main__":
    main()
