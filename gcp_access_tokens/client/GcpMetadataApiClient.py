from gcp_access_tokens.http.HttpClient import HttpClient
from gcp_access_tokens.model.AccessTokenResponse import AccessTokenResponse

from urllib.error import URLError

class GcpMetadataApiClient:
    """
    A class to interface with GCP metadata endpoints
    :see https://cloud.google.com/compute/docs/storing-retrieving-metadata
    """

    """
    Target of host
    """
    target = 'http://metadata.google.internal/'


    """
    Required headers
    """
    metadata_headers = {
        'Metadata-Flavor': 'Google'
    }


    def __init__(self, http_client):
        """
        Loads an api client to interface with GCP Metadata
        from an implementation of HttpClient
        :param HttpClient implementation
        """
        if not isinstance(http_client, HttpClient):
            raise Exception('Invalid api client used.')
        self.http_client = http_client


    def get_access_token(self):
        """
        Retrieves data from compute engine metadata access token endpoint
        :return AccessTokenResponse
        """
        path = 'computeMetadata/v1/instance/service-accounts/default/token'
        try:
            res = self.http_client.get(self.target, path, headers=self.metadata_headers)
        except URLError as e:
            raise Exception('Error hitting metadata endpoint. Ensure script running within GCE, App Engine, or related services')
        return AccessTokenResponse.load_from_dict(res)
