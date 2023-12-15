import csv
import csv_tools

# read preface so that we can keep it before the table
preface_lines = []
with open("README.md", "r", encoding="utf8") as readme:
    for line in readme.readlines():
        preface_lines.append(line)
        if "</preface>" in line: # 2nd line because we need to keep the line with </preface> in
            break 
    
csv_tools.sort_csv()

with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
    conj_reader = csv.reader(conj_csv)
    with open("amsterstam-db.csv", "r", encoding="utf8") as amst_csv:
        amst_reader = csv.reader(amst_csv)
        with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
            conj_md.writelines(preface_lines)
            conj_md.write("\n")
            #first line is headers
            first_row = True
            for reader in (conj_reader, amst_reader):
                for row in reader:
                    new_row = "".join(col + "|" for col in row)[:-1] +"\n" # [:-1] to remove the unneeded | at the end
                    conj_md.write(new_row)
                    if first_row:
                        delimiter_row = "---|" * (len(new_row.split("|")))  
                        delimiter_row = delimiter_row[:-1] + "\n" # [:-1] as above
                        conj_md.write(delimiter_row)
                        first_row = False # delimiter needs to be written after headers (which are the first row)

