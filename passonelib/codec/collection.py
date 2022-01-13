from passonelib.codec.entry import Entry, InvalidEntryFieldException, InvalidEncodingException
from typing import List, Optional
from copy import deepcopy

class Collection:
    def __init__(self, L : List[Entry]):
        self.L = deepcopy(L)
    """
    Encoding Scheme:
    1. Until the first $ sign is encountered, the digits represent the 
       number of entries in our collection.
    2. Read num_entries number of lengths for the len_entries separated by $
    3. Decode the entries from the rest of the string based on len_entries
    """
    def encode(self) -> str:
        num_entries = len(self.L)
        encodings = [entry.encode() for entry in self.L]
        lens = [str(len(encoding)) for encoding in encodings]
        return '$'.join([str(num_entries)] + lens) + '$' + ''.join(encodings)
    @staticmethod
    def decode(s : str) -> 'Collection':
        def get_idx(s : int) -> Optional[int]:
            for i in range(len(s)):
                if s[i] == '$': return i
        idx = get_idx(s)
        if idx == None or len(s) <= idx + 1: raise InvalidEncodingException()
        try: 
            n = int(s[:idx])
        except ValueError: 
            raise InvalidEncodingException()
        s = s[idx+1:]
        def get_nth_idx(s : str, n : int) -> Optional[int]:
            counter = 0
            for i in range(len(s)):
                if s[i] == '$': 
                    counter += 1
                    if counter >= n: return i
        idx = get_nth_idx(s, n)
        print(idx)
        if idx == None or len(s) <= idx + 1:
            raise InvalidEncodingException()
        try: lens = [int(x) for x in s[:idx].split('$')]
        except ValueError: raise InvalidEncodingException()
        s = s[idx+1:]
        encodings = []
        for ln in lens:
            encodings.append(Entry.decode(s[:ln]))
            s = s[ln:]
        if s != "": raise InvalidEncodingException()
        return Collection(encodings)
    def __repr__(self):
        return f"Collection[{','.join([repr(entry) for entry in self.L])}]"
    def __eq__(self, other : 'Collection'):
        if not isinstance(other, Collection): return False
        if len(self.L) != len(other.L): return False
        n = len(self.L)
        for i in range(n):
            if self.L[i] != other.L[i]: return False
        return True
