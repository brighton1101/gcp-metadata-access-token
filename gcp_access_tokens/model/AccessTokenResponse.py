class AccessTokenResponse:
    """
    Class to model the data returned by the GCP Metadata Access Token
    endpoint.
    """

    def __init__(self, access_token, expires_in, token_type):
        """
        :param access_token - the service account access token of the gce instance
        :param expires_in - how long until token expires
        :param token_type - the token type (ie, `bearer`)
        """
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type


    @staticmethod
    def load_from_dict(res):
        return AccessTokenResponse(res.get('access_token'),
            res.get('expires_in'), res.get('token_type'))
