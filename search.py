import glob, os
import threading
import time
from optparse import OptionParser

options = OptionParser(usage='%prog [search values]', description='Search strings in the Heartbleed dump.')

def main():
    try:
        opts, args = options.parse_args()
        if len(args) < 1:
            options.print_help()
            return

	os.chdir("./dump")
	for a in args:
		for file in glob.glob("*.bin"):
			searchfile = open(file)
			for num, line in enumerate(searchfile, 1):
				if a in line:
					print "ARCHIVO:"+searchfile.name+" LINEA: "+str(num)
					print line
			searchfile.close()

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()