import sys


class V1:
    def __init__(self, config):
        self.config = config
        self.__token = None

    @property
    def token(self):
        if self.__token is None:
            self.__token = 'token'
        return self.__token


class V2:
    def __init__(self, config):
        self.config = config
        self.__token = None

    @property
    def access_key_id(self):
        return self.token['AccessKeyId']

    @property
    def secret_access_key(self):
        return self.token['SecretAccessKey']

    # declare order is not matter
    @property
    def token(self):
        if self.__token is None:
            self.__token = {'AccessKeyId': 'ak', 'SecretAccessKey': 'sk'}
        return self.__token


def main():
    e1 = V1('config')
    print(e1.config)
    e1.config = 'config'
    print(e1.token)
    #e1.token = 'token'  # AttributeError: can't set attribute

    e2 = V2('config')
    print(e2.config)
    e2.config = 'config'
    print(e2.access_key_id)
    print(e2.secret_access_key)
    print(e2.token)


if __name__ == "__main__":
    sys.exit(main())
