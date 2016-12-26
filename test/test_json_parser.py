"""test_json_parser: Unit test to read json content and pass into dictionary"""
import json


def test_parse_json():
    content = json.load(open("resources/data.json"))
    print(content['h264']['video'])


def test_iterate_over_json():
    content = json.load(open("resources/data.json"))
    for i in content:
        print(i)
        for k in content[i]:
            print(k, content[i][k])


if __name__ == '__main__':
    test_parse_json()
    test_iterate_over_json()
