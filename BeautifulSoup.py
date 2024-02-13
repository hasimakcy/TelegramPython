from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#BeatifulSoup = It allows you to access desired information by parsing HTML or XML 
#documents from any webpage in the format you want.
from bs4 import BeautifulSoup
import re
import time

driver = webdriver.Chrome()

url = 'Please paste the URL of the conversation from which you want to fetch messages on Telegram here.'

driver.get(url)


last_message_content = ""
last_message_time = ""


# Loop to retrieve all messages
while True:
    #We're using WebDriverWait while logging into Telegram because it needs time to 
    #load and fetch the necessary information.

    #wait.until(It waits for an element with the class 'text-content' to appear on the page.)
    wait = WebDriverWait(driver, 20)
    time.sleep(10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text-content')))
    
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    message_elements = soup.find_all('div', class_='text-content')
    for message_element in message_elements:
        content_text = message_element.text.strip()
        message_content = content_text[:-5].strip()
        message_time = content_text[-5:].strip()
                
        if message_content != last_message_content or message_time != last_message_time:
            print("Message Content:", message_content)
            print("Message Time:", message_time)

            last_message_content = message_content
            last_message_time = message_time

    driver.quit()
