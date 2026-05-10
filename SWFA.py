import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

path = input("Add meg a .txt fájl nevét vagy elérési útját: ").strip()
file_path = Path(path)

if not file_path.exists():
    raise FileNotFoundError(f"Nem található a fájl: {file_path}")


# Megnyitjuk a beszédet és beolvassuk egyetlen nagy szövegként (string)
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# időbélyeget követő szövegeket elmentjük feldolgozásra (list)
pattern = r"\[.*? - .*?\]\s*\n\s*(.*?)(?=\n\n\[|\Z)"
rows = re.findall(pattern, content, flags=re.S)

# összefűzzük a listában tárolt szöveget egyetlen string-be a számoláshoz
full_text = " ".join(rows)

# Tisztítás
full_text = re.sub(r"\s+", " ", full_text)
full_text = re.sub(r"[,.!?;:\"\'-]", "", full_text).strip()
full_text = full_text.lower()

# vissza listába
words = full_text.split()
# titsztítás, nem kell a, az és, hogy, is, nem, egy
stopwords = {"a", "az", "és", "hogy", "is", "nem", "egy", "gracias", "vagy", "meg", "mert", "azt"}
words = [word for word in words if word not in stopwords]

# listából DataFrame, mentés 
df_words = pd.DataFrame(words, columns=["word"])

word_counts = ( 
    df_words["word"]
    .value_counts()
    .reset_index()
)
word_counts.columns = ["word", "count"]

uniq_word = df_words["word"].nunique()

# ábrázoljuk diagramon
plt.bar(word_counts["word"][:10], word_counts["count"][:10])
plt.xlabel("Szavak")
plt.ylabel("Előfordulás")
plt.title("Leggyakoribb szavak")
plt.xticks(rotation=45)
plt.show()