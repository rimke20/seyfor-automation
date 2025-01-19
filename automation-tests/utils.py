import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from variables import *


def get_to_login(driver):
    enter = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[text()='Vstopite v program']")))
    enter.click()


def login(driver):
    email_field = driver.find_element(By.XPATH, "//input[@id='Email']")
    email_field.click()
    email_field.send_keys(user)
    email_field.send_keys(Keys.RETURN)
    password_field = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='Password']")))
    password_field.click()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


def new_invoice(driver):
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='header-shortcuts']")))
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    issued_invoice = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[normalize-space(text())='Izdani račun']")))
    issued_invoice.click()


def add_new_buyer(driver):
    new_buyer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='PPC_EPC_DC_I_StrankaID_bn']/span")))
    new_buyer.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@au-target-id='285']")))
    company_title = driver.find_element(
        By.XPATH, "//input[@au-target-id='285']")
    company_title.click()
    company_title.send_keys(company_name)
    address = driver.find_element(By.XPATH, "//input[@au-target-id='288']")
    address.click()
    address.send_keys(company_address)
    postal_number = driver.find_element(
        By.XPATH,
        "//*[@id='stranka_osnovni_podatki']/osnovni-podatki/div/fieldset[2]/div/div[4]/mm-posta-selector/div/div[1]/div/div/input")
    postal_number.click()
    postal_number.send_keys(postal_code)
    time.sleep(1)
    postal_number.send_keys(Keys.RETURN)
    company_id = driver.find_element(
        By.XPATH,
        "//*[@id='stranka_osnovni_podatki']/osnovni-podatki/div/fieldset[3]/div/div[4]/div/div[1]/input")
    company_id.click()
    company_id.send_keys(id_number)
    save = driver.find_element(By.XPATH, "//button[@id='B_Shrani']")
    save.click()


def add_new_items(driver, item_name=None, item_type=None,
                  item_ddv=None, item_price=None, item_code=None):
    new_item = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='PPC_EPC_DC_I_ArtikelID_bn']/span")))
    new_item.click()
    time.sleep(2)
    new_item_name = driver.find_element(
        By.XPATH, "//input[@au-target-id='111']")
    new_item_name.click()
    new_item_name.send_keys(item_name)
    new_item_type = driver.find_element(
        By.XPATH,
        "//*[@id='artikel_osnovni_podatki']/osnovni-podatki/div/fieldset/div/div[4]/div/div/input")
    new_item_type.click()
    new_item_type.send_keys(item_type)
    new_item_type.send_keys(Keys.RETURN)
    time.sleep(1)
    new_item_ddv = driver.find_element(
        By.XPATH,
        "//*[@id='artikel_osnovni_podatki']/osnovni-podatki/div/fieldset/div/div[7]/div/div/input")
    new_item_ddv.click()
    new_item_ddv.send_keys(item_ddv)
    time.sleep(2)
    new_item_ddv.send_keys(Keys.RETURN)
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(item_price).perform()
    save = driver.find_element(By.XPATH, "//button[@id='B_Shrani']")
    save.click()


def add_items_to_invoice(driver, item_name):
    add_item = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='PPC_EPC_DC_I_ArtikelID']/div[1]/input")))
    add_item.click()
    add_item.send_keys(item_name)
    time.sleep(2)
    add_item.send_keys(Keys.RETURN)
    time.sleep(2)
    save = driver.find_element(
        By.XPATH, "//a[@id='PPC_EPC_DC_bVnosVrsticeIR']")
    save.click()
    time.sleep(5)


def issue_an_invoice(driver):
    issue_an_invoice = WebDriverWait(
        driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='PPC_EPB_bIzstavi']")))
    total_amount = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='PPC_EPC_DC_L_Summary_L_ZaPlaciloVDenarniEnoti']/parent::dd")))
    assert total_amount.text == formatted_total_price
    issue_an_invoice.click()
