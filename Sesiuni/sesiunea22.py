"""
https://refactoring.guru/design-patterns/factory-method/python/example
https://realpython.com/factory-method-python/
https://dictionaryapi.dev/
"""

from abc import ABC, abstractmethod

# clasa abstracta
class Translator(ABC):
    translations = {

    }
    @abstractmethod
    # functie abstracta
    def localize(self, ro_word):
        raise NotImplementedError


class EnglishTranslator(Translator):
    translations = {
        "masina": "car"

    }

    def localize(self, ro_word):
        """
        cauta ro_word (cheia) in dictionarul sel.translations, daca exista
        returneaza valoarea corespunzatoare
        :param ro_word: cuvant in limba romana
        :return: none daca nu exista traducerea lui / traducerea lui
        """
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None

class SpanishTranslator(Translator):
    translations = {
        "masina": "coche"

    }

    def localize(self, ro_word):
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None


class FrenchTranslator(Translator):
    translations = {
        "masina": "voiture"

    }
    def localize(self, ro_word):
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None

language = input("introdu limba: ")
if language == "en":
    en_tr = EnglishTranslator()
    response = en_tr.localize("masina")
    print(response)
elif language == "sp":
    sp_tr = SpanishTranslator()
    response = sp_tr.localize("masina")
    print(response)
elif language == "fr":
    fr_tr = FrenchTranslator()
    response = fr_tr.localize("masina")
    print(response)
else:
    print("Dictionary not implemented")


class TranslatorFactory:
    @staticmethod
    def get_translator(language):
        if language == 'en':
            en_tr = EnglishTranslator()
            return en_tr
        elif language == 'sp':
            sp_tr = SpanishTranslator()
            return sp_tr
        elif language == 'fr':
            fr_tr = FrenchTranslator()
            return fr_tr
        else:
            print('Dictionary not implemented')
            return None

en_tr = TranslatorFactory.get_translator("en")
sp_tr = TranslatorFactory.get_translator("sp")
fr_tr = TranslatorFactory.get_translator("fr")
print(f'In engleza zicem {en_tr.localize("masina")}')
print(f'In spaniola zicem {sp_tr.localize("masina")}')
print(f'In franceza zicem {fr_tr.localize("masina")}')