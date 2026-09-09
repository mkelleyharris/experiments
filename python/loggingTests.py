import time
import logging
import sys

logger = logging.getLogger('DiseaseCodeLookup')
logger.setLevel(logging.DEBUG)

# create a file handler

handler = logging.FileHandler('hello1234.log')
handler.setLevel(logging.DEBUG)

# create a logging format

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)



if __name__ == '__main__':
	print "something std"
	logger.debug("something")
	