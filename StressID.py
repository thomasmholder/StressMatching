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

        for self.word in self.contentlist:
            self.wordlist.append(Word(self.word))
