from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    def get_products(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [element.text for element in elements]
        

        
