import subprocess
import sys



try:
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' ,'requirements.txt'])
finally:
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import requests
    from collections import deque

print("=====================================")



options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(chrome_options = options, executable_path = "/Users/roy/Documents/codeforfun/scraper/chromedriver")

### create new url request
url = input("Enter a URL to:")

# with open('res.xml', 'w') as f:
#     f.write(driver.page_source)
driver.get(url)
visited = set()
visited.add(url)

unvisited = set()


with open("result.txt", "w") as f: 
    elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
    for elem in elems:
                #retrieve all href links and save it to url_element variable
        url_element = elem.get_attribute("href")
        if (url_element not in visited) and (url_element not in unvisited):
            unvisited.add(url_element)
            f.write(str(url_element) + "\n")
    
    
    while len(unvisited) > 0:
        x = unvisited.pop()
        driver.get(x)
        visited.add(x)
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
        for elem in elems:
            #retrieve all href links and save it to url_element variable
            url_element = elem.get_attribute("href")
            if (url_element not in visited) and (url_element not in unvisited):
                unvisited.add(url_element)
                f.write(str(url_element) + "\n")

        