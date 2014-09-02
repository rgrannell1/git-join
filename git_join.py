#!/usr/bin/env python

import sys








def branch_exists (branchname):
	return True





def main (args):

	branchname = args['<branchname>']

	if not branch_exists(branchname):
		raise Exception("error: pathspec '" + branchname + "' did not match any branch name.")
		sys.exit(1)

