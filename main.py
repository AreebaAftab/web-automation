#!/usr/bin/env python
# coding: utf-8

# In[28]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
import random
import os
from os.path import join
import time


# In[145]:


def main():
    #profile
    def generate_email(prefix='huks214+', domain='gmail.com'):
        random_part = ''.join(random.choice(string.ascii_lowercase + string.digits) 
                              for _ in range(10))

        return prefix + random_part + '@' + domain
    def createcv():
        name = os.path.join(os.getcwd(), "cv.txt")
        f= open(name,"w+")
        f.write("I am an experienced developer. I have graduated in computer science from xyz university.")
        f.close()
        return f

    driver= webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://talent.bcg.com/apply/Login?folderIdAuto=10020333&folderId1=10013666")
    register= driver.find_element_by_xpath("//*[@id='mainContent']/div/div/div[1]/div/div/a").click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/form/div[1]/div[4]/a")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    manual_entry= driver.find_element_by_xpath("//*[@id='mainContent']/form/div[1]/div[4]/a").click()
    WebDriverWait(driver, 2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    select= Select(driver.find_element_by_xpath("//*[@id='8039']"))
    select.select_by_value("1")
    driver.find_element_by_xpath("//*[@id='8040']").send_keys("John")
    driver.find_element_by_xpath("//*[@id='8041']").send_keys("John")
    driver.find_element_by_xpath("//*[@id='8042']").send_keys("Bill")
    driver.find_element_by_xpath("//*[@id='8043']").send_keys("Smith")
    select = Select(driver.find_element_by_xpath("//*[@id='8044']"))
    select.select_by_value("296")
    email = generate_email()
    driver.find_element_by_xpath("//*[@id='8045']").send_keys(email)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    driver.find_element_by_xpath("//*[@id='8047']").send_keys("Homealone2!")
    driver.find_element_by_xpath("//*[@id='8048']").send_keys("Homealone2!")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    driver.find_element_by_xpath("//*[@id='8050']").send_keys("2")
    driver.find_element_by_xpath("//*[@id='8051']").send_keys("Karachi")
    driver.find_element_by_xpath("//*[@id='8052']").send_keys("Sindh")
    driver.find_element_by_xpath("//*[@id='8053']").send_keys("74600")
    select = Select(driver.find_element_by_xpath("//*[@id='8054']"))
    select.select_by_value("167")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    driver.find_element_by_xpath("//*[@id='8055']").send_keys("03343434343")
    driver.find_element_by_xpath("//*[@id='9401_3483']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='9403_3482']").click()
    driver.find_element_by_xpath("//*[@id='8059-save']").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='5763']")))

    #location preference
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.3);")
    select = Select(driver.find_element_by_xpath("//*[@id='5763']"))
    select.select_by_value("234743")
    select = Select(driver.find_element_by_xpath("//*[@id='5764']"))
    select.select_by_value("234744")
    select = Select(driver.find_element_by_xpath("//*[@id='5766']"))
    select.select_by_value("234745")
    driver.find_element_by_xpath("//*[@id='8829']").send_keys("Abu Dhabi 80%, Amsterdam 15%, Athens 5%")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.7);")
    driver.find_element_by_xpath("//*[@id='9461_573']").click()
    driver.find_element_by_xpath("//*[@id='9463_573']").click()
    driver.find_element_by_xpath("//*[@id='fieldSpecContainer9464']/div/div/div/div[2]/span/span[1]/span/ul/span/input").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID,"li234743"))).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='5768']").send_keys("June"+Keys.RIGHT+"2019")
    driver.find_element_by_xpath("//*[@id='5771-next']").click()

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='6491_574']")))
    #eductaion
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);")
    driver.find_element_by_xpath("//*[@id='6491_574']").click()
    driver.find_element_by_xpath("//*[@id='6494_574']").click()
    driver.find_element_by_xpath("//*[@id='6539_35656427']").click()
    driver.find_element_by_xpath("//*[@id='10504_3672']").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    driver.find_element_by_xpath("//*[@id='select2-9149-20-0-container']").click()
    driver.find_element_by_class_name("select2-search__field").send_keys("a")
    time.sleep(2)
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    select = Select(driver.find_element_by_xpath("//*[@id='9149-5-0']"))
    select.select_by_value("274")
    driver.find_element_by_xpath("//*[@id='9149-11-0']").send_keys("June"+Keys.RIGHT+"2019")
    driver.find_element_by_xpath("//*[@id='9149-2-0']").send_keys("November"+Keys.RIGHT+"2019")
    select = Select(driver.find_element_by_xpath("//*[@id='9149-26-0']"))
    select.select_by_value("3344")
    select = Select(driver.find_element_by_xpath("//*[@id='9149-15-0']"))
    select.select_by_value("457209")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.9);")
    driver.find_element_by_xpath("//*[@id='select2-9149-16-0-container']").click()
    driver.find_element_by_class_name("select2-search__field").send_keys("a")
    time.sleep(2)
    driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//*[@id='9149-18-0']").send_keys("3.4")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    select = Select(driver.find_element_by_xpath("//*[@id='6501-1-0']"))
    select.select_by_value("22148377")
    element = driver.find_element_by_xpath("//*[@id='6501-2-0']")
    driver.execute_script("arguments[0].innerText = 'English'", element)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='6501-3-0']")))
    driver.find_element_by_xpath("//*[@id='6501-3-0']").send_keys("80")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.25);")
    select = Select(driver.find_element_by_xpath("//*[@id='6503-1-0']"))
    select.select_by_value("38623009")
    driver.find_element_by_xpath("//*[@id='6503-2-0']").send_keys("June"+Keys.RIGHT+"2019")
    driver.find_element_by_xpath("//*[@id='6503-3-0']").send_keys("November"+Keys.RIGHT+"2019")
    driver.find_element_by_xpath("//*[@id='6503-4-0']").send_keys("want this scholarship badly")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='6504-next']").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='7616']")))
    #employment
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2.2);")
    select = Select(driver.find_element_by_xpath("//*[@id='7616']"))
    select.select_by_value("35972608")
    select = Select(driver.find_element_by_xpath("//*[@id='6701-6-0']"))
    select.select_by_value("291")
    select = Select(driver.find_element_by_xpath("//*[@id='6701-17-0']"))
    select.select_by_value("3477")
    driver.find_element_by_xpath("//*[@id='6701-1-0']").send_keys("aa")
    select = Select(driver.find_element_by_xpath("//*[@id='6701-14-0']"))
    select.select_by_value("100775")
    driver.find_element_by_xpath("//*[@id='6701-2-0']").send_keys("Developer")
    driver.find_element_by_xpath("//*[@id='6701-8-0']").send_keys("Karachi/Pakistan")
    driver.find_element_by_xpath("//*[@id='6701-3-0']").send_keys("November"+Keys.RIGHT+"2018")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='6702-next']").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='6821']")))
    #Attachments
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.4);")
    select = Select(driver.find_element_by_xpath("//*[@id='6821']"))
    select.select_by_value("100328")
    select = Select(driver.find_element_by_xpath("//*[@id='6822']"))
    select.select_by_value("16403662")
    select = Select(driver.find_element_by_xpath("//*[@id='6824']"))
    select.select_by_value("32058921")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    a= createcv()
    driver.find_element_by_xpath("//*[@id='6829']").send_keys(os.getcwd()+"\\cv.txt")
    driver.find_element_by_xpath("//*[@id='6832']").send_keys(os.getcwd()+"\\cv.txt")
    driver.find_element_by_xpath("//*[@id='6834']").send_keys(os.getcwd()+"\\cv.txt")
    driver.find_element_by_xpath("//*[@id='6835']").send_keys(os.getcwd()+"\\cv.txt")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='6839-save']").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='9260_month']")))
    #personal details
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5.4);")
    select = Select(driver.find_element_by_xpath("//*[@id='9260_month']"))
    select.select_by_value("1")
    select = Select(driver.find_element_by_xpath("//*[@id='9260_day']"))
    select.select_by_value("23")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    select = Select(driver.find_element_by_xpath("//*[@id='9263-3-0']"))
    select.select_by_value("445")
    select = Select(driver.find_element_by_xpath("//*[@id='9263-2-0']"))
    select.select_by_value("354")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1.35);")
    driver.find_element_by_xpath("//*[@id='9276']").send_keys("8")
    driver.find_element_by_xpath("//*[@id='9277']").send_keys("Karachi")
    driver.find_element_by_xpath("//*[@id='9278']").send_keys("Sindh")
    driver.find_element_by_xpath("//*[@id='9279']").send_keys("72245")
    select = Select(driver.find_element_by_xpath("//*[@id='9280']"))
    select.select_by_value("818")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='9322-save']").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[1]/a[1]")))
    #review application
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")
    driver.find_element_by_xpath("//*[@id='mainContent']/div[1]/a[1]").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='preHeader']/div[2]/div[1]/div/span[3]/a")))
    driver.find_element_by_xpath("//*[@id='preHeader']/div[2]/div[1]/div/span[3]/a").click()
    driver.quit()
if __name__== "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[133]:





# In[ ]:





# In[ ]:





# In[62]:





# In[67]:





# In[ ]:





# In[119]:





# In[116]:





# In[114]:





# In[123]:





# In[132]:





# In[ ]:




