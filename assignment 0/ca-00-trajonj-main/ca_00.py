"""ca_00.py: Starter file to run assignment 0.
DO NOT MODIFY THIS FILE.
"""

__author__ = "Shishir Shah"
__version__ = "1.0.0"
__copyright__ = "Copyright 2022 by Shishir Shah, Quantitative Imaging Laboratory (QIL), Department of Computer  \
                Science, University of Houston.  All rights reserved.  This software is property of the QIL, and  \
                should not be distributed, reproduced, or shared online, without the permission of the author."

import cipher
import fileio
import logging
import sys


def main():
    """ The main function that parses input arguments, calls the appropriate
     method and writes the output image"""

    # Initialize logging
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="output/logfile.log",
                        filemode="w",
                        format=Log_Format,
                        level=logging.INFO)
    logger = logging.getLogger()
    # handler = logging.FileHandler('output/logfile.log')
    # logger.addHandler(handler)
    logger.info('Logging initialized.')

    # Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-kv", "--kvfile", dest="kvfile",
                        help="specify the name of the key-value file", metavar="KVFILE")

    parser.add_argument("-m", "--messages", dest="messages",
                        help="specify the file that has messages to be ciphered", metavar="MESSAGES")

    args = parser.parse_args()

    if args.kvfile is None:
        print("Please specify the name of file that has the cipher code")
        print("use the -h option to see usage information")
        logger.error('Input cipher code file name not specified.')
        sys.exit(1)
    if args.messages is None:
        print("Please specify the name of file that has messages to be ciphered")
        print("use the -h option to see usage information")
        logger.error('Input file name with messages to be ciphered not specified.')
        sys.exit(1)
    else:
        outputDir = 'output/'
        try:
            list1, list2 = fileio.read_keyvalue(args.kvfile)
            logger.info('Image loading succeeded.')
        except:
            logger.error('Error loading cipher code file.')
            sys.exit(1)
        try:
            cipherdict = cipher.make_dictionary(list1, list2)
            logger.info('Creation of cipher dictionary succeeded.')
        except:
            logger.error('Error creating cipher dictionary.')
            sys.exit(1)
        try:
            m = fileio.read_message(args.messages)
            logger.info('Messages to be ciphered read successfully.')
        except:
            logger.error('Error reading file with messages to be ciphered.')
            sys.exit(1)
        try:
            for message in m:
                ciphered_message = cipher.cipher(message, cipherdict)
                fileio.write_ciphered_messages(ciphered_message, 'output/ciphered_messages.txt')
            logger.info('Ciphered messages written successfully.')
        except:
            logger.error('Error ciphering and writing messages.')
            sys.exit(1)


if __name__ == "__main__":
    main()
