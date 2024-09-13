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
import re

fn = "Ref.,Paradosis,Conjecture,Author,Year,Attested Place,Rem.".split(
    ",")  # fn for fieldnames
amst_csv = []
bad_lines = []
with open("amsterdam-db.txt", "r", encoding="utf8") as amst_txt:
    for line in amst_txt.readlines():
        # assumes every line is in the format REF X:Y [X] PARADOSIS ] CONJECTURE SCHOLAR (YEAR) ID
        # IDs should be in Rem. as links to https://ntvmr.uni-muenster.de/nt-conjectures?conjID={ID}
        # Ref. = REF X:Y [X]
        # note that a successful re.split returns an empty string at [0]
        # the following regex means that everything non-ref starts with a string
        results = re.split(
            r"([0-9]*\s*[A-Za-z]+\s[0-9]+:[0-9]+\s\[[0-9]+–*[0-9]*\])((?:\s.+)*\s\])((?:\s.+\.*)*)(\s[A-Za-z]+)(\s\(*[0-9]+\)*)(\scj[0-9]+)", line)
        if results[0] == '':
            ref, paradosis, conjecture, scholar, year, ID = results[1:-1]
            if "(" in year:
                year = year[2:-1]  # got to get rid of brackets
            new_line = {fn[0]: ref,
                        fn[1]: paradosis[1:-2],  # got to get rid of " ]"
                        fn[2]: conjecture[1:],
                        fn[3]: scholar[1:],
                        fn[4]: year,
                        fn[5]: "",  # no place in the txt file.
                        fn[6]: f"[{ID[1:]}](https://ntvmr.uni-muenster.de/nt-conjectures?conjID={ID[1:]})"}
            amst_csv.append(new_line)
        else:
            bad_lines.append(line)

# from pprint import pprint; pprint(amst_csv)
with open("amsterdam-db.csv", "w", encoding="utf8", newline="") as amst_csv_f:
    writer = csv.DictWriter(amst_csv_f, fieldnames=fn)
    writer.writerows(amst_csv)
    for line in bad_lines:
        amst_csv_f.write(line + "\n")
