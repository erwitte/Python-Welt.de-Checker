from urllib.request import urlopen
import re

url = "https://www.welt.de"
page = urlopen(url)
html = page.read().decode("UTF-8")
file = open("test.txt", "w")
file.write(html)
file.close()
patternStart = "<section class=\"c-stage c-stage--headlines\" data-external-stage-name=\"headlines\" data-layout=\"headlines\">"
patternEnd = "</section>"
patternSearch = "title="
headlines = []
matchesArray = re.findall(f"({patternStart}.*{patternEnd})", html)
matches = matchesArray[0]
for i in range(6):
        indexOverwrite = re.search(patternSearch, matches).start()
        indexReadOut = re.search(patternSearch, matches).end()+1
        matches = matches[:indexOverwrite] + '?' + matches[indexOverwrite+1:]
        toAppend = ""
        #print(html[indexReadOut])
        while matches[indexReadOut] != '"':
            toAppend = toAppend + matches[indexReadOut]
            indexReadOut += 1
        #print(re.search(patternSearch, html))
        headlines.append(toAppend)
for w in headlines:
    print(w)