#!/usr/bin/env python 
import time
import sys


def snap_crackle_pop(start = 0, cieling = 100):
	"""
	Takes as input a start number and a cieling to count up to.  Prints "snap" if 
	divisable by 3, "crackle" if divisable by 5, and "pop" if 
	divisable by 10.
	"""
	print "Snap Crackle Pop counting from {} up to {}".format(start, cieling)
	cieling+=1
	for num in range(0, cieling):
		time.sleep(1)
		output = ""
		if not num % 3:
			output += "Snap "
		if not num % 5:
			output += "Crackle "
		if not num % 10:
			output += "Pop "
		print output or str(num)
	print "Snap Crackle Pop game is finished!"

if __name__ == "__main__":
	start_game()
	try: 
		if len(sys.argv[:]) == 1:
				val = int(raw_input("What number should we use as the cieling?"))
				snap_crackle_pop(cieling = val)
		else: 
			snap_crackle_pop(cieling = int((sys.argv[1:][0])))
	except ValueError:
	 		print "Invalid Entry.  Please enter a number."
	