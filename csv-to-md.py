import csv
import csv_tools
# preface must be edited here for changes to stick
PREFACE = """# Database of Greek and Latin Conjectural Emendations Attested in MSS

<details>
    <summary>Bibliography</summary>
    <h3>Methodology</h3>
    <ul>
        <li>James, Patrick, review of <em>The Oxyrhynchus Papyri. Volume LXXXI</em>, in <em>The Classical Review</em>, 68/2 (2018), 395-398 at 396.</li>
    </ul>
    <h3>Sources</h3>
    <ul>
        <li>P.Oxy.I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XIII, XV, XVII, LXXXI</li>
        <li>Borges, Cassandra, and C. Michael Sampson, <em>New literary papyri from the Michigan collection: mythographic lyric and a catalogue of poetic first lines</em> (Ann Arbor, 2012), 20.</li>
        <li>El-Maghrabi, M. G., and C. Römer (eds), <em>Texts from the "Archive" of Socrates, the Tax Collector, and Other Contexts at Karanis (P. Cair. Mich. II)</em> (Berlin, 2015), 48.</li>
        <li>Finglass, P. J., 'Unpublished Conjectures on Sophocles by Jeremiah Markland', <em>Greek, Roman, and Byzantine Studies</em> 51/2 (2011), 232-238.</li>
        <li>Finglass, Patrick J. 'Il valore dei papiri per la critica testuale di Sofocle', in <em><a href="https://library.oapen.org/bitstream/handle/20.500.12657/55124/9788866553878.pdf">Il valore dei papiri per la critica testuale di Sofocle</a></em> (Florence, 2013), 33-51.</li>
        <li>Finglass, P. J. 'Editions of Sappho since the Renaissance', in <em>The Cambridge Companion to Sappho</em> (Cambridge, 2021), 247-59 at 255.</li>
        <li>Gerber, Douglas E. '<a href="https://doi.org/10.5169/seals-660688">Emendations in the Odes of Pindar: An Historical Analysis</a>', <em>Entretiens Hardt</em>, 31 (1984), 1-25.</li>
        <li>Grenfell, B. P., 'The Value of Papyri for the Textual Criticism of Extant Greek Authors', <em>The Journal of Hellenic Studies</em>, 39 (1919), 16-36.</li>
        <li>Homerus, <em>Ilias: Rhapsodiae I-XII</em>, ed. Martin L. West (Munich, 1998).</li>
        <li>Homerus, <em>Ilias: Rhapsodiae XIII-XXIV</em>, ed. Martin L. West (Munich, 2000).</li>
        <li>Homerus, <em>Odyssea</em>, ed. Martin L. West (Berlin, 2017).</li>
        <li>Kenyon, Frederic George, <em>The Evidence of Greek Papyri with Regard to Textual Criticism</em> (London, 1904).</li>
        <li>Markus, D., and G. Schwendner, 'Seneca’s Medea in Egypt (663–704)', <em>ZPE</em>, 117 (1997), 73–84.</li>
        <li>Sommerstein, Alan H., 'The history of the text of Aristophanes', in <em>Brill's Companion to the Study of Greek Comedy</em> (Brill, 2010), 399-422 at 412n69.</li>
        <li>Wilson, N. G., <em>Herodotea: studies on the text of Herodotus</em> (Oxford, 2015), xii-xiii.</li>
    </ul>
</details>

&nbsp;  
See also James Zetzel's [Textual Criticism and the Transmission of Latin Texts](./zetzel.md).

This database is searchable as a [CSV file](https://github.com/t18d/attested-conjectures/blob/main/attested-conjectures.csv).

&nbsp;  

"""

csv_tools.sort_csv()

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

