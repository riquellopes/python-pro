import requests
import json
import xmltodict


def parse():
    xml = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")
    response = json.dumps(
        xmltodict.parse(xml.text)
    )
    response = json.loads(response)
    return [item['TITLE'] for item in response['CATALOG']['CD']]


if __name__ == "__main__":
    print(parse())
