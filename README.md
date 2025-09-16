# 📖 Traitement par lot et Analyse des Textes Religieux  

## 🎯 Objectif du projet  
Ce projet a pour but de développer un pipeline permettant :  
- L’ingestion et le traitement **par lot** de corpus de textes religieux.  
- L’analyse **linguistique, statistique et thématique** de ces textes.  
- La mise en place d’outils pour la **visualisation des résultats**.  

## ⚙️ Fonctionnalités  
- 🔄 **Traitement par lot** : collecte et prétraitement automatique de fichiers textes.  
- 📝 **Nettoyage des données** : suppression des caractères spéciaux, normalisation et tokenisation.  
- 📊 **Analyse statistique** : fréquences des mots, cooccurrences, nuages de mots.  
- 🤖 **Analyse avancée (NLP)** :  
  - lemmatisation et racinisation (stemming)  
  - détection de thématiques (topic modeling)  
  - classification et regroupement des textes  
- 📈 **Visualisations interactives** (graphiques, nuages de mots, histogrammes).  

## 🛠️ Technologies utilisées  
- **Python** (Pandas, NumPy)  
- **NLTK / SpaCy** pour le NLP  
- **Matplotlib / Seaborn / Plotly** pour la visualisation  
- **Airflow** ou **scripts batch** pour l’orchestration  
- **Git & GitHub** pour la gestion de version  


## 🚀 Installation & Utilisation  
1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/tonUser/wordscount-analysis.git
   cd wordscount-analysis
python -m venv venv
source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows
pip install -r requirements.txt
./wordscount.sh
