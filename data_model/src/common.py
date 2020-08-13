
class Common:
    """Example between __new__ and __init__
    """

    def __new__(cls):
        """
        This is the constructor.
        Should return an object, usually an instance of cls

        Args:
            cls `Constructor`: this class

        Returns:
            `Constructor` instance

        """
        print('this is the constructor')
        obj = super().__new__(cls)
        print('here object is created but not initialized')
        return obj

    def __init__(self):
        """
        This is the initializer for instance.
        Here the object already exists, is `self`
        Should return None.
        """
        print('this is the initializer')

    def __del__(self):
        """Finalizer
        """
        print('this is executed with `del` statement'
              'or when count reference is 0'
              'or when program execution going to finish')

    def __repr__(self):
        """this is the object representation.
        It's executed with `repr` function or
        just with "intro" (only in the shell interpreter)
        It should not necessarily be human readable.

        Returns:
            str: representation string
        """
        return f'<{self.__class__.__name__}>'

    def __str__(self):
        """this is the object text representation
        It's executed with `str` and `print` functions.
        It Should be human readable.

        Returns:
            str: representation string
        """
        return self.__class__.__name__
