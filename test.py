from scraper.config import default_driver_path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager(path=default_driver_path()).install())
