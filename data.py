fh = open("./STUDENT- 24-25 CSV.csv")

data = fh.readlines()

grades = {
    #"junior": [],
    #"middle": [],
    "high": []
}

#junior = ["I", "II", "III", "IV", "V"]
#middle = ["VI", "VII", "VIII"]
high = ["IX", "X", "XI", "XII"]

for i in data:
    tokens = i.split(",")

    #if tokens[3] in junior:
    #    grades["junior"].append(
    #        {"name":tokens[1], "jssid":tokens[0]}
    #    )
#
    #if tokens[3] in middle:
    #    grades["middle"].append(
    #        {"name":tokens[1], "jssid":tokens[0]}
    #    )

    if tokens[3] in high:
        grades["high"].append(
            {"name":tokens[1], "jssid":tokens[0], "class":tokens[3] + tokens[4]}
        )

#import json
#
#with open("students.json", "w") as dataFile:
#    dataFile.write(json.dumps(grades))
