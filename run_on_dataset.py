# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import csv
from serpextract import extract


def main(csv_file_name):
    """Read lines from csv file formatted as <i>,<url> and output results to console."""
    serps = 0
    nonserps = 0
    with open(csv_file_name, 'r') as f:
        reader = csv.reader(f)
        for i, url in reader:
            result = extract(url)
            is_serp = result is not None
            if is_serp:
                serps += 1
            else:
                nonserps += 1
            print('{},{},{},{},{}'.format(i,
                                          is_serp,
                                          result.engine_name if is_serp else None,
                                          result.keyword if is_serp else None,
                                          url).encode(encoding='utf-8'))
    print('Total SE: {}, non-SE: {}'.format(serps, nonserps))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python run_on_dataset.py <csv-file-name>')
        exit(0)

    main(sys.argv[1])
