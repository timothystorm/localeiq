import re
import time
import xml.sax


class CldrCommonParser(xml.sax.ContentHandler):
    """
    A SAX parser for CLDR common XML files.
    This parser is designed to handle the structure of CLDR common files,
    extracting relevant information as needed.
    """

    def __init__(self):
        super().__init__()
        self.str = ""
        self.data = {}
        self.current_key = None
        self.territory_type_pattern = re.compile(r"^[A-Z]{2}$")

    def startElement(self, name, attrs):
        if (
            name == "territory"
            and not attrs.get("alt")
            and self.territory_type_pattern.match(attrs.get("type"))
        ):
            self.current_key = attrs.get("type")
            self.data[attrs["type"]] = []

    def endElement(self, name):
        if self.current_key:
            self.data[self.current_key].append(self.str.strip())
            self.str = ""
            self.current_key = None

    def characters(self, content):
        if self.current_key is not None:
            self.str += content

    def get_data(self):
        return self.data


if __name__ == "__main__":
    # creates an XMLReader
    parser = xml.sax.make_parser()

    # turnoff namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # overrides the default Handler
    handler = CldrCommonParser()
    parser.setContentHandler(handler)

    start_time = time.time()
    parser.parse("./de.xml")
    print("--- %s seconds ---" % (time.time() - start_time))
    print(handler.get_data())
