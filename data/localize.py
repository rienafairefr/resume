import json
import copy
import os
import collections


class Localizer:
    def __init__(self, resume_filepath):
        self.resume_filepath = resume_filepath
        self.resume = json.load(
            open(self.resume_filepath), object_pairs_hook=collections.OrderedDict)
        self.found_languages = set()

    def localize(self):
        self.__find_languages(self.resume)
        for l in self.found_languages:
            self.__process_language(l)

    def __find_languages(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__find_languages(value)
            else:
                if "_" in key:
                    self.found_languages.add(key.split("_")[0])

    def __localize_resume(self, resume, language):
        if not isinstance(resume, dict):
            # we are in an array of string
            return
        for key in list(resume.keys()):
            value = resume[key]
            if isinstance(value, dict):
                self.__localize_resume(value, language)
            elif isinstance(value, list):
                for v in value:
                    self.__localize_resume(v, language)
            else:
                if "_" in key:
                    if language + "_" in key:
                        new_key = key.split(language + "_")[1]
                        change_key(resume, key, new_key)
                    else:
                        del resume[key]

    def __process_language(self, language):
        localized_resume = copy.deepcopy(self.resume)
        self.__localize_resume(localized_resume, language)
        if not os.path.exists(language):
            os.makedirs(language)
        output_filepath = language + "/" + self.resume_filepath
        with open(output_filepath, "w") as outfile:
            json.dump(localized_resume, outfile, indent=2, ensure_ascii=False)


def change_key(dictionary, old, new):
    for _ in range(len(dictionary)):
        k, v = dictionary.popitem(False)  # pop first item
        dictionary[new if old == k else k] = v


def main():
    localizer = Localizer('resume.json')
    localizer.localize()


if __name__ == "__main__":
    main()
