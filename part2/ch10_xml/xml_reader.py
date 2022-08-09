from lxml import etree


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

# Xpath 기반 데이터 접근
root_tree = xml_tree.getroot()
print(f"root = {root_tree.tag}")

exist, number_t = read_xpath(xml_tree, "/message/number")
if not exist:
    exit(0)
print(f"number = {number_t.text}")

_, pi_t = read_xpath(xml_tree, "/message/pi")
print(f"pi = {pi_t.text}")

_, str_t = read_xpath(xml_tree, "/message/str")
print(f"str = {str_t.text}")
for attr in str_t.attrib:
    print(f"str attribute: {attr} = {str_t.attrib[attr]}")

exist, null_t = read_xpath(xml_tree, "/message/null_tag")
assert exist
print(f"null_tag = {null_t.text}")

_, option1 = read_xpath(xml_tree, "/message/str/text()")
print(f"{option1}")

_, str2 = read_xpath(xml_tree, "/message/object/str2")
print(f"str2 = {str2.text}")

_, num2 = read_xpath(xml_tree, "/message/object/object2/number2")
print(f"number2 = {num2.text}")

_, num_array_t = read_xpath(xml_tree, "/message/num_array")
for element in num_array_t.xpath("element"):
    print(f"element = {element.text}")
    for attr in element.attrib:
        print(f"\telement attribute : {attr} = {element.attrib[attr]}")

_, str_array_t = read_xpath(xml_tree, "/message/str_array")
for element in str_array_t.xpath("element"):
    print(f"element = {element.text}")
