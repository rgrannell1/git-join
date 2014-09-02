#!/usr/bin/env python

import sys
from subprocess import call








def branch_exists (branchname):
	return True

def delete_branch (branchname):

	call(["git branch", "-d", branchname])





def main (args):

	branchname = args['<branchname>']

	if not branch_exists(branchname):
		raise Exception("error: pathspec '" + branchname + "' did not match any branch name.")
		sys.exit(1)

	#delete_branch(branchname)

