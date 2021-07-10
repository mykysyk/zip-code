import requests
import sys
import json
from pprint import pprint

URL = 'http://zipcloud.ibsnet.co.jp/api/search?zipcode={}'

def zip_api(zip_code):
    r = requests.get(URL.format(zip_code))
    return r.json()

def main():
    zip_code = sys.argv[1]
    zip_json = zip_api(zip_code)
    print(json.dumps(zip_json, ensure_ascii=False))

if __name__ == '__main__':
    main()
