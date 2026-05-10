# Speech Word Frequency Analyzer

Ez a projekt beolvas egy timestamp-el ellátott beszéd leirat file-t `MP_beszed.txt`, amit DaVinci Resolve Studioban generáltam AI transcription-nel.
Tisztítja a szöveget, kiszedi a speciális karaktereket és azokat a szavakat, amiket nem akarunk beleszámolni, majd vizuálisan megjeleníti a top10-et.

## Input format

```text
[00:00:31:33 - 00:00:34:19]
Magyarok, határon innen is túl!
```

## Features

- reads timestamped transcript text
- removes timestamps
- cleans punctuation
- lowercases text
- removes custom stopwords
- counts word frequencies with pandas
- plots top words with matplotlib
- types: sring, list, DataFrame