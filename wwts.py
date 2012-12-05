#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import traceback
import re
import codecs
import lib.bayes as bayes

def main():
    parser = argparse.ArgumentParser(description='Who wrote this shit?')
    parser.add_argument('-F', '--file', required=True, help='Input file')
    parser.add_argument('-T', '--tag', help='Tag, e.g. \'Thaddeus T. Grugq\' or \'@thegrugq\'')
    parser.add_argument('-t', '--train', action='store_true', help='Training mode')
    parser.add_argument('-g', '--guess', action='store_true', help='Guessing mode')
    args = parser.parse_args()
    
    wwts = bayes.Bayes()
    try:
        wwts.load()
    except:
        if args.train:
            pass
        elif args.guess:
            parser.error('cannot load identity file')

    if args.train:
        if not args.tag:
            parser.error('argument -T/--tag is required.')
        with codecs.open(args.file, 'r', encoding='utf-8') as content:
            wwts.train(args.tag, content.read())
            wwts.save()
    elif args.guess:
        with codecs.open(args.file, 'r', encoding='utf-8') as content:
            print wwts.guess(content.read())
    else:
        parser.error('argument -t/--train or -g/--guess is required')


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt, e:
        raise e
    except SystemExit, e:
        raise e
    except Exception, e:
        print str(e)
        traceback.print_exc()
        sys.exit(1)
