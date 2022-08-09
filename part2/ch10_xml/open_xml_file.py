from lxml import etree


def open_xml_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding="utf-8"))
        except KeyError as e:
            print(f"XML 데이터를 파싱하는 데 실패했습니다. 사유 : {e}")
            return None


xml_tree = open_xml_file("message1.xml")
if xml_tree:
    print(etree.tounicode(xml_tree, pretty_print=True))
