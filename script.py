#!/usr/bin/env python

# don't forget to make the file executable
# $ chmod +x script.py

__VERSION__ = 0.1


import sys
import logging
import argparse


def main():
	'''Main function'''
	# Logger pattern from 
	# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
	logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
	logger = logging.getLogger()
	# modify filename!
	fileHandler = logging.FileHandler('script.log')
	fileHandler.setFormatter(logFormatter)
	logger.addHandler(fileHandler)
	consoleHandler = logging.StreamHandler()
	consoleHandler.setFormatter(logFormatter)
	logger.addHandler(consoleHandler)
	logger.setLevel(logging.DEBUG)

	# argparse insights from https://pymotw.com/3/argparse/
	parser = argparse.ArgumentParser(description='Processes the file.')
	parser.add_argument('filename', type=str, 
						help='File to be processed')
	parser.add_argument('-d', action='store_true', dest='DEBUG', default=False,
						help='Force debug mode with detailed logging')
	parser.add_argument('--output', dest='output_file', type=str, default=None,
						help='Filename for results.')
	parser.add_argument('--version', action='version',
						version=f'Script.py Version {__VERSION__}',
						help='Show version information')
	args = parser.parse_args()
	logger.debug(f'Script {__VERSION__} called with \
DEBUG={args.DEBUG}, filename={args.filename}, output_file={args.output_file}.')


if __name__ == '__main__':
	main()