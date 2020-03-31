import re
import glob
import io
for filename in glob.glob("*.md"):
    #print("Reading file : " + filename)
    with open(filename, 'r', encoding='utf8') as myFile:
        data = re.findall(r'\+{3}(.*)\+{3}(.*)',str(myFile.read()),re.DOTALL) #reading between +++ only
        #print (type(data))
        for file in data:
            data_lines = file[0].split('\n')
            data_after_plus = file[1] # after the frontmatter +++
            #print (data_after_plus)
            for line in data_lines:
                if line.startswith("published"):
                    publish_date = line.split("=")[1].split("T")[0].split('-')
                    year = publish_date[0].replace(" ", "") #remove white space
                    my_year_s = "year = \"%s" "\"" % year   # construct the string for year with = and ""
                    #print (my_year_s)
                    data_lines.insert(6,my_year_s) #inserting formated year into data
                    x = [publish_date[0],publish_date[1]] #Joing month and year in a string
            # note the [bracket we wasted with {}, that is dictoionary unsorted list
                    s = '/'
                    month = s.join(x).replace(" ", "")
                    my_month_s = "\nmonth = \"%s" "\"" % month
                    #print (my_month_s)
                    data_lines.insert(7,my_month_s) #inserting formated month into data
                    #print(data_lines)
                    #print(data_after_plus)
                    Frontmatter_delimiter = "+++" # Frontmatter_delimiter
                    #print (Frontmatter_delimiter)
					filename_write = filename_out
                    newfile = open(filename_write, 'w', encoding='utf8')
                    newfile.write(Frontmatter_delimiter + '\n')
                    newfile.write(data_lines)  # writing modified lines but loosing everything else 
                    newfile.write('\n' + Frontmatter_delimiter + '\n')
                    newfile.writelines(data_after_plus) # writing the content
                    newfile.close()
