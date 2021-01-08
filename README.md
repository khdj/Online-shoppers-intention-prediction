# Intentions d'achats en ligne
_Projet Python visant à créer un modèle d'apprentissage automatique pour prédire **l'intention des acheteurs en ligne**, ainsi qu'une API Django._

### Visualisation du notebook Python
**1.** Télécharger le dossier zip Online-shoppers-intention-prediction-master, fourni sur github et le dézipper.\
**2.** Ouvrir Jupyter.\
**3.** Ouvrir le dossier Online-shoppers-intention-prediction-master dans Jupyter.\
**4.** Ouvrir le fichier nommé "Online-shoppers-intention.ipynb".\
**5.** Vous pouvez visualiser le notebook.\
**6.** Vous pouvez également visualiser le fichier "Online-shoppers-intention.html" en l'ouvrant directement depuis le dossier.

### Installation de l'API
**1.** Télécharger le dossier zip Online-shoppers-intention-prediction-master, fourni sur github et le dézipper.\
**2.** Ouvrir PyCharm.\
**3.** Ouvrir le dossier Online-shoppers-intention-prediction-master dans PyCharm.\
**4.** Ouvrir le fichier "requirements.txt".\
**5.** Ouvrir un terminal (dans PyCharm).\
**6.** Lancer toutes les commandes indiquées dans le fichier "requirements.txt" dans le terminal.\
**7.** Dans le terminal, pointer sur le dossier "apirest" en lançant la commande `cd apirest`.\
**8.** Puis, lancer la commande `python manage.py migrate`.\
**9.** Ouvrir un autre terminal (dans PyCharm).\
**10.** Dans le nouveau terminal, pointer sur le dossier "apirest" en lançant la commande `cd apirest`.\
**11.** Puis, lancer la commande `python manage.py runserver`.\
**12.** Ouvrir l'url http://127.0.0.1:8000/admin/ dans un navigateur.\
 Entrer comme nom d'utilisateur "badji" et comme mot de passe "badji".\
_**Bienvenue sur l'API !**_

###### Créer des exemples de paramétrages
Sur l'API, vous pouvez créer des exemples de paramétrage.\
**1.** Cliquer sur "Add" situé à droite de "Online shoppers intentionss".\
**2.** Avec le formulaire, créer de nouveaux paramètres.

###### Obtenir une prédiction
**1.** Ouvrir maintenant Postman.\
**2.** Pour visualiser les exemples paramétrés, se positionner sur GET et mettre comme URL http://127.0.0.1:8000/shoppers/1 (faire varier la dernière valeur de 1 à autant d'exemples créés).\
**3.** Pour obtenir une prédiction, se positionner sur POST et mettre comme URL http://127.0.0.1:8000/intention/ \
Cliquer sur Body >> JSON et entrer les paramètres désirés, sous la forme suivante:
```
{
    "Administrative": 0,
    "AdministrativeDuration": 0.0,
    "Informational": 0,
    "InformationalDuration": 0.0,
    "ProductRelated": 16,
    "ProductRelatedDuration": 953.5,
    "SpecialDay": 0.8,
    "Month": "May",
    "OperatingSystems": 2,
    "Browser": 2,
    "Region": 9,
    "VisitorType": "New_Visitor",
    "Weekend": false,
    "Revenue": null
}
```
**4.** Cliquer sur "Send" pour obtenir la prédiction.
