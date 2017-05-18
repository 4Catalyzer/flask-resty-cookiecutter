from flask_resty import (
    JwtAuthentication as AuthenticationBase,
    HasAnyCredentialsAuthorization as AuthorizationBase,
)

# -----------------------------------------------------------------------------


class Authorization(AuthorizationBase):
    pass


class Authentication(AuthenticationBase):
    pass
