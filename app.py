from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/', methods=['POST'])
def handling():
    data = request.get_json()
    user = data.get('username')
    pword = data.get('password')

    driver = webdriver.Chrome()
    try:
        driver.get("https://www.linkedin.com/login")

        time.sleep(5)

        username = driver.find_element(By.ID, "username")
        username.send_keys(user)

        password = driver.find_element(By.ID, "password")
        password.send_keys(pword)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    finally:
        driver.quit

if __name__ == '__main__':
    app.run()