import json

from flask.testing import FlaskClient
import jwt

# -----------------------------------------------------------------------------


class AuthorizedClient(FlaskClient):
    """A Flask client with JWT authorization support"""

    default_metadata = None
    default_subject = 'foo'

    def open(
        self,
        *args,
        headers=None,
        metadata=None,
        subject=None,
        data=None,
        token_payload_extra=None,
        **kwargs
    ):
        args = ('api/v1/{}'.format(args[0]),)

        headers = {
            'Authorization': self.make_authorization(
                metadata, subject, token_payload_extra,
            ),
            **(headers or {}),
        }

        if data is not None:
            kwargs.setdefault('content_type', 'application/json')
            if kwargs['content_type'] == 'application/json':
                data = json.dumps({'data': data})

        return super().open(*args, headers=headers, data=data, **kwargs)

    def make_authorization(
        self, metadata=None, subject=None, token_payload_extra=None,
    ):
        token = jwt.encode(
            {
                'iss': 'issuer',
                'sub': subject or self.default_subject,
                'aud': 'audience',
                'app_metadata': metadata or self.default_metadata,
                **(token_payload_extra or {}),
            },
            'secret',
            algorithm='HS256',
        )

        return 'Bearer {}'.format(token.decode())
