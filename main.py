from bs4 import BeautifulSoup
import csv


# Read
f = open('./input.html', "r", encoding="utf-8")
data = f.read()
f.close()

# Write
f = open("out.csv", "w", encoding="utf-8", newline="\n")
writer = csv.writer(f)

# Right-to-left should be opposite index to read properly (last index = first index)
header = [None, None, None, None, None]
header[0] = "מחיר למטר"
header[1] = "נרשמים בהגרלה"
header[2] = "דירות בהגרלה"
header[3] = "ישוב"
header[4] = "מספר הגרלה"
writer.writerow(header)


def append_to_csv(data):
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
    x4 = soup.findAll(lambda tag: tag.name == "td" and
                       "data-title" in tag.attrs and
                       tag.attrs["data-title"] == "נרשמים בהגרלה")
    x5 = soup.findAll(lambda tag: tag.name == "td" and
                       "data-title" in tag.attrs and
                       "מחיר למטר" in tag.attrs["data-title"].strip())

    x1 = list(map(lambda x: x.text.strip(), list(x1)))
    x2 = list(map(lambda x: x.text.strip(), list(x2)))
    x3 = list(map(lambda x: x.text.strip(), list(x3)))
    x4 = list(map(lambda x: x.text.strip().replace(',', ''), list(x4)))

    def extract_mehir_le_meter(x):
        x = x.div.text.strip().replace('₪', '').replace("*", "").replace(",", "")
        x = x.split(".")[0]
        return x

    x5 = list(map(extract_mehir_le_meter, list(x5)))

    for _x1, _x2, _x3, _x4, _x5 in zip(x1, x2, x3, x4, x5):
        # Hebrew = Reverse indexes
        writer.writerow([_x5, _x4, _x3, _x2, _x1])

append_to_csv(data)


f2 = open('./input2.html', "r", encoding="utf-8")
data2 = f2.read()
f2.close()
append_to_csv(data2)


f.close()