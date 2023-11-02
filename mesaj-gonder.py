import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Kullanıcı adı ve şifrenizi girin
username = input("Kullanıcı adınızı giriniz: ")
password = input("Şifrenizi giriniz: ")
kisi = input("Kişinin linki: ")
mesaj = input("Yazılacak mesaj: ")

# Selenium tarayıcısını başlatın
driver = webdriver.Chrome()

# Instagram web sitesine gidin
driver.get("https://www.instagram.com/")

time.sleep(5)
# Kullanıcı adı ve şifre alanlarını bulun
username_input = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
password_input = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

# Kullanıcı adı ve şifreyi girin
username_input.send_keys(username)
password_input.send_keys(password)

# Giriş yap butonuna tıklayın
login_button = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
login_button.click()

# Oturum açmayı bekleyin
time.sleep(5)

driver.get(kisi)
time.sleep(2)
simdidegil_button = driver.find_element(By.XPATH, "//*[@class='_a9-- _a9_1']")
simdidegil_button.click()
time.sleep(2)
mesaj_input = driver.find_element(By.XPATH, "//*[@role='textbox' and @aria-label='Mesaj Gönder']")
mesaj_input.send_keys(mesaj)
time.sleep(2)
gonder_button = driver.find_element(By.XPATH, "//div[@role='button' and text()='Gönder']")
gonder_button.click()

