import json

def main():
    with open('file.json', encoding='utf-8') as f:
        data = json.load(f)

    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['country_code'] = 'RUS'
    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['postal_code'] = '675004'
    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['formatted'] = 'БГПУ, ул. Ленина, 104'

    with open('file.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
