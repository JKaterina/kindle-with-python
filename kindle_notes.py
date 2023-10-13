import pandas as pd
import re

data = []
quote = ""

with open(r"My Clippings.txt", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()  # Remove leading/trailing whitespaces
    if line.startswith("- Your Highlight"):
        continue  # Skip the "Your Highlight" line
    elif line != "":
        if quote == "":
            quote = line  # Store the quote in the 'quote' variable
        else:
            match = re.match(r"^(.+)\s\((.+)\)$", line)
            if match:
                book_title = match.group(1)
                author = match.group(2)
                data.append([quote, book_title, author])
                quote = ""  # Reset the 'quote' variable

df = pd.DataFrame(data, columns=["quote", "book title", "author"])
print(df.head())

df.to_csv('my_kindle_clippings.csv', index = False)