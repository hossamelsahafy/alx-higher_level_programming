class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    def __setattr__(self, name, value):
        """Define setattr"""
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        self.__dict__[name] = value
