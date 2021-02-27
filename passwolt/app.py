"""
Module exposing the Passwolt API
"""

class Passwolt(object):

    def __init__(self, factory, master_password):
        self.factory = factory
        self.master_password = master_password

    def store(self, url, id, password, tags=None):
        """
        Store a new password corresponding to ``id`` for the website
        ``url``.

        The tags helps to easily retrieve and organize passwords across
        different websites and different user accounts.
        """
        pass

    def fetch(self, url, id):
        """
        Fetch password corresponding to ``id`` for the website ``url``.
        """
        pass

    def update(self, url, id, password):
        """
        Update existing password corresponding to ``id`` for the website
        ``url``.
        """
        pass

    def update_master_password(self, new_password):
        """
        Update existing ``master_password`` with ``new_password``.
        """
        pass

    def search(self, text, fields=Ellipsis):
        """
        Search ``text`` in the fields specified by ``fields``.

        By default (``fields=Ellipsis``), all the fields (i.e. ``url``, ``id``
        and ``tags``) are searched.
        """
        pass

    def generate_password(self, length=10):
        """
        Generate a strong password with desired ``length``.
        """
        pass
