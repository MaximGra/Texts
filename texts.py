import os
text = []
texts_name = os.listdir("texts")
for name in texts_name:
    with open(f"texts/{name}", encoding="utf-8") as f:
        lines = f.readlines()
        count_line = str(len(lines))
        lines = ["\n" + name + "\n"] + [count_line + "\n"] + lines
        text.append(lines)

final_text = "".join(sum((sorted(text, key=len)), []))

with open("final_text.txt", "w", encoding="utf-8") as f:
    f.write(final_text)