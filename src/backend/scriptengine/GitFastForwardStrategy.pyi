from enum import Enum


class GitFastForwardStrategy(Enum):
	"""
	| Strategy used for merging.
	
	"""
	
	FastForwardIfPossible = 0
	"""
	| Default fast-forward strategy. If the merge.ff configuration option is set,
	| it will be used.  If it is not set, this will perform a fast-forward merge if
	| possible, otherwise a non-fast-forward merge that results in a merge commit.
	
	"""
	
	NoFastForward = 1
	"""
	| Do not fast-forward. Always creates a merge commit.
	
	"""
	
	FastForwardOnly = 2
	"""
	| Only perform fast-forward merges.
	
	"""