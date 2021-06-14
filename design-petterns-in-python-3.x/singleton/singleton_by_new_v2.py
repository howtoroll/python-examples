class SingleTon:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleTon, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.instance_id = id(self)

    def get_id(self):
        return self.instance_id
