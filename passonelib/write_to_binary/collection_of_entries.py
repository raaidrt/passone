from entry import Entry, InvalidEntryFieldException, InvalidEncodingException
from typing import List
from copy import deepcopy

class Collection:
    def __init__(self, L : List[Entry]):
        self.L = deepcopy(L)
    
