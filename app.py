from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handling():
    data = request.get_json()
    user = data.get('username')
    pword = data.get('password')
    link = data.get('link')

    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(5)

        username = driver.find_element(By.ID, "username")
        username.send_keys(user)

        password = driver.find_element(By.ID, "password")
        password.send_keys(pword)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)
        
        driver.get(link)

        return jsonify({"status": "success", "message": "Navigated to profile page"}), 200

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Current URL: {driver.current_url}")
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
