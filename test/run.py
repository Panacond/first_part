# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://www.epam.com/insights"


driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds
driver.get(url)
driver.maximize_window()
selector="#main > div.content-container.parsys > div:nth-child(1) > section > div.section__wrapper.section--padding-no > div.detail-pages-filter > div > div.detail-pages-filter__top-panel.pinned-filter > div > div > span:nth-child(1) > div > div.selected-params > div.default-label"
driver.find_element(By.CSS_SELECTOR, selector).click()
selector="div[class='multi-select-filter validation-focus-target open'] li[data-index='3'] span"
assert driver.find_element(By.CSS_SELECTOR, selector)
selector="div[class='multi-select-filter validation-focus-target open'] li[data-index='4'] span::before"
assert driver.find_element(By.CSS_SELECTOR, selector)