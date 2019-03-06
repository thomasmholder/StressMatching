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

        for word in self.wordlist:
            self.meterlist.append(word.stresseslist)


@Sentence
def comparemeter(sentence1, sentence2):
    if sentence1.meterlist.length() != sentence2.meterlist.length():
        return False

    for i in sentence1.meterlist.length():
        for stress in sentence1.meterlist[i]:
            if stress in sentence2.meterlist[i] is False:
                return False

    return True
