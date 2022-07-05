from bs4 import BeautifulSoup
import csv

# Read
f = open("abc.html", "r")
data = f.read()
f.close()

# Write
f = open("out.csv", "w")
writer = csv.writer(f)

# Right-to-left should be opposite index to read properly (last index = first index)
first_row = [None, None, None]
first_row[2] = "מספר הגרלה"
first_row[1] = "ישוב"
first_row[0] = "דירות בהגרלה"
writer.writerow(first_row)

# Parse
soup = BeautifulSoup(data, "html.parser")
all = soup.findAll("td")
x1 = soup.findAll(lambda tag: tag.name == "td" and
                   "data-title" in tag.attrs and
                   tag.attrs["data-title"] == "מספר הגרלה")
x2 = soup.findAll(lambda tag: tag.name == "td" and
                   "data-title" in tag.attrs and
                   tag.attrs["data-title"] == "יישוב")
x3 = soup.findAll(lambda tag: tag.name == "td" and
                   "data-title" in tag.attrs and
                   tag.attrs["data-title"] == "דירות בהגרלה")

x1 = list(map(lambda x: x.text, list(x1)))
x2 = list(map(lambda x: x.text, list(x2)))
x3 = list(map(lambda x: x.text, list(x3)))


writer.writerows([list(x1), list(x2)])
#writer.writerows(list(x2))

#writer.writerows(list(x3))

print(x1)

f.close()