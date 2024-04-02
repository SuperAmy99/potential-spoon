from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = 'https://www.vmo.nl/leden/'


# Replace 'path/to/your/webdriver' with the actual path to the WebDriver executable
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get(url)

# Locate the element you want to hover over


# find all the elements

elements = driver.find_elements(by=By.CSS_SELECTOR, value='div.member-item')

for element in elements[1:4]:

    # find the name in the element
    name = element.find_element(by=By.CSS_SELECTOR, value='.title-layer h3')
    print(name.text)


    button_to_click = element.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-quinary')
    print(button_to_click.text)
    click = ActionChains(driver).click(button_to_click)
    click.perform()

    # wait for the popup to appear
    driver.implicitly_wait(3)

    # inspect popup
    popup = driver.find_element(by=By.CSS_SELECTOR, value='div.member-popup')

    c_name = popup.find_element(by=By.CSS_SELECTOR, value='h2')
    print(c_name.text)

    specialism = popup.find_element(by=By.CSS_SELECTOR, value='.col-md-5 span')
    print(specialism.text)

    # close the popup
    close_button = popup.find_element(by=By.CSS_SELECTOR, value='button.mfp-close')
    # close_button.click()
    close_button_click = ActionChains(driver).click(close_button)
    close_button_click.perform()
    

# Hover over the element
# element_to_hover_over = driver.find_element(by=By.CSS_SELECTOR, value='div.member-item')
# hover = ActionChains(driver).move_to_element(element_to_hover_over)
# hover.perform()

# Remember to close the browser window when you're done
driver.quit()



