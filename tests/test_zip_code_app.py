from zip_code_app import __version__
from zip_code_app import core

def test_version():
    assert __version__ == '0.1.0'

def test_zip_api():
    expect = {
        'message': None,
        'results': [{'address1': '東京都',
              'address2': '千代田区',
              'address3': '千代田',
              'kana1': 'ﾄｳｷｮｳﾄ',
              'kana2': 'ﾁﾖﾀﾞｸ',
              'kana3': 'ﾁﾖﾀﾞ',
              'prefcode': '13',
              'zipcode': '1000001'}],
        'status': 200
    }
    actual = core.zip_api('100-0001')
    assert expect == actual
