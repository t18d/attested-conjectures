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
