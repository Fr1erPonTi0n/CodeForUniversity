import json


def main():
    with open('file.json', encoding='utf-8') as f:
        data = json.load(f)

        country = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][0]['name']
        cords = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

        print(country, cords, sep='\n')


if __name__ == '__main__':
    main()
