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


def comparemeter(sentence1, sentence2):
    if len(sentence1.meterlist) != len(sentence2.meterlist):
        print("LengthFalse")
        return False

    for i in range(len(sentence1.meterlist)):
        for stress in sentence1.meterlist[i]:
            if stress not in sentence2.meterlist[i]:
                print("MeterFalse")
                print(i)
                return False

    return True
