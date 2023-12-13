import csv
from copy import copy
from datetime import datetime

def sort_csv(column="Ref."):
    "Sorts attested-conjectures.csv by the column provided."
    with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv) # has to be forced into a list so that we can close the file
        # fieldnames are the first row of the csv file so don't need to be provided
        sorted_conj = sorted(conjj, key=lambda row: row[column])
    try:
        with open("attested-conjectures.csv", "w", encoding="utf8", newline="") as conj_csv:
            fieldnames = "Ref.,Paradosis,Conjecture,Author,Year,Attested Place,Rem.".split(",")
            writer = csv.DictWriter(conj_csv, fieldnames)
            writer.writeheader()
            writer.writerows(sorted_conj)
    except ValueError as e: # if the rows are wrong then occurs ValueError: dict contains fields not in fieldnames - need to save the data in that case
        with open(f"error{datetime.now().isoformat()}.txt", "w", encoding="utf8") as err_txt: # need date in case multiple errors occur
            err_txt.write(str(e))
            err_txt.write(sorted_conj) # save the data


def format_ref_column():
    "Makes sure all references are properly spaced."
    with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv)
        # fieldnames are the first row of the csv file so don't need to be provided
        refs = (row["Ref."] for row in conjj)
        new_refs = {}
        for ref in refs:
            parts = ref.split(".")
            new_ref = ". ".join(parts)
            if "  " in new_ref:
                extra_space = new_ref.index("  ")
                new_ref = new_ref[0:extra_space] + new_ref[extra_space+1:]
            new_refs[ref] = new_ref

    with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv) # needs reopening before for some reason - #TODO: fix this
        new_conjj = []
        for row in conjj:
            old_ref = row["Ref."]
            row["Ref."] = new_refs[old_ref]
            new_conjj.append(row)

        with open("attested-conjectures.csv", "w", encoding="utf8", newline="") as conj_csv2:
            fieldnames = "Ref.,Paradosis,Conjecture,Author,Year,Attested Place,Rem.".split(",")
            writer = csv.DictWriter(conj_csv2, fieldnames)
            writer.writeheader()
            writer.writerows(new_conjj)

if __name__ == "__main__": # functions to be called when this file is run
    sort_csv("Ref.")
    format_ref_column()