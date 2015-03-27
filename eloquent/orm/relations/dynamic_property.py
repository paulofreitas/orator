# -*- coding: utf-8 -*-


class DynamicProperty(object):
    """
    Relationship dynamic property.

    It provides a simple way to access a property as is, returning the results,
    or has a method whihch will start a query on the relation.

    Example:

    >>> user = User.find(1)
    >>> user.roles  # will return the roles associated with the user
    >>> user.roles().first() # Will return the first role
    """

    def __init__(self, results, relation):
        self._results = results
        self._relation = relation

    def get_results(self):
        return self._results

    def __getattr__(self, item):
        return getattr(self._results, item)

    def __call__(self, *args, **kwargs):
        return self._relation(*args, **kwargs)