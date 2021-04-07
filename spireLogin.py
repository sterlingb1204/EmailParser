#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:02:39 2020

@author: sterling
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd



def scrape_contact(url,i,driver,timeout):
    driver.get(url)
    index = str(i)
#    element_present = EC.presence_of_element_located((By.XPATH,notFound_xpath)) #checks first name box
#    WebDriverWait(driver, 2).until(element_present)
    personInfo = {}
    
    try:
        first_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[1]/input'
        element_present = EC.presence_of_element_located((By.XPATH,first_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        first_name = driver.find_element_by_xpath(first_xpath).get_attribute('value')
        print("First:{}".format(first_name))
        
        last_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[2]/input'
        element_present = EC.presence_of_element_located((By.XPATH,last_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        last_name = driver.find_element_by_xpath(last_xpath).get_attribute('value')
        print("Last:{}".format(last_name))
        
        email_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[3]/input'
        element_present = EC.presence_of_element_located((By.XPATH, email_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        email = driver.find_element_by_xpath(email_xpath).get_attribute('value')
        print("Email:{}".format(email))
        
        mobile_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[4]/input'
        element_present = EC.presence_of_element_located((By.XPATH, mobile_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        mobile = driver.find_element_by_xpath(mobile_xpath).get_attribute('value')
        print("Mobile:{}".format(mobile))
        
        work_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[5]/input'
        element_present = EC.presence_of_element_located((By.XPATH, work_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        work = driver.find_element_by_xpath(work_xpath).get_attribute('value')
        print("Work:{}".format(work))    
        
        address1_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[6]/input'
        element_present = EC.presence_of_element_located((By.XPATH, address1_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        address1 = driver.find_element_by_xpath(address1_xpath).get_attribute('value')
        print("Address:{}".format(address1))
        
        address2_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[7]/input'
        element_present = EC.presence_of_element_located((By.XPATH, address2_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        address2 = driver.find_element_by_xpath(address2_xpath).get_attribute('value')
        print("        {}".format(address2))
                
        region_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[8]/ul/li'
        element_present = EC.presence_of_element_located((By.XPATH, region_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        region = driver.find_element_by_xpath(region_xpath).text
        print("Region:{}".format(region))
    
        city_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[9]/input'
        element_present = EC.presence_of_element_located((By.XPATH, city_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        city = driver.find_element_by_xpath(city_xpath).get_attribute('value')
        print("City:{}".format(city))   
        
        state_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[10]/input'
        element_present = EC.presence_of_element_located((By.XPATH, state_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        state = driver.find_element_by_xpath(state_xpath).get_attribute('value')
        print("State:{}".format(state))  
        
        zip_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[11]/input'
        element_present = EC.presence_of_element_located((By.XPATH, zip_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        zipcode = driver.find_element_by_xpath(zip_xpath).get_attribute('value')
        print("Zip:{}".format(zipcode))   
        
        country_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[1]/div/div[2]/div/div[12]/input'
        element_present = EC.presence_of_element_located((By.XPATH, country_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        country = driver.find_element_by_xpath(country_xpath).get_attribute('value')
        print("Country:{}".format(country))
        
        #################################Employment Section##########################
        employment_xpath = '/html/body/div[4]/section[2]/div/div/ul/li[2]/a'
        element_present = EC.presence_of_element_located((By.XPATH, employment_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        driver.find_element_by_xpath(employment_xpath).click()
        
        title_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[2]/div/div[1]/input'
        element_present = EC.presence_of_element_located((By.XPATH,title_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        title = driver.find_element_by_xpath(title_xpath).get_attribute('value')
        print("Title:{}".format(title))
        
        company_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[2]/div/div[2]/input'
        element_present = EC.presence_of_element_located((By.XPATH,company_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        company = driver.find_element_by_xpath(title_xpath).get_attribute('value')
        print("Company:{}".format(company))
        
        industry_xpath = '/html/body/div[4]/section[2]/div/div/form/div/div[2]/div/div[3]/input'
        element_present = EC.presence_of_element_located((By.XPATH,industry_xpath)) #checks first name box
        WebDriverWait(driver, timeout).until(element_present)
        industry = driver.find_element_by_xpath(industry_xpath).get_attribute('value')
        print("Industry:{}".format(industry))
        
        personInfo = {'index':index, 'first_name':first_name, 'last_name':last_name, 'email':email, 'mobile':mobile, 'work':work, 'address 1':address1, 'address2':address2, 'region':region, 'city':city, 'state':state, 'zip':zipcode, 'country':country, 'title':title, 'company':company, 'industry':industry}
        return personInfo
    
    except:
        return False
    

def collection(profile_id):
    scrape_contact('https://www.spirestanford.org/members/profile/{}/'.format(profile_id))
    return None    

#driver.quit()


def loopy(start,stop):    
#login Process
    driver = webdriver.Chrome('*****REDACTED*****')
    timeout = 1
    driver.get('https://www.spirestanford.org/accounts/login/?next=/members/profile/13540/')
    username = driver.find_element_by_id("id_username")
    password = driver.find_element_by_id("id_password")
    username.send_keys("*****REDACTED*****")
    password.send_keys("*****REDACTED*****")
    
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/form/input[4]'))
        WebDriverWait(driver, 5).until(element_present)
        login = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/input[4]')
        login.click()
    except:
        print("Error Logging In")
        return None
    
    data = []
    i = start
    while i < stop:
        time.sleep(2)
        found = scrape_contact('*****REDACTED*****'.format(i),i,driver,timeout)
        if found:
            data.append(found)
        else:
            print("Error finding profile: {}".format(i))
        i+=1
        
    df = pd.DataFrame(data)
    df.to_excel('spire30000.xlsx')
    driver.quit()
    print(df)
    return df

loopy(20000,30000)

# Page Not found xpath


    


