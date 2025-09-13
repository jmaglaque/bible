import sqlite3
import json

# Input and output files
bblx_file = "RTPV.bblx"   # make sure this file is in the same folder
output_file = "rtpv.json"

# Book number → Book name (Tagalog / RTPV order)
# If your translation uses different book names, update this list accordingly.
# Standard Protestant 66 books
book_names = [
    "Genesis", "Exodo", "Levitico", "Mga Bilang", "Deuteronomio",
    "Josue", "Mga Hukom", "Ruth", "1 Samuel", "2 Samuel",
    "1 Mga Hari", "2 Mga Hari", "1 Cronica", "2 Cronica", "Ezra",
    "Nehemias", "Esther", "Job", "Mga Awit", "Mga Kawikaan",
    "Ecclesiastes", "Awit ng mga Awit", "Isaias", "Jeremias", "Panaghoy",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadias", "Jonas", "Mikas", "Nahum", "Habakuk",
    "Zefanias", "Hagay", "Zacarias", "Malakias",
    "Mateo", "Marcos", "Lucas", "Juan", "Mga Gawa",
    "Roma", "1 Corinto", "2 Corinto", "Galacia", "Efeso",
    "Filipos", "Colosas", "1 Tesalonica", "2 Tesalonica", "1 Timoteo",
    "2 Timoteo", "Tito", "Filemon", "Hebreo", "Santiago",
    "1 Pedro", "2 Pedro", "1 Juan", "2 Juan", "3 Juan",
    "Judas", "Pahayag"
]

# Connect to SQLite
conn = sqlite3.connect(bblx_file)
cur = conn.cursor()

# Prepare JSON structure
bible = {}

for i, book_name in enumerate(book_names, start=1):
    bible[book_name] = {}
    # get all verses for this book
    cur.execute("SELECT Chapter, Verse, Scripture FROM Bible WHERE Book=? ORDER BY Chapter, Verse", (i,))
    rows = cur.fetchall()
    for chapter, verse, text in rows:
        chapter = str(chapter)
        if chapter not in bible[book_name]:
            bible[book_name][chapter] = []
        # Append verse text
        bible[book_name][chapter].append(text)

# Save as JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(bible, f, ensure_ascii=False, indent=2)

print(f"Done! Exported Bible to {output_file}")
