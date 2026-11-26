WORD = "".join(
    chr(c) for c in (
        101, 110, 115, 104, 105, 116, 116, 105, 102,
        105, 99, 97, 116, 105, 111, 110,
    )
)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(WORD)
