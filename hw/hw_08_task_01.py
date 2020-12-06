class KeyValueStorage(dict):
    def __init__(self, filename: str):
        with open(filename, "r") as f:
            key_value = f.read()
        key_value = [list(pair.split("=")) for pair in key_value.split()]
        for pair in key_value:
            key, value = pair
            if key.isdigit():
                raise ValueError("Key should be a string!")
            if value.isdigit():
                value = int(value)
            if key not in self:
                self[key] = value
        self.__dict__ = self
