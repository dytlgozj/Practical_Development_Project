import json


message2 = {
    "number": 12345,
    "pi": 3.14,
    "str": "문자열 값",
    "null_key": None,
    "object": {
        "str2": "문자열 값2",
        "object2": {
            "number2": 12345
        }
    },
    "num_array": [1, 2, 3, 4, 5],
    "str_array": ["one", "two", "three", "four", "five"]
}

with open("message2.json", 'w', encoding="UTF8") as file:
    json.dump(message2, file, indent=4, ensure_ascii=False)
