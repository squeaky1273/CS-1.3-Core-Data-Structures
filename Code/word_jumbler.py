# Dictionary
class Dict_word_jumbler(object):
    def __init__(self):
        self.dict = self.build_dict()

    def build_dict(self):
        """"Build a dictionary to hold all of the words/letters"""
        dic = {}
        f = open("/usr/share/dict/words", "r")
        word_list = f.readlines()
        for word in word_list:
            word = word.strip().lower()
            words = ''.join(sorted(word))
            dic[words] = word
        return dic

    def unscramble(self, words):
        """Build a function to unscramble the letters"""
        for word in words:
            word = word.strip().lower()
            word_sorted = ''.join(sorted(word))
            if word_sorted in self.dict:
                unscrambled = self.dict[word_sorted]
                print(unscrambled)
            else:
                return None

if __name__ == '__main__':
    # Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his __-______."
    words = ['tefon', 'sokik', 'niumem', 'siconu']
    jumble = Dict_word_jumbler()
    jumble.unscramble(words)
    
    # # "A bad way for a lawyer to learn the criminal justice system: _____ and _____."
    # words = ['laisa', 'laurr', 'bureek', 'prouot']
    # jumble = Dict_word_jumbler()
    # jumble.unscramble(words)

    # # Cartoon prompt for final jumble: "What a dog house is: A ____ ___."
    # words = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    # jumble = Dict_word_jumbler()
    # jumble.unscramble(words)