# Intentions d'achats en ligne
_Projet Python visant à créer un modèle d'apprentissage automatique pour prédire **l'intention des acheteurs en ligne**, ainsi qu'une API Django._

## Contexte
_Nous avons travaillé sur le dataset Online Shoppers Purchasing Intention qui a été créé par C. Okan Sakar (Department of Computer Engineering, Faculty of
Engineering and Natural Sciences) et Yomi Kastro
(Inveon Information Technologies Consultancy and Trade)._ \
_Ce dataset présente des sessions Internet (interaction entre un site ou une application et un visiteur ayant chargé au moins une page)._ \
_En plus de différentes informations sur la session (exemples : région géographique, mois de visite, etc.), nous savons également si la session a abouti à un achat ou non._ \

## Problématique
_A partir des informations sur une session Internet, nous cherchons à prévoir si le visiteur va effectuer ou non un achat au cours de la session ouverte._

## Résultats
_Après avoir testé sur notre dataset différents modèles (KNeighbors Classifier, C-Support Vector Classification, Gradient Boosting Classifier et Random Forest), nous avons conclu que le modèle le plus performant est le Gradient Boosting Classifier qui donne un score de 0.85._ \
_Le meilleur modèle final est donc le Gradient Boosting Classifier (CLF) appelé avec les paramètres suivants :_

- *learning_rate : 0.1*
- *loss : deviance*
- *max_depth: 5*
- *min_samples_leaf: 2*
- *min_samples_split: 3*
- *n_estimators: 20*

_Ce que nous remarquons en observant les matrices de confusion, c'est que dû à la faible proportion des "Revenue = True" dans le dataset, les prédictions sont plutôt médiocres quand "Revenue = True". Ce phénomène se manifeste sur tous les modèles testés._

_Ensuite, nous avons créé un API sur Django, permettant de prédire si une session aboutira à un achat ou non avec les paramètres entrés par l'utilisateur._

## Instructions

Pour commencer veuillez télécharger le dossier zip Online-shoppers-intention-prediction-master, fourni sur github et le dézipper.

### Visualisation du notebook Python
**1.** Ouvrir Jupyter.\
**2.** Ouvrir le dossier Online-shoppers-intention-prediction-master dans Jupyter.\
**3.** Ouvrir le fichier nommé "Online-shoppers-intention.ipynb".\
**4.** Vous pouvez visualiser le notebook.\
**5.** Vous pouvez également visualiser le fichier "Online-shoppers-intention.html" en l'ouvrant directement depuis le dossier.

### Mise en place de l'API
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

Pour rappel, seules 15% des sessions de notre dataset aboutissent à un achat.\
Ainsi, dans la majorité des cas, le modèle prédit que le visiteur n'effectuera pas de transaction.\
Pour obtenir une prédiction positive, essayez de saisir les informations d'une session pour laquelle le champ Revenue est à True dans le dataset fourni : online_shoppers_intention.csv.

## Auteures

> Khadidiatou BADJI\
> Vayshnavi SIVARAJAH
