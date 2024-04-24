# Portfolio Pauline

Ce projet consiste en un portfolio personnel avec un chatbot intégré alimenté par le service d'IA Azure OpenAI. Le portfolio est déployé sur Azure à l'aide de deux conteneurs Docker : un pour le backend et un pour le frontend.

## Fonctionnalités

- Présentation brève du profil de mon profil et de mes compétences de dev IA
- Intégration d'un chatbot permettant aux visiteurs de poser des questions sur mon profil.
- Collecte des feedbacks des utilisateurs sur les réponses du chatbot.

## Déploiement

Le déploiement sur Azure est automatisé à l'aide d'un workflow GitHub.

### Prérequis

- Compte Azure
- Compte GitHub

### Étapes de déploiement

1. Cloner le projet depuis GitHub.
2. Configurer les secrets GitHub pour l'accès à Azure et à l'API OpenAI.
3. Pousser les modifications vers la branche `dev` pour déclencher le déploiement.