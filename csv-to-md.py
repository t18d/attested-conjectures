import csv
# preface must be edited here for changes to stick
PREFACE = """# attested-conjectures
A Database of Greek and Latin Conjectural Emendations Attested in MSS

<details>
    <summary>Bibliography</summary>
    <ul>
        <li>P.Oxy.I,II,LXXXI</li>
        <li>James, Patrick. ‘Review of The Oxyrhynchus Papyri. Volume LXXXI.’ <i>The Classical Review</i> 68, no. 2 (2018): 395-398.</li>
        <li>Kenyon, Frederic George. <i>The Evidence of Greek Papyri with Regard to Textual Criticism.</i> London: Hernry Frowde, 1904.</li>
        <li>Wessely and Rzach, <i>Studien zur Palaeographie und Papyruskunde</i>, I (1901)</li>
        <li>Weil, <i>Revue de Philologie</i>, xiii. 179 (1882)</li>
        <li>Wilcken, <i>Sitzungsb. d. Berl. Akad.</i>, 1887 p. 807</li>
        <li>P.Louvre ed. Weil = Austin 42</li>
        <li>P.Münch.II.40 = Pap.graec.mon.89</li>
        <li>Papyrus Massiliensis</li>
    </ul>
</details>
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
