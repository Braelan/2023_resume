from selenium import webdriver
import time
driver  = webdriver.Safari()
driver.get("https://www.google.com")
driver.implicitly_wait(10) #wait for 10 seconds before throwing an exception
#open_case  uses the selenium browser to open the case careers website
#it then applies to every job listed on the site
#it then opens the case careers website for each job
#it then applies to the job
#it then closes the case careers website
#it then closes the browser
def open_case():
    driver.get("https://whitecase.taleo.net/careersection/wc_external/jobsearch.ftl?lang=en")
    time.sleep(15)
    driver.implicitly_wait(10)
    #driver.implicitly_wait(10)
    #driver.find_element_by_id("text-input-what").send_keys("software engineer")
    #driver.find_element_by_id("text-input-where").send_keys("New York")
    #driver.find_element_by_id("whatWhereFormSubmit").click()
    #driver.implicitly_wait(10)
    #driver.find_element_by_id("text-input-what").send_keys("software engineer")
    #driver.find_element_by_id("text-input-where").send_keys("New York")
    #driver.find_element_by_id("whatWhereFormSubmit").click()
    #driver.implicitly_wait(10)
    #driver.find_element_by_id("text-input-what").send_keys("software engineer")
    #driver.find_element_by_id("text-input-where").send_keys("New York")
    #driver.find_element_by_id("whatWhereFormSubmit").click()
open_case()



