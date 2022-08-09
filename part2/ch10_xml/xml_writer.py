from lxml import etree


message2 = {
    "number": "12345",
    "pi": "3.14",
    "str": "문자열 값",
    "null_key": None,
    "object": {
        "str2": "문자열 값2",
        "object2": {
            "number2": "12345"
        }
    },
    "num_array": ['1', '2', '3', '4', '5'],
    "str_array": ["one", "two", "three", "four", "five"]
}


def to_xml(tree, dict_object):
    for key in dict_object:
        element = etree.SubElement(tree, key)
        value = dict_object[key]
        if value:
            if type(value) is str:
                element.text = value
            elif type(value) is dict:
                to_xml(element, value)
            elif type(value) is list:
                for v in value:
                    assert type(v) is str
                    etree.SubElement(element, "element").text = v
            else:
                assert False
        else:
            pass


xml_tree = etree.Element("message")
to_xml(xml_tree, message2)

with open("message2.xml", "wb") as file:
    file.write(etree.tostring(xml_tree, xml_declaration=True, encoding="UTF-8", pretty_print=True))
