"""
Ce script utilise Selenium pour extraire des URLs de redirection et leurs langues
à partir d'une page Wikipedia donnée. Il télécharge ensuite le contenu de chaque page
extrait, nettoie le texte et le segmente en phrases, puis sauvegarde ces informations
dans un fichier TSV.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from bs4 import BeautifulSoup
import nltk

# Télécharger les modèles de tokenisation de phrases avant d'exécuter ce script
# nltk.download('punkt')

def setup_browser():
    """
    Configure et démarre le navigateur Firefox avec les options spécifiées.

    Returns:
        WebDriver: Instance de Firefox WebDriver configurée.
    """
    options = Options()
    geckodriver_path = "/snap/bin/geckodriver"
    driver_service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(options=options, service=driver_service)
    return driver

def extract_language_code(url):
    """
    Extrait le code de langue d'une URL Wikipedia.

    Args:
        url (str): L'URL de la page Wikipedia.

    Returns:
        str: Le code de langue ISO 639-1 extrait de l'URL, ou None si aucun code de langue n'est trouvé.
    """
    match = re.search(r'https://([a-z]+)\.wikipedia', url)
    return match.group(1) if match else None

def click_button_and_extract_links(driver, button_xpath, link_xpath_template, count):
    """
    Clique sur un bouton pour afficher un menu déroulant, puis extrait les liens et leurs langues.

    Args:
        driver (WebDriver): Instance du WebDriver.
        button_xpath (str): XPath du bouton à cliquer pour afficher le menu déroulant.
        link_xpath_template (str): Template XPath des liens de redirection.
        count (int): Nombre de liens à extraire.

    Returns:
        tuple: Un ensemble d'URLs, un ensemble de langues, et un ensemble de tuples (URL, langue).
    """
    urls = set()
    languages = set()
    tuples = set()
    wait = WebDriverWait(driver, 10)
    button = driver.find_element(By.XPATH, button_xpath)
    button.click()

    for i in range(count):
        wait = WebDriverWait(driver, 10)
        menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, link_xpath_template.format(i+1))))
        element = driver.find_element(By.XPATH, link_xpath_template.format(i+1))
        lien_redirection = element.get_attribute('href')
        langue = element.get_attribute('lang')
        urls.add(lien_redirection)
        languages.add(langue)
        tuples.add((lien_redirection, langue))

    return urls, languages, tuples

def extract_and_clean_text(driver, url):
    """
    Extrait et nettoie le texte d'une page web.

    Args:
        driver (WebDriver): Instance du WebDriver.
        url (str): L'URL de la page à extraire.

    Returns:
        str: Le texte nettoyé de la page.
    """
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    for img in soup.find_all('img'):
        img.decompose()

    texte_de_la_page = re.sub(r'\{.*?\}', '', soup.get_text(strip=True))
    texte_de_la_page = re.sub(r'\n+', '\n', texte_de_la_page)
    texte_de_la_page = re.sub(r'\s+', ' ', texte_de_la_page)
    texte_de_la_page = re.sub(r'\{\displaystyle.+?\}', '', texte_de_la_page)
    texte_de_la_page = re.sub(r'(^|\n)[^\n]{1}(\n|$)', '\n', texte_de_la_page)

    return texte_de_la_page

def main():
    """
    Fonction principale orchestrant l'exécution du script. Configure le navigateur,
    extrait les liens et les langues des pages Wikipedia, nettoie le contenu textuel
    de chaque page, et sauvegarde les données dans un fichier TSV.
    """
    driver = setup_browser()

    initial_url = 'https://en.wikipedia.org/wiki/Entropy_(information_theory)'
    urls = {initial_url}
    languages = {extract_language_code(initial_url)}
    tuples = {(initial_url, extract_language_code(initial_url))}

    driver.get(initial_url)

    xpaths = [
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div[1]/div/ul/li[{}]/a', 8),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div[2]/div/ul/li[{}]/a', 3),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div[3]/div/ul/li[{}]/a', 5),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div[4]/div/1/ul[1]/li[{}]/a', 5),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div[4]/div/1/ul[2]/li[{}]/a', 8),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/4/2/ul[{}]/li[{}]/a', 16),  # Assuming 2x8 elements
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/5/div/ul[{}]/li[{}]/a', 6),  # Assuming 2x3 elements
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/6/div/ul/li[{}]/a', 4),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/7/div/1/ul[{}]/li[{}]/a', 10),  # Assuming 2x5 elements
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/7/div/1/ul[1]/li[6]/a', 1),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/7/div/2/ul/li[{}]/a', 2),
        ('//*[@id="p-lang-btn-checkbox"]', '/html/body/div[1]/div[2]/div/8/div/ul/li[{}]/a', 4)
    ]

    for button_xpath, link_xpath_template, count in xpaths:
        new_urls, new_languages, new_tuples = click_button_and_extract_links(driver, button_xpath, link_xpath_template, count)
        urls.update(new_urls)
        languages.update(new_languages)
        tuples.update(new_tuples)

    with open('donnees.tsv', 'w') as fichier_tsv:
        fichier_tsv.write('text\tlanguage_code\n')
        for url, langue in tuples:
            texte_de_la_page = extract_and_clean_text(driver, url)
            liste_de_phrases = nltk.sent_tokenize(texte_de_la_page)
            for phrase in liste_de_phrases:
                fichier_tsv.write(f"{phrase}\t{langue}\n")

    driver.quit()

if __name__ == "__main__":
    main()
