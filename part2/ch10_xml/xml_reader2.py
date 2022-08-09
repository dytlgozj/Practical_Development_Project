from lxml import etree


def read_all(tree, xpath):
    for tag in tree:
        if len(tag) > 0:
            read_all(tag, f"{xpath}/{tag.tag}")
        else:
            if tag.text:
                print(f"{xpath}/{tag.tag} = {tag.text}")
            else:
                print(f"{xpath}/{tag.tag}")


def read_xpath(tree, xpath):
    tags = tree.xpath(xpath)
    if tags and len(tags) > 0:
        return True, tags[0]
    else:
        return False, None


def open_xml_file(filename):
    with open(filename, encoding="UTF8") as file:
        try:
            return etree.parse(file, parser=etree.XMLParser(encoding="utf-8"))
        except KeyError as e:
            print(f"XML 데이터를 파싱하는 데 실패했습니다. 사유 : {e}")
            return None


xml_tree = open_xml_file("message1.xml")
if not xml_tree:
    exit(0)

exist, root_tree = read_xpath(xml_tree, "/message")
assert exist

read_all(root_tree, root_tree.tag)
