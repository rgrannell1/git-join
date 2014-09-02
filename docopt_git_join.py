#!/usr/bin/env python

"""
Usage:
    git-join [<branchname>]

Description:
	Incorperate changes from another branch into the current branch,
	and delete the other branch. This command wraps git merge.

Options:
    <branchname>     The name of the branch to join into the current branch.

"""

from docopt   import docopt
from git_join import main





if __name__ == '__main__':

	arguments = docopt(__doc__, version = "0.1.0")
	main(arguments)
