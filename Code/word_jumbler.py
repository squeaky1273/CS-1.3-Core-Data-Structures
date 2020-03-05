import sys
# from hashtable import HashTable

# Dictionary
class Dict_word_jumbler(object):
    def __init__(self):
        self.dictionary = self.build_dict()

    def build_dict(self):
        """"Build a dictionary to hold all of the words"""
        dic = {}
        f = open("/usr/share/dict/words", "r")
        word_list = f.readlines()
        for word in word_list:
            word = word.strip().lower()
            words = ''.join(sorted(word))
            dic[words] = word
        return dic

    def anagram(self, words):
        """Build an anagram function to unscramble the letters"""
        answer = {}
        for word in words:
            word = word.strip().lower()
            word_sorted = ''.join(sorted(word))
            unscrambled = self.dictionary[word_sorted]
            answer[unscrambled] = unscrambled
            print(unscrambled)
        return answer

# # Hashtable
# class Hash_word_jumbler(object):
    # def __init__(self):
    #     self.hash = self.build_hash()

    # def build_hash(self):
    #     """"Build a hash to hold all of the words"""
    #    hashed = {}
    #     f = open("/usr/share/dict/words", "r")
    #     word_list = f.readlines()
    #     for word in word_list:
    #         word = word.strip().lower()
    #         words = ''.join(sorted(word))
    #         hashed[words] = word
    #     return hashed

    # def anagram(self, words):
    #     """Build an anagram function to unscramble the letters"""
    #     for word in words:
    #         word = word.strip().lower()
    #         word_sorted = ''.join(sorted(word))
    #         unscrambled = self.hash[word_sorted]
    #         print(unscrambled)

if __name__ == '__main__':
    words = ['tefon', 'sokik', 'niumem', 'siconu']
    jumble = Dict_word_jumbler()
    jumble.anagram(words)

    words = ['laisa', 'laurr', 'bureek', 'prouot']
    jumble = Dict_word_jumbler()
    jumble.anagram(words)