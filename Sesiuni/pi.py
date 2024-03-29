# sesiunea 13-14 merge tot codul
'''class ExampleJson:
    file_path = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\Sesiuni\\example.json"

    def citeste_fisier(self):
        with open(file=self.file_path, mode="r") as file: # metoda de a deschide un fisier
            for line in file.readlines():
                print(line)

e = ExampleJson()
e.citeste_fisier()
'''
'''
class ExampleJson:
    file_path_text = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\requirements.txt"

    def citeste_fisier_text(self):
        with open(file=self.file_path_text, mode="r") as file: # metoda de a deschide un fisier
            for line in file.readlines():
                print(line)

e = ExampleJson()
e.citeste_fisier_text()


'''

# sesiunea14
'''
import json
class ExampleJson:
    file_path_text = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\requirements.txt"

    def citeste_fisier_text(self):
        with open(file=self.file_path_text, mode="r") as fisier:
            # pt json
            # json.load(fisier)
            return fisier.readlines()

    def scriere_fisier(self):
        with open(self.file_path_text, "a") as fisier: # a de la append
            fisier.writelines('teste')

e = ExampleJson()
e.citeste_fisier_text()
print(e.citeste_fisier_text())
e.scriere_fisier()
print(e.citeste_fisier_text())
'''

import json
import csv
import pandas as pd
from pprint import pprint

class WorkingWithFiles:
    file_path_text = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\requirements.txt"
    file_path_json = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\Sesiuni\\file.json"
    file_path_csv = "C:\\Users\\Daniel\\PycharmProjects\\Intro\\Sesiuni\\file.csv"

    def citeste_fisier_text(self):
        with open(file=self.file_path_text, mode='r') as fisier:
            for line in fisier.readlines():
                line = line.strip() # elimina caractere nedorite ca /n (new line)
                print(line)

    def citeste_fisier_json(self):
        with open(file=self.file_path_text, mode='r+') as file:
            content = json.load(file)
            # a = content['c']
            # print(a)
            # print(content)
            return content
            # for k, v in content.items():
            #     print(k, v)


    def scrie_fisier_json(self, key, value):
        # getting the old file content
        with open(file=self.file_path_json, mode='r+') as file:
            content = json.load(file) # citim fisierul
            content[key] = value # adaugam key + value la content
            file.seek(0) # muta file pointer la inceputul  fisierului
            file.truncate() # stergem continutul fisierului
            json.dump(content, file) # scriem continutul in fisier
        # with open(file=self.file_path_json, mode='w+') as file:
        #     content = json.load(file)
        #     print(content)

            # obj = {key:value}
            # # print(content)



    def citeste_fisier_csv(self):
        with open(file=self.file_path_csv, mode='r+', newline='\n') as file:
            content = pd.read_csv(file, header=0)
            #     print(content)
            # print(content.columns.values)
            header = "\t\t".join(content.columns.values) # \t e pentru tab, join ia valorile dintr-o lista si creeaza un string punand intre ele ce vrem noi
            print(header)
            print("---------------------------------------------------")
            # pprint(content)
            for line in content.values:
                l = [str(element) for element in line] # list comprehension
                # ll = [] # alt mod de a face list comprehension
                # for element in line:
                #     ll.append(str(element))
                new_line = "\t\t".join(l)
                print(new_line)
            print(content)
            # csvwriter = csv.writer(file) #old version
            # csvwriter.writerow([4, "17763ds", 764]) # old version








    def scriere_fisier(self):
        with open(self.file_path_text, "a") as fisier:
            fisier.writelines('teste')



e = WorkingWithFiles()
# e.citeste_fisier_text()
# e.citeste_fisier_json()
# print(e.citeste_fisier_json())
# e.scrie_fisier_json(key = "key d", value="val d")
e.citeste_fisier_csv()














