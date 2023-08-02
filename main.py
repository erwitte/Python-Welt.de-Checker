from urllib.request import urlopen
import re

url = "https://www.welt.de"
page = urlopen(url)
html = page.read().decode("UTF-8")
patternStart = "<section class=\"c-stage c-stage--headlines\" data-external-stage-name=\"headlines\" data-layout=\"headlines\">"
patternEnd = "</section>"
patternTitle = "title="
patternLink = "href="
headlines = []
matchesArray = re.findall(f"({patternStart}.*{patternEnd})", html)
matches = matchesArray[0]
print(matches)
indexOverwrite = re.search(patternLink, matches).start()
matches = matches[:indexOverwrite] + '?' + matches[indexOverwrite+1:]
for i in range(6):
        indexOverwrite = re.search(patternTitle, matches).start()
        indexReadTitle = re.search(patternTitle, matches).end()+1
        matches = matches[:indexOverwrite] + '?' + matches[indexOverwrite+1:]
        indexOverwrite = re.search(patternLink, matches).start()
        indexReadLink = re.search(patternLink, matches).end()+1
        matches = matches[:indexOverwrite] + '?' + matches[indexOverwrite+1:]
        titleAppend = ""
        linkAppend = "https://www.welt.de/"
        while matches[indexReadTitle] != '"':
            titleAppend += matches[indexReadTitle]
            indexReadTitle += 1
        headlines.append(titleAppend)
        while matches[indexReadLink] != '"':
            linkAppend += matches[indexReadLink]
            indexReadLink += 1
        headlines[i] += "\n Link: " + linkAppend
for w in headlines:
    print(w)