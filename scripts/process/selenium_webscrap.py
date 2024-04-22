from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import re

from bs4 import BeautifulSoup

import nltk




# Télécharger les modèles de tokenisation de phrases avant d'exécuter ce script
#nltk.download('punkt')


# Pour obtenir la langue du texte du lien URL, sous forme de code ISO 639-1
def extract_language_code(url):
    match = re.search(r'https://([a-z]+)\.wikipedia', url)
    if match:
        return match.group(1)
    else:
        return None








options = Options()
#options.headless = False
#options.headless = True


geckodriver_path = "/snap/bin/geckodriver"  # specifie le chemin vers mon geckodriver
driver_service = Service(executable_path=geckodriver_path)

driver = webdriver.Firefox(options=options, service=driver_service)

#driver.get('http://selenium.dev/')



urls = set()
langues = set()

# Liste de tuples [(url, langue)]
ensemble_tuple = set()


# URL de la page web à partir de laquelle on souhaite extraire le lien de redirection
url = 'https://en.wikipedia.org/wiki/Entropy_(information_theory)'
print(url)
urls.add(url)
langue = extract_language_code(url)
print(langue)
langues.add(langue)

t = (url, langue)
ensemble_tuple.add(t)




# Charger la page web
driver.get(url)


# Ici on a ouvert le navigateur et on a en disponibilité les liens des langues : à la place de cliquer tout de suite sur le 1er, pourquoi ne pas enregistrer tous les liens des langues qui nous intéresse dans une liste (ou ensemble pour éviter les doublons ?) ?
# Et comme ça, on fait le traitement pour la page en cours (pour un lien, on prend le texte), puis on le fera pour tous les liens de la liste ?
    #D'abord pour la page sur laquelle on est (anglais)
    # Puis avec une boucke while ou for
        # A chaque fois, on va charger la page avec `driver.get(url)`, en prenant comme `url` tous les liens de la liste les uns après les autres
            # on va chercher grâce à leur structure commmune, les textes de chaque langue, en enregistrant bien à chaque fois les langues
# Donc quand on est sur le dernier lien, s'il n'y a plus de lien suivant, alors on break et on sort de la boucle
# (Dans ce cas-là, même pas sur d'avoir besoin de Sélénium ?? Ceci dit, on peut toujours continuer avec)
# A chaque fois il faudra écrire le texte dans un fichier qui s'appellera `{nom de la langue}.txt` après l'avoir nettoyé au maximum (supprimer les choses inutiles (avec split ou autres ?))
# (Il faudra ensuite un autre script qui permettra de prendre tous les fichiers txt de textes de langue et de tout recopier dans un seul fichier texte avec toutes les textes divisés en phrases et étiquettées avec leur langue respective)
# Puis un autre script qui va prendre toutes les phrases pour créer 3 fichiers (entrainement, validation, ) avec une répartition des langues équivalente pour le fichier d'entrainement





# boucle while ou for pour répéter les instructions en dessous
# for i in range 100


wait = WebDriverWait(driver, 10)
# On va cliquer sur l'élément du menu déroulant qui va nous donner les langues disponibles qu'on va pouvoir prendre
bouton = driver.find_element(By.XPATH, '//*[@id="p-lang-btn-checkbox"]')
bouton.click()





#/html/body/div[1]/div[2]/div[2]/div/ul/li[4]/a

# Pour les elements f'/html/body/div[1]/div[2]/div[1]/div/ul/li[{i+1}]/a' avec i de 0 à 8 exclu
for i in range(8):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[1]/div/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[1]/div/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

for i in range(3):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[2]/div/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

for i in range(5):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

for i in range(5):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/ul[1]/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/ul[1]/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

for i in range(8):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/ul[2]/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[1]/ul[2]/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

# Pour les éléments f'/html/body/div[1]/div[2]/div[4]/div[2]/ul[1]/li[{i+1}]/a' et f'/html/body/div[1]/div[2]/div[4]/div[2]/ul[2]/li[{i+1}]/a' avec i de 0 à 8 exclu
for j in range(2):
    for i in range(8):
        # Attendre que le menu déroulant devienne visible
        wait = WebDriverWait(driver, 10)
        menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[2]/ul[{j+1}]/li[{i+1}]/a')))
        # Trouver le lien de redirection en utilisant XPath
        element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[4]/div[2]/ul[{j+1}]/li[{i+1}]/a')
        # Extraire l'URL du lien de redirection et la langue
        lien_redirection = element.get_attribute('href')
        urls.add(lien_redirection)
        langue = element.get_attribute('lang')
        langues.add(langue)
        t = (lien_redirection, langue)
        ensemble_tuple.add(t)

for j in range(2):
    for i in range(3):
        # Attendre que le menu déroulant devienne visible
        wait = WebDriverWait(driver, 10)
        menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[5]/div/ul[{j+1}]/li[{i+1}]/a')))
        # Trouver le lien de redirection en utilisant XPath
        element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[5]/div/ul[{j+1}]/li[{i+1}]/a')
        # Extraire l'URL du lien de redirection et la langue
        lien_redirection = element.get_attribute('href')
        urls.add(lien_redirection)
        langue = element.get_attribute('lang')
        langues.add(langue)
        t = (lien_redirection, langue)
        ensemble_tuple.add(t)


# Attendre que le menu déroulant devienne visible
wait = WebDriverWait(driver, 10)
menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[5]/div/ul[1]/li[4]/a')))
# Trouver le lien de redirection en utilisant XPath
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[5]/div/ul[1]/li[4]/a')
# Extraire l'URL du lien de redirection et la langue
lien_redirection = element.get_attribute('href')
urls.add(lien_redirection)
langue = element.get_attribute('lang')
langues.add(langue)
t = (lien_redirection, langue)
ensemble_tuple.add(t)


for i in range(4):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[6]/div/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[6]/div/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)


for j in range(2):
    for i in range(5):
        # Attendre que le menu déroulant devienne visible
        wait = WebDriverWait(driver, 10)
        menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[7]/div[1]/ul[{j+1}]/li[{i+1}]/a')))
        # Trouver le lien de redirection en utilisant XPath
        element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[7]/div[1]/ul[{j+1}]/li[{i+1}]/a')
        # Extraire l'URL du lien de redirection et la langue
        lien_redirection = element.get_attribute('href')
        urls.add(lien_redirection)
        langue = element.get_attribute('lang')
        langues.add(langue)
        t = (lien_redirection, langue)
        ensemble_tuple.add(t)


# Attendre que le menu déroulant devienne visible
wait = WebDriverWait(driver, 10)
menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[7]/div[1]/ul[1]/li[6]/a')))
# Trouver le lien de redirection en utilisant XPath
element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[7]/div[1]/ul[1]/li[6]/a')
# Extraire l'URL du lien de redirection et la langue
lien_redirection = element.get_attribute('href')
urls.add(lien_redirection)
langue = element.get_attribute('lang')
langues.add(langue)
t = (lien_redirection, langue)
ensemble_tuple.add(t)


for i in range(2):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[7]/div[2]/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[7]/div[2]/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)

for i in range(4):
    # Attendre que le menu déroulant devienne visible
    wait = WebDriverWait(driver, 10)
    menu_deroulant = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div[2]/div[8]/div/ul/li[{i+1}]/a')))
    # Trouver le lien de redirection en utilisant XPath
    element = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[8]/div/ul/li[{i+1}]/a')
    # Extraire l'URL du lien de redirection et la langue
    lien_redirection = element.get_attribute('href')
    urls.add(lien_redirection)
    langue = element.get_attribute('lang')
    langues.add(langue)
    t = (lien_redirection, langue)
    ensemble_tuple.add(t)


# '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p'


#ele = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p')

#menu_deroulant.click()

#continue # pour passer à l'itération suivante de la grande boucle for initiée tout en haut



#print(urls)
#print(len(urls))
#print(langues)
#print(len(langues))
print(ensemble_tuple)
print(len(ensemble_tuple))



titres = ['text', 'language_code']

# Ouvrir fichier tsv en écriture qui servira de corpus
with open('donnees.tsv', 'w') as fichier_tsv:
    fichier_tsv.write('\t'.join(titres) + '\n')
    # Capturer le contenu textuel, la langue, etc. et l'écrire dans un fichier csv
    for url, langue in ensemble_tuple:
        # Charger la page web
        driver.get(url)
        # Récuperer le contenu textuel
        # Récupérer le contenu des paragraphes par exemple !
        # /html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[1]/p[64]
        # Ou alors récuperer le contenu textuel de tout la page
            #  cf. ChatGPT Outils de Corpus Linguistique
        # Nettoyer le contenu textuel et séparer en phrases

        # Obtenir le code source HTML de la page
        page_source = driver.page_source

        # Utiliser BeautifulSoup pour analyser le code HTML
        soup = BeautifulSoup(page_source, 'html.parser')

        # Exclure le texte contenu dans les balises <img> et ses sous-balises
        for img in soup.find_all('img'):
            img.decompose()
        # Extraire le texte de la page et supprimer le contenu entre les accolades en spécifiant strip=True pour supprimer les espaces vides au début et à la fin du texte
        texte_de_la_page = re.sub(r'\{.*?\}', '', soup.get_text(strip=True))

        # Extraire tout le texte de la page
        #texte_de_la_page = soup.get_text()
        #print(texte_de_la_page)

        # Remplacer plusieurs sauts de ligne par un seul
        texte_de_la_page = re.sub(r'\n+', '\n', texte_de_la_page)
        # Remplacer plusieurs espaces par un seul
        texte_de_la_page = re.sub(r'\s+', ' ', texte_de_la_page)
        # Supprimer les motifs {\displaystyle ...}
        texte_de_la_page = re.sub(r'\{\displaystyle.+?\}', '', texte_de_la_page)
        # Supprimer les lignes avec un seul caractère
        texte_de_la_page = re.sub(r'(^|\n)[^\n]{1}(\n|$)', '\n', texte_de_la_page)
        #print(texte_de_la_page)

        # Segmenter le texte en phrases en utilisant NLTK
        liste_de_phrases = nltk.sent_tokenize(texte_de_la_page)
        print(liste_de_phrases)

        # Écrire dans un fichier tsv le texte avec leur langue (pour chaque ligne on a : le texte et sa langue correspondante, séparées par une tabulation)
        #fichier_tsv.write(f"{texte_de_la_page}\t{langue}\n")

        # Écrire phrases par phrases
        for phrase in liste_de_phrases :
            fichier_tsv.write(f"{phrase}\t{langue}\n")


# Fermer le navigateur
driver.quit()
