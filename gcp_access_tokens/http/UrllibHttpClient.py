from urllib.request import Request
from urllib.request import urlopen
import json

from .HttpClient import HttpClient

class UrllibHttpClient(HttpClient):

    """
    Implemented response handlers
    """
    allowed_response_types = ['application/json']

    
    def get(self, target, path, headers={}, expected_response_type='application/json'):
        """
        Issues a get request
        :param target - the target location 
                        (ie, `http://localhost:8080/` or `https://google.com/`)
        :param path - the path to the desired resource (ie, `attributes/`)
        :param headers - dict containing relevant headers
        :param expected_response_types - list of response types consumer is expecting
                                         (ie, `application/json`)
        """
        if not expected_response_type in self.allowed_response_types:
            raise NotImplementedError("Not allowed response type")
        res = urlopen(Request(
            url='{0}{1}'.format(target, path),
            headers=headers,
            method='GET'))
        # If there is ever a need to add another response type to `allowed_response_types`,
        # we will obviously need to rethink the below
        return UrllibHttpClient._parse_json_res(res)
        

    def _parse_json_res(response):
        return json.loads(response.read().decode('utf-8'))
