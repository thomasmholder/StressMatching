import pronouncing


class Word:

    def __init__(self, content):
        self.stresseslist = []
        self.content = content

        self.phoneslist = pronouncing.phones_for_word(content)

        for phone in self.phoneslist:
            self.stresseslist.append(pronouncing.stresses(phone))


class Sentence:

    def __init__(self, content):
        self.contentlist = content.split()
        self.meter = []
        self.wordlist = []
        self.meterlist = []

        for self.word in self.contentlist:
            self.wordclass = Word(self.word)
            self.wordlist.append(self.wordclass)

    def getmeter(self):
        self.meterlist = []
        for word in self.wordlist:
            self.meterlist.append(word.stresseslist)
