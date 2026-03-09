# Cyber-Security-Tools-Python
# 🔐 RSA Custom Engine - Python Implementation


## 📌 Présentation du Projet
Ce projet est une implémentation complète et "from scratch" de l'algorithme de chiffrement asymétrique **RSA**.

## 🚀 Fonctionnalités
* **Génération de clés** : Production de paires de clés (publique/privée) de 1024 à 2048 bits.
* **Moteur Arithmétique Optimisé** : Implémentation manuelle des piliers de RSA.
* **Interface Graphique (GUI)** : Interface moderne et intuitive réalisée avec `CustomTkinter`.
* **Sécurité** : Utilisation de tests probabilistes de primalité et d'exponentiation modulaire rapide.

## 🧠 Concepts Mathématiques Appliqués
Pour garantir la robustesse et la performance de l'outil, les algorithmes suivants ont été implémentés :
1.  **Test de Miller-Rabin** : Vérification de la primalité des grands nombres (k=40).
2.  **Algorithme d'Euclide Étendu** : Calcul du PGCD et des coefficients de Bézout.
3.  **Inverse Modulaire** : Détermination de l'exposant privé $d$.
4.  **Square and Multiply** : Exponentiation modulaire itérative pour éviter les dépassements de pile (RecursionError).



## 🛠 Installation & Utilisation

### Prérequis
* Python 3.11 ou supérieur
* Environnement virtuel recommandé

## LANCEMENT : 
python interface.py

si jamais vous rencontrer cette erreur UnicodeDecodeError: 'utf-8' codec can't decode byte 0xee in position 1: invalid continuation byte augmenter p = arithmetic.generate_prime(512)
                            q = arithmetic.generate_prime(512)


## Développé par Reymbaut - Étudiant en L3 Maths-Info & Freelance Cybersécurité sur Malt.