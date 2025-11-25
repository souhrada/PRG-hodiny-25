import json

with open("data.json", "r", encoding="utf-8") as f:
    kocka = json.load(f)

kocka["věk"] += 1

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(kocka, f, ensure_ascii=False, indent=4)

