# Intentions d'achats en ligne
_Projet Python visant à créer un modèle d'apprentissage automatique pour prédire **l'intention des acheteurs en ligne**, ainsi qu'une API Django._

Pour commencer veuillez télécharger le dossier zip Online-shoppers-intention-prediction-master, fourni sur github et le dézipper.

### Visualisation du notebook Python
**1.** Ouvrir Jupyter.\
**2.** Ouvrir le dossier Online-shoppers-intention-prediction-master dans Jupyter.\
**3.** Ouvrir le fichier nommé "Online-shoppers-intention.ipynb".\
**4.** Vous pouvez visualiser le notebook.\
**5.** Vous pouvez également visualiser le fichier "Online-shoppers-intention.html" en l'ouvrant directement depuis le dossier.

### Installation de l'API
**1.** Ouvrir PyCharm.\
**2.** Ouvrir le dossier Online-shoppers-intention-prediction-master dans PyCharm.\
**3.** Ouvrir le fichier "requirements.txt".\
**4.** Ouvrir un terminal (dans PyCharm).\
**5.** Lancer toutes les commandes indiquées dans le fichier "requirements.txt" dans le terminal.\
**6.** Dans le terminal, pointer sur le dossier "apirest" en lançant la commande `cd apirest`.\
**7.** Puis, lancer la commande `python manage.py runserver`.\
**8.** Ouvrir l'url http://127.0.0.1:8000/admin/ dans un navigateur.\
 Entrer comme nom d'utilisateur "badji" et comme mot de passe "badji".\
_**Bienvenue sur l'API !**_

###### Créer des exemples de paramétrages
Sur l'API, vous pouvez créer des exemples de paramétrage.\
**1.** Cliquer sur "Add" situé à droite de "Online shoppers".\
**2.** Avec le formulaire, créer de nouveaux paramètres.

###### Obtenir une prédiction
**1.** Ouvrir maintenant Postman.\
**2.** Pour obtenir la liste des visiteurs enregistrés, faire une requête GET et mettre comme URL http://127.0.0.1:8000/shoppers. (La liste est la même que celle observable directement sur Django). \
**3.** Pour visualiser les exemples paramétrés, faire une requête GET et mettre comme URL http://127.0.0.1:8000/shopper/1 (faire varier la dernière valeur de 1 à autant d'exemples créés).\
**4.** Pour obtenir une prédiction, faire une requête sur POST et mettre comme URL http://127.0.0.1:8000/intention/ \
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

Dans la majorité des cas, le modèle prédit que le visiteur n'effectuera pas de transaction. Pour obtenir une prédiction positive, essayez saisir les informations d'une session pour laquelle le champ Revenue est à True dans le dataset fourni : online_shoppers_intention.csv.
