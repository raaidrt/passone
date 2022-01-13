class InvalidEntryFieldException(Exception):
    def __init__(self, info : str):
        self.info = info

class InvalidEncodingException(Exception):
    pass


def format_int(n : int) -> str:
    to_return = str(n)
    to_add_in_front = ''.join(['0'] * (3 - (len(to_return))))
    return to_add_in_front + to_return

def is_valid_username(username : str) -> bool:
    return len(username) < 1000
def is_valid_account_name(account_name : str) -> bool:
    return len(account_name) < 1000
def is_valid_password(password : str) -> bool:
    return len(password) < 1000
def is_valid_url(url : str) -> bool:
    return len(url) < 1000
 

class Entry:
    def __init__(self, account_name : str, url : str, username : str, password : str):
        if not is_valid_username(username): raise InvalidEntryFieldException(f"Invalid Username \"{username}\"")
        if not is_valid_account_name(account_name): raise InvalidEntryFieldException(f"Invalid Account Name \"{account_name}\"")
        if not is_valid_password(password): raise InvalidEntryFieldException(f"Invalid Password \"{password}\"")
        if not is_valid_url(url): raise InvalidEntryFieldException(f"Invalid URL \"{url}\"")
        self.username = username
        self.account_name = account_name
        self.url = url
        self.password = password
    """
    Encoding Scheme:
    1. The first 3 characters are digits that correspond to the length of the account_name
    2. The next 3 characters are digits corresponding to the length of the url
    3. The next 3 characters are digits corresponding to the length of the username
    4. The next 3 characters are digits corresponding to the length of the password
    The account_name, url, username and password are then concatenated in the rest of the string
    """
    def encode(self) -> str:
        return ''.join([format_int(len(self.account_name)), format_int(len(self.url)), 
                format_int(len(self.username)), format_int(len(self.password)), 
                self.account_name, self.url, self.username, self.password])
    @staticmethod
    def decode(s : str) -> 'Entry':
        if len(s) < 12: raise InvalidEncodingException()
        lens = {}
        try:
            lens['account_name'] = int(s[:3])
            lens['url'] = int(s[3:6])
            lens['username'] = int(s[6:9])
            lens['password'] = int(s[9:12])
        except ValueError:
            raise InvalidEncodingException()
        if len(s[12:]) != sum(lens.values()):
            raise InvalidEncodingException()
        s = s[12:]
        values = {}
        for item in lens.keys():
            values[item], s = s[:lens[item]], s[lens[item]:]
        return Entry(values['account_name'], values['url'], values['username'], values['password'])
    def __repr__(self) -> str:
        return f"Entry[account_name={self.account_name},url={self.url},username={self.username},password={self.password}]"
    def __eq__(self, other : 'Entry') -> bool:
        if not isinstance(other, Entry): return False
        return self.account_name == other.account_name and self.url == other.url and self.username == other.username and self.password == other.password
