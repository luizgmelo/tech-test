import os
import requests
from bs4 import BeautifulSoup
import zipfile

def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    print("Acessando o site...")
    page = access_website(url)

    if not page:
        print("Falha ao acessar o site")
        return

    print("Procurando anexos...")
    pdf_links = find_pdf_links(page.text)

    if not pdf_links:
        print("Nenhum anexo foi encontrado")
        return

    print(f"Encontrados {len(pdf_links)} anexos")

    print("Baixando arquivos...")
    downloaded_files = download_pdfs(pdf_links)

    if not downloaded_files:
        print("Falha ao baixar os arquivos")
        return

    print("Compactando arquivos...")
    zip_filename = "anexos_ans.zip"
    create_zip(downloaded_files, zip_filename)


def access_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return None


def find_pdf_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    pdf_links = []

    # Procurar por links que contenham "Aneno I" ou "Anexo II"
    for link in soup.find_all('a', href=True):
        href = link['href'].lower()
        text = link.get_text().lower()

        if 'anexo ii' in text and href.endswith('.pdf'):
            pdf_links.append(('Anexo_II.pdf', link['href']))
        elif 'anexo i' in text and href.endswith('.pdf'):
            pdf_links.append(('Anexo_I.pdf', link['href']))

    return pdf_links


def download_pdfs(pdf_links):
    downloaded_files = []

    try:
        for filename, url in pdf_links:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open(filename, 'wb') as f:
                f.write(response.content)

            downloaded_files.append(filename)
            print(f"Baixado arquivo {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {e}")

    return downloaded_files


def create_zip(file_list, zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in file_list:
                if os.path.exists(file):
                    zipf.write(file)
                    os.remove(file)
        return True
    except Exception as e:
        print(f"Erro ao criar arquivos ZIP: {e}")
        return False


if __name__ == "__main__":
    main()