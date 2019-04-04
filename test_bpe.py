#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
import codecs

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from learn_bpe import learn_bpe
from apply_bpe import BPE



if __name__ == '__main__':

    # raw data를 읽어 vocab 제작
    infile = codecs.open(os.path.join(currentdir, 'corpus.en'), encoding='utf-8')
    outfile = codecs.open(os.path.join(currentdir, 'vocap.out'), 'w', encoding='utf-8')
    learn_bpe(infile, outfile, 1000)
    infile.close()
    outfile.close()

    # vocap을 읽어 
    with codecs.open(os.path.join(currentdir, 'vocap.out'), encoding='utf-8') as bpefile:
        bpe = BPE(bpefile)

    f = open( 'corpus.en', 'r')
    f1 = open('corpus_space.en', 'w')
    while True:
        line = f.readline()
        if not line: break
        # print(line)
        out=bpe.process_line(line)
        f1.write(out)
        # print(out)
        b=0
    f.close()
    f1.close()
