# © 2023. This work is openly licensed via CC BY-SA 4.0.
# You may obtain a copy of the License at 
#
#     https://creativecommons.org/licenses/by-sa/4.0/

import csv
from copy import copy
from datetime import datetime
import re
import os

fieldnames = "Ref.,Paradosis,Conjecture,Author,Year,Attested Place,Rem.".split(",")

# next two functions from https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside under CC-BY-SA 3.0 
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def human_sort_dict(row, column):
    "Provide a naturally-sorted key for the row of a DictReader."
    return natural_keys(row[column])

def sort_grc(file="greek.csv", column="Ref."):
    "Sorts the file given by the column provided."
    with open(file, "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv) # has to be forced into a list so that we can close the file
        # fieldnames are the first row of the csv file so don't need to be provided
        sorted_conj = sorted(conjj, key=lambda row: human_sort_dict(row, column)) # old key=lambda row: row[column]
    try:
        with open(file, "w", encoding="utf8", newline="") as conj_csv:
            writer = csv.DictWriter(conj_csv, fieldnames, lineterminator=os.linesep)
            writer.writeheader()
            writer.writerows(sorted_conj)
    except ValueError as e: # if the rows are wrong then occurs ValueError: dict contains fields not in fieldnames - need to save the data in that case
        with open(f"error{datetime.now().isoformat()}.txt", "w", encoding="utf8") as err_txt: # need date in case multiple errors occur
            err_txt.write(str(e))
            err_txt.write(sorted_conj) # save the data

def sort_lat(file="latin.csv", column="Ref."):
    "Sorts the file given by the column provided."
    with open(file, "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv) # has to be forced into a list so that we can close the file
        # fieldnames are the first row of the csv file so don't need to be provided
        sorted_conj = sorted(conjj, key=lambda row: human_sort_dict(row, column)) # old key=lambda row: row[column]
    try:
        with open(file, "w", encoding="utf8", newline="") as conj_csv:
            writer = csv.DictWriter(conj_csv, fieldnames, lineterminator=os.linesep)
            writer.writeheader()
            writer.writerows(sorted_conj)
    except ValueError as e: # if the rows are wrong then occurs ValueError: dict contains fields not in fieldnames - need to save the data in that case
        with open(f"error{datetime.now().isoformat()}.txt", "w", encoding="utf8") as err_txt: # need date in case multiple errors occur
            err_txt.write(str(e))
            err_txt.write(sorted_conj) # save the data


def format_ref_column():
    """
    Makes sure all references are properly spaced; does not work on the numbered part properly.
    Properly spaced references are of the type "Plu. Caes. 45.8".
    """
    with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
        conjj = csv.DictReader(conj_csv)
        # fieldnames are the first row of the csv file so don't need to be provided
        refs = (row["Ref."] for row in conjj)
        new_refs = {}
        for ref in refs: #TODO: make this remove spaces between numbers automatically
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
            writer = csv.DictWriter(conj_csv2, fieldnames)
            writer.writeheader()
            writer.writerows(new_conjj)

def create_league_table(csvs):
    """
    Creates a sorted dictionary of authors to how many entries they have in the table.
    Takes a list of open CSV files (not readers).
    """
    csv_readers = []
    for file in csvs:
        csv_readers.append(csv.DictReader(file))

    league = {} # Author : Total Conjectures
    for reader in csv_readers:
       for row in reader:
            if row["Author"] in league:
                league[row["Author"]] += 1
            else:
                league[row["Author"]] = 1
    return league


if __name__ == "__main__": # functions to be called when this file is run
    sort_csv("attested-conjectures copy.csv", "Ref.")
    #format_ref_column()
    #with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
     #   with open("amsterdam-db.csv", "r", encoding="utf8") as amst_csv:
      #      from pprint import pprint;pprint(create_league_table([conj_csv, amst_csv]))
