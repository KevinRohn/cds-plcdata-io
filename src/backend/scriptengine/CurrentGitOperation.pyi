from enum import Enum


class CurrentGitOperation(Enum):
	"""
	| Determines the pending operation of a git repository - ie, whether
	| an operation (merge, cherry-pick, etc) is in progress.
	
	"""
	
	None = 0
	"""
	| No operation is in progress.
	
	"""
	
	Merge = 1
	"""
	| A merge is in progress.
	
	"""
	
	Revert = 2
	"""
	| A revert is in progress.
	
	"""
	
	RevertSequence = 3
	"""
	| A sequencer revert is in progress.
	
	"""
	
	CherryPick = 4
	"""
	| A cherry-pick is in progress.
	
	"""
	
	CherryPickSequence = 5
	"""
	| A sequencer cherry-pick is in progress.
	
	"""
	
	Bisect = 6
	"""
	| A bisect is in progress.
	
	"""
	
	Rebase = 7
	"""
	| A rebase is in progress.
	
	"""
	
	RebaseInteractive = 8
	"""
	| A rebase --interactive is in progress.
	
	"""
	
	RebaseMerge = 9
	"""
	| A rebase --merge is in progress.
	
	"""
	
	ApplyMailbox = 10
	"""
	| A mailbox application (am) is in progress.
	
	"""

	ApplyMailboxOrRebase = 11
	"""
	| A mailbox application (am) or rebase is in progress.
	
	"""