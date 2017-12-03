# coding=utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--program', required=True, dest='PROGRAM', help='Set program name')
parser.add_argument('-s', '--symbolic', dest='SYMBOLIC', default=True, help='Set enable symbolic execution')
parser.add_argument('-l', '--logging', dest='LOGGING', default=True, help='Set enable record logging')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')

args_results = parser.parse_args()
print 'Program name is :', args_results.PROGRAM
print 'Symbolic Execution Enabled ? ', args_results.SYMBOLIC
print 'Recording Log Enabled ? ', args_results.LOGGING
