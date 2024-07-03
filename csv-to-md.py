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
    
csv_tools.sort_grc()

csv_tools.sort_lat()

with open("greek.csv", "r", encoding="utf8") as greek_csv:    
  with open("latin.csv", "r", encoding="utf8") as latin_csv:
    with open("biblical.csv", "r", encoding="utf8") as amst_csv:        
        # use league ranking to make top 10 sentence in preface
        league = csv_tools.create_league_table((greek_csv, latin_csv, amst_csv))
        top_10 = sorted(league.items(), key=operator.itemgetter(1), reverse=True)
        limit = 9 # keep ties for 10th
        tie = False
        while top_10[limit][1] == top_10[limit+1][1]: # [1] to access the actual score
            limit += 1
            tie = True
        top_10 = dict(top_10[:limit+1])
        top_10_line = "<p>The top 10 critics are "
        for i, critic in enumerate(top_10.keys()):
            top_10_line += f"{critic} ({top_10[critic]})"
            if i < len(top_10)-2:
                top_10_line += ", "
            elif i == len(top_10)-2:
                top_10_line += " and "
            else:
                if tie:
                    top_10_line += f" (tied)"
                top_10_line += ".</p>\n"
        # juggle the last few lines around
        preface_lines[-3] = top_10_line

# reopen files to create new readers
with open("greek.csv", "r", encoding="utf8") as greek_csv:    
  with open("latin.csv", "r", encoding="utf8") as latin_csv:
    with open("biblical.csv", "r", encoding="utf8") as amst_csv:   
        greek_reader = csv.reader(greek_csv)
        latin_reader = csv.reader(latin_csv)
        amst_reader = csv.reader(amst_csv)
        with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
            conj_md.writelines(preface_lines)
            conj_md.write("\n")
            #first line is headers
            first_first_row = True
            for reader in (greek_reader, latin_reader, amst_reader):
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

