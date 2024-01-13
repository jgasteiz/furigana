#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# $ python -m 活版印刷の流れを汲む出版作業では

import sys

from furigana.furigana import get_plaintext

if __name__ == "__main__":
    print(get_plaintext(sys.argv[1]))
