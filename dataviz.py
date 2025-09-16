import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Charger le CSV
df = pd.read_csv("results.csv", sep=",", on_bad_lines="skip", engine="python")


# =============================
# 1. Totaux par mot
# =============================
totals = df.drop(columns=["Fichier"]).sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
totals.plot(kind="bar")
plt.title("Total des occurrences par mot (tous les PDF)")
plt.ylabel("Occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# =============================
# 2. Comparaison par fichier
# =============================
df.set_index("Fichier").T.plot(kind="bar", figsize=(14,7))
plt.title("Comparaison des mots par fichier")
plt.ylabel("Occurrences")
plt.xlabel("Mots")
plt.xticks(rotation=90)
plt.legend(title="Fichier")
plt.tight_layout()
plt.show()

# =============================
# 3. Heatmap
# =============================
plt.figure(figsize=(14,7))
sns.heatmap(df.set_index("Fichier"), cmap="YlGnBu", annot=False)
plt.title("Heatmap des occurrences par mot et par fichier PDF")
plt.xlabel("Mots")
plt.ylabel("Fichiers")
plt.tight_layout()
plt.show()

# =============================
# 3. Clustered Bar Chart
# =============================

wordcloud = WordCloud(width=1200, height=600, background_color="white").generate_from_frequencies(totals.to_dict())

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud - Fréquence des mots")
plt.show()

plt.figure(figsize=(8,8))
plt.pie(totals, labels=totals.index, autopct="%1.1f%%", startangle=140, wedgeprops=dict(width=0.4))
plt.title("Répartition des mots (tous fichiers confondus)")
plt.tight_layout()
plt.show()

