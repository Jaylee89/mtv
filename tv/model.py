import datetime

class TVModel:
    name: str
    url: str
    category: str
    http_code: int
    ipv4: int
    valid: int
    updated_date: str

    def __init__(self, name: str, url: str, category: str = 'N/A', http_code: int = 0, ipv4: int = '9', valid: int = '9', updated_date: str = datetime.datetime.now()) -> None:
        self.name = name
        self.url = url
        self.category = category
        self.http_code = http_code
        self.ipv4 = ipv4
        self.valid = valid
        self.updated_date = updated_date
    
    def to_tuple(self) -> tuple:
        return (self.name, self.url, self.category, self.ipv4, self.valid, self.updated_date)
