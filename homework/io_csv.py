import csv
from homework.constant import *


class IOCsv:
    """
     Wrapper for Reader
     wanted to use a @staticmethod /shrug
    """

    @staticmethod
    def read(filename, check_header=None):
        rows = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            if check_header is None or reader.fieldnames == check_header:
                for row in reader:
                    rows.append(row)
            else:
                logger.fatal("%s does not match expected header" % filename)
        return rows
