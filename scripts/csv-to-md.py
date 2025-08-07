# © 2023. This program is free software: you can
# redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/gpl-3.0.txt

import csv
import csv_tools
import operator

# read preface so that we can keep it before the table
preface_lines = []
with open("README.md", "r", encoding="utf8") as readme:
    for line in readme.readlines():
        preface_lines.append(line)
        if "<!-- Anything" in line:  # 2nd line because we need to keep the line with comment in
            break

csv_tools.sort_grc()

csv_tools.sort_lat()

with open("greek.csv", "r", encoding="utf8") as greek_csv:
    with open("latin.csv", "r", encoding="utf8") as latin_csv:
        with open("biblical.csv", "r", encoding="utf8") as amst_csv:
            # use league ranking to make top 10 sentence in preface
            league = csv_tools.create_league_table(
                (greek_csv, latin_csv, amst_csv))
            top_10 = sorted(
                league.items(), key=operator.itemgetter(1), reverse=True)
            limit = 9  # keep ties for 10th
            tie = False
            while top_10[limit][1] == top_10[limit+1][1]:  # [1] to access the actual score
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
            with open("README.md", "w", encoding="utf8") as conj_md:  # WARNING: rewrites the file!
                conj_md.writelines(preface_lines)
                conj_md.write("\n")
                # first line is headers
                first_first_row = True
                for reader in (greek_reader, latin_reader, amst_reader):
                    first_row = True
                    for row in reader:
                        if first_row and not first_first_row:
                            first_row = False
                            continue
                        # [:-1] to remove the unneeded | at the end
                        new_row = "".join(col + "|" for col in row)[:-1] + "\n"
                        conj_md.write(new_row)
                        if first_first_row:
                            delimiter_row = "---|" * (len(new_row.split("|")))
                            # [:-1] as above
                            delimiter_row = delimiter_row[:-1] + "\n"
                            conj_md.write(delimiter_row)
                            first_first_row = False
                            # delimiter needs to be written after headers (which are the first row)
                            first_row = False
