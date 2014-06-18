import urllib
import json

BASE_URL = 'https://vericoindice.com/api'


class VericoindiceError(Exception):
    pass


class VericoindiceClient:
    def __init__(self, api_key):
        self._api_encoded = urllib.urlencode({'api': api_key})
        
    def _make_contents(self, contents):
        contents = json.loads(contents)
        if 'error' in contents:
            raise VericoindiceError(contents['error'])

        return contents

    def get_balance(self):
        url = BASE_URL + '/getbalance'

        contents = urllib.urlopen('%s?%s' % (url, self._api_encoded)).read()
        return self._make_contents(contents)['balance']

    def roll(self, amount, chance=None):
        url = BASE_URL + '/roll'

        data = {'amount': amount}
        if chance is not None:
            data['chance'] = chance

        data = '%s&%s' % (self._api_encoded, urllib.urlencode(data))
        contents = urllib.urlopen(url, data).read()
        return self._make_contents(contents)