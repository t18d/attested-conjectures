import csv

with open("attested-conjectures.csv", "r") as conj_csv:
    conj_reader = csv.reader(conj_csv)
    with open("attested-conjectures.md", "w") as conj_md: # WARNING: rewrites the file!
        #first line is headers
        first_row = True
        for row in conj_reader:
            new_row = "".join(col + "|" for col in row)[:-1] +"\n" # [:-1] to remove the unneeded | at the end
            conj_md.write(new_row)
            if first_row:
                delimiter_row = "---|" * (len(new_row.split("|")))  
                delimiter_row = delimiter_row[:-1] + "\n" # [:-1] as above
                conj_md.write(delimiter_row)
                first_row = False # delimiter needs to be written after headers (which are the first row)
        conj_md.write("\n") # for good markdown