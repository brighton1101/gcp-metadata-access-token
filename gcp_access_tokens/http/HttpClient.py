"""
Simple HttpClient. 

All implementations should implement the following interface
"""
class HttpClient:

    """
    Issues a get request
    :param target - the target location 
                    (ie, `http://localhost:8080/` or `https://google.com/`)
    :param path - the path to the desired resource (ie, `attributes/`)
    :param headers - dict containing relevant headers
    :param expected_response_types - response type consumer is expecting
                                     (ie, `application/json`)
    """
    def get(self, target, path, headers={}, expected_response_type='application/json'):
        raise NotImplementedError
