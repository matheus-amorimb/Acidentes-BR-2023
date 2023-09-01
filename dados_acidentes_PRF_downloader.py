import requests
from bs4 import BeautifulSoup
import zipfile
import os
import datetime
from tqdm import tqdm

def get_dados_acidentes_PRF_BR(ano_inicial_download = 0, ano_final_download = datetime.datetime.now().year, anos_download = [] ):

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
    
    if ano_inicial_download != 0:
        anos_to_download = range(ano_inicial_download, ano_final_download + 1, 1)

    elif len(anos_download) > 0:
        anos_to_download = [int(i) for i in anos_download]

    else:
        anos_to_download = anos
    
    
    years_download = [links_download[anos.index(ano)] for ano in anos_to_download]
    
    for link_download in tqdm(years_download):

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
    get_dados_acidentes_PRF_BR(2007, 2012)