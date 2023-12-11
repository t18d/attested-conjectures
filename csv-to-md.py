import csv

PREFACE = """# attested-conjectures
A Database of Greek and Latin Conjectural Emendations Attested in MSS

A CSV version can be found [here](./attested-conjectures.csv).

"""

with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
    conj_reader = csv.reader(conj_csv)
    with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
        conj_md.write(PREFACE)
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
