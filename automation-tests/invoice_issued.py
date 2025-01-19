from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from variables import *
from utils import *


driver = None


def suite_setup():
    global driver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Optional: run Chrome in
    # headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(minimax_url)
    driver.maximize_window()
    get_to_login(driver)
    login(driver)
    new_invoice(driver)
    add_new_buyer(driver)
    for new_item, new_type, new_ddv, new_price in new_items:
        add_new_items(driver, new_item, new_type, new_ddv, new_price)
    for item_name in item_names:
        add_items_to_invoice(driver, item_name)
    issue_an_invoice(driver)


def teardown():
    driver.quit()


def check_invoice():
    global driver
    wait_for_invoice = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='PPC_VPC_ctl02_L_Summary_L_ZaPlaciloVDenarniEnoti1']")))
    total_amount = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/fieldset[3]/div[3]/div[2]/div/div/dl[5]/dd")))
    first_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[1]/tr/td[3]/div")))
    second_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[2]/tr/td[3]/div")))
    third_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[3]/tr/td[3]/div")))
    first_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[1]/tr/td[10]")))
    second_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[2]/tr/td[10]")))
    third_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='T_Vrstice']/tbody[3]/tr/td[10]")))
    assert wait_for_invoice.text == "Za plačilo (Transakcijski račun):"
    assert first_item.text.strip() == item_one_name
    assert second_item.text.strip() == item_two_name
    assert third_item.text.strip() == item_three_name
    assert first_item_price.text.strip() == item_one_price + ",00"
    assert second_item_price.text.strip() == item_two_price + ",00"
    assert third_item_price.text.strip() == item_three_price + ",00"
    assert total_amount.text == formatted_total_price


def check_invoice_pdf():
    global driver

    pdf_invoice = driver.find_element(
        By.XPATH, "//*[@id='File_Editor']/div/table/tbody/tr/td[2]/a")
    pdf_invoice.click()
    wait_for_invoice = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[17]")))
    total_amount = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[70]")))
    first_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[45]")))
    second_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[54]")))
    third_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[63]")))
    first_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[39]")))
    second_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[48]")))
    third_item_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='AttachmentPreview']/div[2]/div[2]/div/div[1]/span[57]")))
    assert wait_for_invoice.text == "RAČUN"
    assert first_item.text.strip() == item_one_name
    assert second_item.text.strip() == item_two_name
    assert third_item.text.strip() == item_three_name
    assert first_item_price.text.strip() == item_one_price + ",00"
    assert second_item_price.text.strip() == item_two_price + ",00"
    assert third_item_price.text.strip() == item_three_price + ",00"
    assert total_amount.text.strip() == formatted_total_price_no_eur


suite_setup()
check_invoice()
check_invoice_pdf()
teardown()
