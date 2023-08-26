import requests
from bs4 import BeautifulSoup

def get_Acidentes_2023():
    url = "https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf"
    response = requests.get(url)
    response.status_code

    site = BeautifulSoup(response.text, "html.parser")
    #print(site.prettify())
    tables = site.find_all("table", class_ = "plain")
    
    links = []

    for table in tables:
        for indice, cell in enumerate(table.find_all("td")):
            if "(Agrupados por ocorrência)" in cell.text:
                link_tags = table.find_all("td")[indice+1].find("a",  href=True)
                links.append(link_tags["href"])
    
    
    response2 = requests.get(links[0])
    soup = BeautifulSoup(response2.text, "html.parser")

    buttons = soup.find_all('div', {'class': 'ndfHFb-c4YZDc-to915-LgbsSe'})

    for button in buttons:
        print(button)
        print("\n")

    from selenium import webdriver

    # Initialize the web driver (replace 'chromedriver_path' with the actual path to the driver)
    driver = webdriver.Chrome(executable_path='chromedriver_path')

    # Open the Google Drive link
    driver.get('https://drive.google.com/file/d/1-WO3SfNrwwZ5_l7fRTiwBKRw7mi1-HUq/view')

    # Find the "Download" button by its class name (you need to inspect the button element to get the correct class)
    download_button = driver.find_element_by_class_name('ndfHFb-c4YZDc-to915-LgbsSe')

    # Click the button to initiate the download
    download_button.click()

    # Close the browser window
    driver.quit()


get_Acidentes_2023()