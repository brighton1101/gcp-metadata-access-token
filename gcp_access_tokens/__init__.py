from gcp_access_tokens.http.UrllibHttpClient import UrllibHttpClient
from gcp_access_tokens.client.GcpMetadataApiClient import GcpMetadataApiClient


def access_token_from_metadata():
    """
    Injects UrllibHttpClient into GcpMetadataApiClient, and then
    makes request to get access token response from metadata endpoints
    for GCE instances (and associated resources, such as App Engine and
    Cloudfunctions, which run in App Engine). This returns an 
    `AccessTokenResponse` object, which contains the access token,
    the amount of time the token until the token expires, and the 
    token type

    :see https://cloud.google.com/compute/docs/storing-retrieving-metadata
    :throws Exception upon error with http call
    :return `AccessTokenResponse`
    """
    http_client = UrllibHttpClient()
    metadata_api_client = GcpMetadataApiClient(http_client)
    return metadata_api_client.get_access_token()


def access_token_string_from_metadata():
    """
    Does the same thing as `access_token_from_metadata` except the
    actual access token is extracted and returned

    :see https://cloud.google.com/compute/docs/storing-retrieving-metadata
    :throws Exception upon error with http call
    :return str containing access token
    """
    return access_token_from_metadata().access_token
