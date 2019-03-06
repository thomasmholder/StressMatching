import pronouncing


class Word:

    def __init__(self, content):
        self.stresseslist = []
        self.content = content

        self.phoneslist = pronouncing.phones_for_word(content)

        for phone in self.phoneslist:
            self.stresseslist.append(pronouncing.stresses(phone))


class Sentence:
    contentlist = []
    wordlist = []
    content = ""

    def __init__(self, content):
        self.contentlist = content.split()
        self.meter = []

        for self.word in self.contentlist:
            self.wordclass = Word(self.word)
            self.wordlist.append(Word(self.wordclass))
            self.meter.append(self.wordclass)
