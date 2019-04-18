import re
from pattern.en import suggest
from spellchecker import SpellChecker


class SpellingSuggestor(object):
    def __init__(self, word):
        self.word = word
        self.spell = SpellChecker()

    """"method to replace underscore or dash by space"""

    def pre_process(self):
        return re.sub(r'([^\s\w]|_|-)+', ' ', self.word)

    """method to remove letters which occur more than twice"""

    def reduce_lengthening(self):
        pattern = re.compile(r"(.)\1{2,}")
        return pattern.sub(r"\1\1", self.word)

    "main method to call and do spell check processing "

    def spell_checker_result(self):
        self.word = self.pre_process()
        self.word = self.reduce_lengthening().lower()
        i = 1
        print("word after cleaning ", self.word)
        misspelled = self.spell.unknown([self.word])
        if len(misspelled) == 0:
            return [self.word]
        result = set()
        while (i < len(self.word)):
            r1 = self.spell.candidates(self.word[:i].strip())
            r2 = self.spell.candidates(self.word[i].strip())
            r1 = self.spell.known(r1)
            r2 = self.spell.known(r2)
            if len(r1) > 0 and len(r2) > 0:
                try:
                    for v1 in r1:
                        result.add(v1)
                        for v2 in r2:
                            if len(v2) > 2:
                                result.add(v2)
                                result.add(v1 + " " + v2)
                except Exception as ex:
                    print("some error", ex)
            i += 1
        return result


if __name__ == "__main__":
    print(SpellingSuggestor("hello;world").spell_checker_result())
