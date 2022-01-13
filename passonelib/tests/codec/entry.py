from passonelib.codec.entry import Entry, InvalidEntryFieldException, InvalidEncodingException

class EntryTest:
    @staticmethod
    def testEncoding():
        entry : Entry = Entry("test_account Name", "Test URL @ hotmail.com", "Test Username asldf134)*R(141&*2  16%", "test passdsaf;als29381++0`-3`23||sdafa\\")
        encoding : str = entry.encode()
        decodedEntry : Entry = Entry.decode(encoding)
        assert entry == decodedEntry
    def testEquality():
        firstEntry : Entry = Entry("abcd", "12", "34", "566&8(*34013\\")
        secondEntry : Entry = Entry("abcd", "12", "34", "566&8(*34013\\")
        assert firstEntry == secondEntry
    @staticmethod
    def testAll():  
        EntryTest.testEncoding()
        EntryTest.testEquality()

def main():
    EntryTest.testAll()

if __name__ == "__main__": main()
