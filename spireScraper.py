from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd

# If you want to open Chrome
driver = webdriver.Chrome('/Users/sterling/Documents/School/CompSci/Parser/chromedriver')
timeout = 30
driver.get('https://www.spirestanford.org/accounts/login/?next=/members/profile/13540/')


username = driver.find_element_by_id("id_username")
password = driver.find_element_by_id("id_password")
username.send_keys("*****REDACTED*****")
password.send_keys("*****REDACTED*****")
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/form/input[4]'))
    WebDriverWait(driver, timeout).until(element_present)
    login = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/input[4]')
    login.click()
except:
    print("Error Logging In")
    
element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table[1]/tbody/tr/td[2]/h5/a'))
WebDriverWait(driver, timeout).until(element_present)
person = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table[16]/tbody/tr/td[2]/h5/a')
#old version starting at 1: person = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table[1]/tbody/tr/td[2]/h5/a')
person.click()


data = {}
i = 796
while i <= 1562:
    #Checks to Find name
    if i%100 == 0:
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_excel("OutputFinal{}.xls".format(i))
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong'))
        WebDriverWait(driver, timeout).until(element_present)
        name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong').text # individual name
        description = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div/p').text
        email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[2]/dl/dd[2]/a[1]').text # individual Email
        print("{}: {} - {}".format(name,email,description))
        data[name] = [email,description]
    except:
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong'))
            WebDriverWait(driver, timeout).until(element_present)
            name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong').text
            email = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[2]/dl/dd[2]/a[1]').text # individual Email
            print("Description Not collected")
            print(name, email)
            data[name] = [email]
        except:
            try:
                element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong'))
                WebDriverWait(driver, timeout).until(element_present)
                name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong').text
                data[name] = 'null'
            except:
               print("Exception Thrown at iteration: {}".format(i))
            
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/a[3]'))
    WebDriverWait(driver, timeout).until(element_present)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div/a[3]').click()
    
    i+=1

df = pd.DataFrame.from_dict(data, orient='index')
df.to_excel("StanfordAlumniGa.xls")
print(data)
driver.quit()



#/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p title

#/html/body/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[2]/dl/dd[3]/a[1]



#  driver.get('https://alumni.stanford.edu/get/page/groups/members/?schools=ABCDEGHZ&sort=lastname&group_id=0038990756&p=1')
#        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table[{}]/tbody/tr/td[2]/h5/a'.format(i)))
#        WebDriverWait(driver, timeout).until(element_present)
#        


    
#for i in range(2,21):
#    i = str(i)
#    person = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table['+ i +']/tbody/tr/td[2]/h5/a')
#    person.click()
#    driver.find_element_by_xpath("//body").click()
#    print(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong').text) #finds name
#    print(driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[2]/dl/dd[2]/a[1]').text) # finds email
#    driver.get('https://alumni.stanford.edu/get/page/groups/members/?schools=ABCDEGHZ&sort=lastname&group_id=0038990756&p=1')
#    



#works:
#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/table[7]/tbody/tr/td[2]/h5/a').click() #selects the individual
#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[2]/dl/dd[2]/a[1]').text # individual Email
#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div[1]/div/div/div[1]/p/strong').text # individual name

#driver.get('url')
#timeout = 5
#try:
#    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
#    WebDriverWait(driver, timeout).until(element_present)
#except TimeoutException:
#    print "Timed out waiting for page to load"
