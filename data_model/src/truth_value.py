
class TrueObject:
    pass


class FalseLenObject:

    def __len__(self):
        return 0


class FalseBoolObject:

    def __bool__(self):
        return False


class LenBoolObject:

    def __len__(self):
        print('len')
        return 0

    def __bool__(self):
        print('bool')
        return False
