import re
import glob

for filename in glob.glob("*.md"):
    with open(filename, 'r', encoding='utf8') as myFile:
        data = re.findall(r'\+{3}(.*)\+{3}(.*)',str(myFile.read()),re.DOTALL)
        data_between_plus = data[0][0].split('\n')
        data_after_plus = data[0][1]
        for line in data_between_plus:
            if line.startswith("published"):
                publish_date = line.split("=")[1].split("T")[0].split('-')
                my_year_s = 'year = "' + str(publish_date[0]).strip() + '"'
                my_month_s = 'month = "' + str(publish_date[0]).strip() + '/' + str(publish_date[1]).strip() + '"'
    with open(filename, 'w', encoding='utf8') as myFile_toWrite:
        myFile_toWrite.write("+++" + data[0][0])
        myFile_toWrite.write(my_year_s + "\n" + my_month_s + "\n" + "+++")
        myFile_toWrite.write(data[0][1])