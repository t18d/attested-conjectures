---
title: Notes for Contributors @ Database of Greek and Latin Conjectural Emendations Attested in MSS
permalink: contributing/
seo:
  type: HowTo
last_modified_at: 2024-08-30T00:10:12+00:00
---
# Notes for Contributors

The only works that lie outside the scope of this database are Christian and other sectarian writings. The two testaments are included, however, on account of their interest for textual criticism.

If you are going to concentrate on a particular author, first have a look at open [issues](https://github.com/t18d/attested-conjectures/issues) to see if someone is already working on it.

After editing a CSV file in your fork or [clone](#clone-the-repo), open a pull request. In the **description** field, record the secondary source(s) where you _first_ learnt about the conjectures you are editing. Time permitting, check and record the original publication containing a conjecture. Add a link if it’s difficult to find.

The following notes provide more in-depth guidelines.

## Clone the repo
If you prefer working from the command line, you can follow the steps below to keep the files you download to a minimum:

```bash
# Make sure you have git installed
$ git clone --single-branch --filter=blob:none --sparse --depth=1 git@github.com:t18d/attested-conjectures.git
$ cd attested-conjectures/
$ git sparse-checkout set --no-cone '/*' '!/assets/*.webp' '!/assets/*.pdf'
```
See also our [Unix tools](https://t18d.github.io/tools/) page.

## CSV syntax
Enclose fields containing commas in double quotes. Escape a double quote inside such fields by a [preceding double quote](https://datatracker.ietf.org/doc/html/rfc4180#section-2).

## Ref.
For Greek, use LSJ’s abbreviations and [DGE’s](http://dge.cchs.csic.es/lst/2lst1.htm) numberings. When LSJ uses [single-letter abbreviation](#single-letter-abbreviations) for an author, switch to [OCD’s](https://oxfordre.com/classics/page/3993). When an author or work is absent from both LSJ and DGE, try [RE](https://de.m.wikipedia.org/wiki/Liste_der_Abkürzungen_antiker_Autoren_und_Werktitel). For Byzantine works, see [LBG](https://stephanus.tlg.uci.edu/lbg/lbg_abbreviations.html).

For Latin, follow [TLL](https://thesaurus.badw.de/tll-digital/index/a.html).

Instructions for specific works follow:

### Fragments
#### Same tradition 
If the conjecture on a fragmentary text is attested in sources belonging to the same tradition as the paradosis, record it under that tradition.

#### Multiple traditions 
If it is attested in a different tradition, record it under the original author of the fragment.

### Aristophanes
Follow OCD’s abbreviations.

### Philo
<img src="https://t18d.github.io/attested-conjectures/assets/290511383-00bd0375-06f1-4cae-b0f6-64188379966e.jpeg.webp" width="50%" />
<img src="https://t18d.github.io/attested-conjectures/assets/290511838-72d71c5b-6d24-412f-8aa6-4dd9f9d927b3.jpeg.webp" width="50%" />

### Single-letter abbreviations
For authors with single-letter (grapheme) abbreviations in LSJ, use the abbreviations in [OCD](https://oxfordre.com/classics/page/3993) instead. Thus, **Soph.**, **Eur.**, **Aesch.**, **Thuc.**, **Dem.**, are preferable to **S.**, **E.**, **A.**, **Th.**, **D.**.

## Paradosis
This column aims to capture not what other readings are available in the tradition but specifically the one(s) that was actually available to the critic at the time an emendation was made, whenever such information is available or can be inferred from the apparatus. This becomes difficult when an editor did not disclose the identity of his base text. Help with improving the accuracy on this front is most welcome.

Of the readings that have been thus identified, record only those that may be considered to have contributed to the conjecture in question.

Neighbouring words are given when they offer clues to how the corruption may have occurred.

### NT
The text printed in NA<sup>28</sup> is used for NT conjectures, following upstream.

### Superscript 
Unicode superscript is preferable because it preserves the readability of raw CSV. When this is unavailable, enclose the letter with \<sup\>\</sup\> tags.

## Conjecture
This aims to capture the exact letters and accentuation as proposed by the critic, whilst the actual reading as found in manuscripts are recorded in Rem. if it is different. The two readings may be combined in this column, however, if this is unlikely to cause confusion.

## Author
This is the name of the critic. 

### Spelling
If the critic already has entries in the database, follow the spelling of existing entries. (And open an issue in case there’s inconsistency.)

For new names, prefer the spelling that is going to turn up most information in the search engine. Vernacular spelling is particularly appropriate when a critic made waves outside scholarship.

The lemma on Wikipedia is usually a good choice if an article is available in the relevant language, except when it differs from the one commonly used in classical scholarship or is ill-formed (e.g. [Turnèbe](https://t18d.github.io/attested-conjectures/des-noms-latins/#turnebus)). Mark Ockerbloom’s Online Books Page is another useful resource, as the spelling adopted there tends to reflect what’s actually on the title-pages.

#### German names
The choice between _c_ and _k_ follows the critic’s own practice when signing _in German_.

### Styling
A single given name is written out; otherwise, initials are used. A combination of given name and initials may be used to reflect a critic’s own preference. Note the following exceptions:

#### Famous critics
These are well-known names in classical scholarship that need no further identification. They are represented by surname alone.

#### Single initial
Critics identified with a single initial are of three kinds:

##### The namesakes
Less-known critics who have a famous name but who can still be easily identified, e.g. L. Dindorf, P. Manutius. 

##### The unknown 
These are names of which only the initial has been identified and for which a N&Q note would be welcome.

##### Living critics
These are frequently given with single initial when this is enough to find them through search engines.

## Year
As a general rule, do not convert to [Circumcision style](https://archive.org/details/oxfordcompaniont00blac/page/784/) or correct for [secular difference](https://archive.org/details/oxfordcompaniont00blac/page/788/). This makes it easier for the user to track down the same book from which a conjecture is taken. Where a correction is made for the purpose of establishing priority, document this in Rem.

### Ad editores
Editors are urged to follow the best practice of disclosing a list of _recentiorum commentationes_ or _index philologorum_ and using superscripts after a name in the apparatus when the same critic has made conjectures in different publications.

### Posthumous conjectures 
Record the year or range of years during which a conjecture was actually made if this information is available in biographical materials.

Otherwise, record the year of posthumous publication. When priority may be at issue, however, indicate instead the period (see [below](#undatable-conjectures)) during which a conjecture was made.

### Conjectures to be dated
Give the range of years when a conjecture is known to be made in a multi-volume work or one of several works but you haven’t yet found out which.

Leave the column blank when you believe a conjecture can be dated but haven’t been able to do it.

### Undatable conjectures
Enter ‘n.d.’ when a conjecture is considered undatable.

For obscure critics, it would be helpful to indicate the period in which they flourished:

<img src="https://t18d.github.io/attested-conjectures/assets/289861739-9c2261b1-1680-4726-a196-96c336063ef7.jpeg.webp" width="50%" />

### Self-reported conjectures 
Self-reported conjectures cannot be verified and are therefore excluded from this database.

## Attested Place
This aims to give just enough information to help locate the relevant source. For papyri, a [Checklist-style citation](https://papyri.info/docs/checklist) is given whenever it is available.

### Two forms of citation 
A **full citation** is the shelfmark of a manuscript in the case of direct tradition, and the relevant author and passage in the case of indirect tradition.

Whenever possible, append the siglum adopted in the best available edition of the material at the time of the creation of an entry and enclose it _in uncis_, whilst qualifications should go in the Rem. column.

An **abbreviated citation** consists of sigla and their qualifications.

#### Give full citation if …
a single source is being cited and there is no qualification as to which hand wrote the reading in question or where it’s written.

#### Give abbreviated citation if …
two or more sources are cited, or a source requires qualification.

Superscripts indicating a hand are only necessary when the sigla themselves contain Arabic numerals. Use Unicode superscripts.

### Too good to be true
If a critic’s conjectures coincide with readings of the same manuscript in a disproportionate way, it can be a sign that he had actually seen that copy or a similar one. Unless it is determined that the critic didn’t have access to such an additional source, delete the relevant entries and document the case in the commit message.

### Multiple sources
Sources are reported selectively. In general, direct tradition takes precedence over indirect tradition; unqualified sources are cited over qualified ones. When manuscripts from different periods are available, report the earliest.

### Conflicting reports
When the relevant manuscript reading is only reported in one recent edition, use abbreviated citation and append the name of that editor _in uncis_. If a different reading is reported or implied in the other recent editions, add the word _teste_ in front of that name.

### Correlatives
Two conjectures that form a pair of correlatives must appear in the same manuscript to be considered attested. 

### Conjectures in manuscript
It is likely that some of the manuscript readings cited here are themselves be the conjectures of the scribe or scholar. Where this is generally held to the case (e.g. Livineius’s ‘p’ or Paris. gr. 2886 for Sophocles), that manuscript is not considered evidence of attestation.

## Rem.
This can record the exact papyrus reading, a qualification concerning a source (usually when full citation is given in the previous column), the relevant bibliography, or anything that is noteworthy about an emendation or critic.

When a conjecture is not made in the text, apparatus or running commentary, it would be helpful to record the page where it is found.

So as to encourage a basic familiarity with the history of scholarship, full citation should be given sparingly. Commentaries and adversaria are meant to be identified through author and year alone. Examples of the latter include Madvig (1871, 1873, 1884), Gronovius (1639, 1662) and Caspar von Barth (1624).

When a group of emendations on the same text come from a single source, reference may be given at the first entry.
