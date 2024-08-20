from html.parser import HTMLParser


class XMLtoMD(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.output = ""
        self.section_counter = 0

    def handle_starttag(self, tag, attrs):
        if tag == "content":
            self.in_content = True
        elif self.in_content:
            if tag == "section":
                self.section_counter += 1  # TODO: make this decrease
            elif tag == "title":
                self.output += "#" * self.section_counter
                self.output += " "
            elif tag == "para":
                self.output += "\n"
            elif tag == "emphasis":
                self.output += " *"  # can be assume to be italics

    def handle_data(self, data):
        if self.in_content:
            self.output += data

    def handle_endtag(self, tag):
        if tag == "emphasis":
            self.output += "* "


with open("zetzel.xml", "r", encoding="utf8") as zetz_xml:
    parser = XMLtoMD()
    parser.feed(zetz_xml.read())
    md = parser.output
    with open("zetzel.md", "w", encoding="utf8") as zetz_md:
        zetz_md.write(md)
