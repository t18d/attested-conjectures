import csv
import csv_tools
import operator

# read preface so that we can keep it before the table
preface_lines = []
with open("README.md", "r", encoding="utf8") as readme:
    for line in readme.readlines():
        preface_lines.append(line)
        if "</preface>" in line: # 2nd line because we need to keep the line with </preface> in
            break 
    
csv_tools.sort_csv()

with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:    
    with open("amsterdam-db.csv", "r", encoding="utf8") as amst_csv:        
        # use league ranking
        league = csv_tools.create_league_table((conj_csv, amst_csv))
        top_10 = dict(sorted(league.items(), key=operator.itemgetter(1), reverse=True)[:10])
        top_10_line = "The top 10 critics are "
        for i, critic in enumerate(top_10.keys()):
            top_10_line += f"{critic} ({top_10[critic]})"
            if i < 8:
                top_10_line += ", "
            elif i == 8:
                top_10_line += ", and "
            else:
                top_10_line += ".\n"
        # juggle the last few lines around
        preface_lines[-4] = top_10_line

# reopen files to create new readers
with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:    
    with open("amsterdam-db.csv", "r", encoding="utf8") as amst_csv:   
        conj_reader = csv.reader(conj_csv)
        amst_reader = csv.reader(amst_csv)
        with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
            conj_md.writelines(preface_lines)
            conj_md.write("\n")
            #first line is headers
            first_first_row = True
            for reader in (conj_reader, amst_reader):
                first_row = True
                for row in reader:
                    if first_row and not first_first_row:
                        first_row = False
                        continue
                    new_row = "".join(col + "|" for col in row)[:-1] +"\n" # [:-1] to remove the unneeded | at the end
                    conj_md.write(new_row)
                    if first_first_row:
                        delimiter_row = "---|" * (len(new_row.split("|")))  
                        delimiter_row = delimiter_row[:-1] + "\n" # [:-1] as above
                        conj_md.write(delimiter_row)
                        first_first_row = False
                        first_row = False # delimiter needs to be written after headers (which are the first row)

