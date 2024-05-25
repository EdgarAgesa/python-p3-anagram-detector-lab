class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []
        for anagram in possible_anagrams:
            if self.is_anagram(anagram):
                matches.append(anagram)
        return matches

    def is_anagram(self, anagram):
        return sorted(anagram.lower()) == sorted(self.word.lower())
            