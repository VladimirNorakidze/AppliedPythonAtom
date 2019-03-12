#!/usr/bin/env python
# coding: utf-8

import sys
from for_table import import_data, processing, table_creator


if __name__ == '__main__':
    filename = sys.argv[1]

    data, json_status = import_data.opening(filename)
    if json_status:
        keys = list(data.keys())
    if not processing.check_data(data, json_status=False):
        sys.exit()
    if not json_status:
        data, keys = processing.data_to_json(data)
        json_status = True
        if data is False:
            print("Формат не валиден")
            sys.exit()
    if processing.check_data(data, keys, json_status=True):
        output = table_creator.creator(data, keys)
        print(output)
    else:
        sys.exit()
