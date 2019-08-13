from behave import given,then,when,step
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time 

driver=webdriver.Firefox()

@when(u'I login with username "senders mail" and password "password"')
def step_impl(context):
    
    driver.get("https://mail.google.com/mail")
    elem = driver.find_element_by_name("identifier")
    elem.send_keys("senders mail")
    elem = driver.find_element_by_class_name("CwaK9").click() 
    time.sleep(2)
    elem = driver.find_element_by_name("password")
    elem.send_keys("password")
    elem = driver.find_element_by_class_name("CwaK9").click()
    time.sleep(3)
    
    

@then(u'I should be on "Home" page')
def step_impl(context):
    pass
    time.sleep(4)
            

@when(u'I click on "Compose"')
def step_impl(context):
    driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()
    time.sleep(2)


@then(u'I should see "Message box"')
def step_impl(context):
    pass
    

@then(u'I enter username "receivers mail" in "Recipients box"')
def step_impl(context):
    driver.find_element_by_id(":pt").send_keys("receiversmail")
    
    

@then(u'I enter "Subject" in "Subject box"')
def step_impl(context):
    elem = driver.find_element_by_class_name("aoT").send_keys("Selenium Automation")
    
    

@then('I enter "Message" in "Message body"')
def step_impl(context):
    elem = driver.find_element_by_id(":qg").send_keys("Your message")
    time.sleep(2)
    
    

@when(u'I click on "Send"')
def step_impl(context):
    driver.find_element_by_xpath("/html[1]/body[1]/div[25]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[2]/div[1]").click()
    time.sleep(3)
    

@then(u'I see confirmation message')
def step_impl(context):
    pass
    
