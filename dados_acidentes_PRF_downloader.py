import requests
from bs4 import BeautifulSoup
import zipfile
import os

def get_dados_acidentes_PRF_BR(ano = 0):
    url = "https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf"
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for HTTP errors

    site = BeautifulSoup(response.text, "html.parser")
    tables = site.find_all("table", class_ = "plain")
    
    links_download = []
    anos = [ano for ano in range(2023, 2006, -1)]

    for table in tables:
        for cell in table.find_all("td"):
            if "(Agrupados por ocorrência)" in cell.text:
                link_tag = cell.find_next("a",  href=True)
                links_download.append(link_tag["href"])
    
    if ano != 0:
        years_download = [links_download[anos.index(ano)]]

    for link_download in years_download:

        file_id = link_download.split("/")[5]
        download_url = f"https://drive.google.com/u/0/uc?id={file_id}&export=download"

        download_request = requests.get(download_url)
        download_request.raise_for_status()

        local_filename = "downloaded_file.zip"

        with open(local_filename, "wb") as file:
            file.write(download_request.content)

        with zipfile.ZipFile(local_filename, "r") as zip_ref:
            zip_ref.extractall(os.getcwd() + "\data")
        
        os.remove(local_filename)

if __name__ == "__main__":
    get_dados_acidentes_PRF_BR(2023)