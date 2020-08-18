# GCE Service Account Access Token Extractor

##### Python logic to fetch the application-default service account programatically from within GCE, App Engine, Cloudfunctions, or other GCE-associated services

### Usage
- Suppose you need to make an authenticated request to a GCP endpoint from within a GCE instance
- Your service account has proper IAM perms to perform action, but you just need to retrieve the access tokens associated with it
```python3
from gcp_access_tokens import access_token_string_from_metadata

# Fetch access token
token = access_token_string_from_metadata()
```
