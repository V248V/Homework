import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        list_words = []
        for name_of_f in self.file_names:
            with (open(name_of_f, 'r', encoding='utf-8') as file):
                for line in file:
                    new_line = re.sub(r'[.!,]', '', line)
                    new_line = new_line.lower().split()
                    for word in new_line:
                        list_words.append(word)
                all_words[name_of_f] = list_words
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_dict[name] = words.index(word.lower()) + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word.lower())
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))