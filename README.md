# Outils_Traitement_Corpus
Dépôt pour les devoirs du cours d'Outils de Traitement de Corpus de M1 TAL (PluriTAL)

## Séance 1 (18/03/2024)

### Devoir de la séance
- Tache que je veux réaliser : Détecter la langue d'un texte
- Un corpus qui répond à cette tache : https://huggingface.co/datasets/Mike0307/language-detection
- A quel typre de prédiction peut servir ce corpus :
    - Ce corpus peut servir à faire de la classification :
        - La langue est une variable catégorielle, et ce corpus peut servir à classifier chaque texte dans une catégorie de langue spécifique.
- A quel modèle il a servi :
    - Pour le moment, aucun modèle n'a utilisé ce corpus... Mais en vérifiant sur la page, on constate qu'il est tout récent (le premier commit datant du 21 décembre 2023) : peut-être que c'est en partie ce qui explique cela ?
- Informations sur ce corpus :
    - Auteur :
        - Pseudo :`Mike0307`
        - Lien du compte : https://huggingface.co/Mike0307
    - Taille : 7,86 MB de fichiers dataset convertis en fichier parquet, pour un total de 42 362 lignes
    - Création et mise à jour :
        - Création : le 21 décembre 2023
        - Dernière modification :
            - le 21 décembre 2023 sur la branche main
            - le 7 mars 2024 et le 23 février pour les autres branches (qui ont donc quelques commit d'avance qui n'ont pas été rappatriés sur le main)
        - Il y a donc peut-être eu création de ce corpus en amont, et le corpus a été déposé sur Hugging Face une fois considéré comme fini ? Ce qui expliquerait que tous les changements du main se soient faits le même jour
        - 3 branches :
            - la branche `main` avec 12 commits au total
            - une branche `refs/convert/duckdb` avec 20 commits
            - une branche `refs/convert/parquet` avec 20 commits
    - Dans quel but : le but n'est pas clairement précisé, mais d'après le titre du corpus, il doit être utilisé pour développer, entrainer et tester un modèle de détection de langue.
    - Langues : l'ensemble des langues n'est pas renseigné explicitement, mais vu la diversité des langues que l'on peut observer dans la Dataset Viewer mise à disposition (et dans le `language_code`), on a (avec leur proportion dans le corpus):
        - du portugais (9,9%),
        - du polonais (10,2%),
        - du russe (9,7%),
        - du néerlandais (9,8%),
        - de l'anglais (10,1%),
        - du mandarin taiwanais (10,1%),
        - de l'allemand (9,9%),
        - du français (10,1%),
        - de l'italien (9,9%),
        - de l'espagnol (10,4%)
        - On remarque qu'on a essayé d'avoir des proportions de langues relativement proche (avec une différence de proportion de l'ordre de 0,7 point de pourcentage) afin sûrement de ne pas biaiser les phases d'entrainement, de développement et de test
    - Description du corpus :
        - L'ensemble du corpus a été divisé en 3 parties :
            - Un corpus de développement (`dev` mais nommé ici `validate` ?) de 4 240 lignes
            - Un corpus d'entrainement `train` de 33 900 lignes
            - Un corpus de test `test` de 4 240 lignes
            - On remarque que la part du corpus `train` est très importante par rapport aux autres (environ  75% du total) et que les corpus `validate` et `test` ont la même taille et une proportion beaucoup plus petite (environ 12.5% chacun)
        - (EN COURS)
