class SingleTon:
    def __init__(self):
        self.instance_id = id(self)

    def get_id(self):
        return self.instance_id


singleton_instance = SingleTon()