from keyword import iskeyword


class KeyValueStorage:
    def __init__(self, filename: str):
        self.my_dict = {}
        with open(filename, "r") as f:
            key_value = f.read()
        key_value = [list(pair.split("=")) for pair in key_value.split()]
        for pair in key_value:
            key, value = pair
            value = value.rstrip()
            if iskeyword(key) or not key.isidentifier():
                raise ValueError("Invalid key!")
            if value.isdigit():
                value = int(value)
            if key not in self.my_dict.keys():
                self.my_dict[key] = value

    def __getitem__(self, item: str):
        return self.my_dict[item]

    def __getattr__(self, key: str):
        return self.my_dict[key]
