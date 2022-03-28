import csv
import sys


class File_Parser:

    @staticmethod
    def parse_csv():
        dict_csv = {}
        if sys.platform.startswith('win'):
            path = ".\\app\\files\\test.csv"
        else:
            path = "./code/app/files/test.csv"
        with open(f'{path}', mode='r') as csv_file:
            File_Parser = csv.DictReader(csv_file)
            for row in File_Parser:
                dict_csv[row["bin"]] = {key: row[key] for key in row}
            return dict_csv
