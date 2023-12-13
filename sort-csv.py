import csv

with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
    conj_list = csv.DictReader(conj_csv) # really a list of dicts
    # fieldnames are the first row of the csv file so don't need to be provided
    sorted_conj = sorted(conj_list, key=lambda row: row["Ref."])
    from pprint import pprint; pprint(sorted_conj)

with open("attested-conjectures.csv", "w", encoding="utf8") as conj_csv:
    fieldnames = "Ref.,Paradosis,Conjecture,Author,Year,Attested Place,Rem.".split(",")
    writer = csv.DictWriter(conj_csv, fieldnames)
    writer.writeheader()
    writer.writerows(sorted_conj)