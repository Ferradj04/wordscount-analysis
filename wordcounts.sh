#!/bin/bash

# Dossier courant (où se trouvent le script + les PDFs)
INPUT_DIR="./books/"
OUTPUT_FILE="results.csv"

# Liste des mots à chercher (séparés par des espaces)
WORDS=("Peace" "Love" "Responsibility" "Truth" "Justice" "Freedom" "Happiness" "Courage" "Compassion" "Wisdom")

# Initialiser le CSV avec en-têtes dynamiques
echo -n "Fichier" > "$OUTPUT_FILE"
for word in "${WORDS[@]}"; do
    echo -n ",$word" >> "$OUTPUT_FILE"
done
echo "" >> "$OUTPUT_FILE"

# Parcourir tous les PDFs du dossier courant
for file in "$INPUT_DIR"*.pdf; do
    if [ -f "$file" ]; then
        pdftotext "$file" temp.txt 2>/dev/null
        if [ -f temp.txt ]; then
            echo -n "$(basename "$file")" >> "$OUTPUT_FILE"
            for word in "${WORDS[@]}"; do
                COUNT=$(grep -o -i "$word" temp.txt | wc -l)
                echo -n ",$COUNT" >> "$OUTPUT_FILE"
            done
            echo "" >> "$OUTPUT_FILE"
            rm temp.txt
        else
            echo "Erreur lors de la conversion de $file"
        fi
    fi
done

echo "✅ Résultats sauvegardés dans $OUTPUT_FILE"
python dataviz.py
