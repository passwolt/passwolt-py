"""
Backend storage factory classes
"""


class BaseFactory(object):

    def load(self):
        """
        Load the encrypted password file in memory
        """"
        pass

    def save(self):
        """
        Save the file on the remote server.
        """
        pass


class SelfHostedFactory(BaseFactory):
    """
    Self hosted server with encrypted file.
    """
    def __init__(self, host, auth=None):
        self.host = host
        self.auth = auth


class GoogleDriveFactory(BaseFactory):
    pass
