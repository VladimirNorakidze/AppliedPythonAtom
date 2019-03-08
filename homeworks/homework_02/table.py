#!/usr/bin/env python
# coding: utf-8

import sys
from for_table import import_data, processing, table_creator

if __name__ == '__main__':
    filename = sys.argv[1]

    data, json_status = import_data.opening(filename)
    if not json_status:
        data = processing.data_to_json(data)
    table_creator.creator(data)
