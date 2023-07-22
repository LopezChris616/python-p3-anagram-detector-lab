class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        word_letters = [letter for letter in self.word]
        anagram_matches = []

        for word in list:
            list_letters = [letter for letter in word]
            if sorted(word_letters) == sorted(list_letters):
                anagram_matches.append(word)

        if len(anagram_matches) > 0:
            return anagram_matches
        else:
            return []