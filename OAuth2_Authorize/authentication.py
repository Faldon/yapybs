class AuthenticationRequest(object):
    def __init__(self, scope, response_type, client_id, redirect_uri, state=None, **kwargs):
        assert isinstance(scope, list)
        self.scope = scope
        self.response_type = response_type
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.state = state

        for key, value in kwargs:
            if key == 'response_type':
                assert isinstance(self.response_type, list)
                self.response_type = value.split(' ')
            elif key == 'prompt':
                assert isinstance(self.prompt, list)
                self.prompt = value.split(' ')
            elif key == 'ui_locales':
                assert isinstance(self.ui_locales, list)
                self.ui_locales = value.split(' ')
            elif key == 'acr_values':
                assert isinstance(self.acr_values, list)
                self.acr_values = value.split(' ')
            else:
                self.__setattr__(key, value)


class AuthenticationResponse(object):
    def __init__(self, code, state=None):
        self.code = code
        self.state = state


class AuthenticationErrorResponse:
    def __init__(self):
        pass


class IDToken:
    def __init__(self):
        pass


class TokenRequest:
    def __init__(self):
        pass


class TokenResponse:
    def __init__(self):
        pass