from urllib.request import urlopen
import re

url = "https://www.welt.de"
page = urlopen(url)
html = page.read().decode("UTF-8")
file = open("test.txt", "w")
file.write(html)
file.close()
#regex1 = "<h4 class=\"c-teaser__headline\" data-external=\"Teaser.Title\">"
regex1 = "<section class=\"c-stage c-stage--headlines\" data-external-stage-name=\"headlines\" data-layout=\"headlines\">"
regex2 = "</section>"
matches = re.findall(f"({regex1}.*{regex2})", html)
matches2 = re.search(regex2, html, re.IGNORECASE)

print(len(matches))
print(matches[0])