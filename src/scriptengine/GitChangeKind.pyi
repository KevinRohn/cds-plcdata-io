from enum import Enum


class GitChangeKind(Enum):
	"""
	| The kind of changes that a Diff can report.
	
	"""
	
	Unmodified = 0
	"""
	| No changes detected.
	
	"""
	
	Added = 1
	"""
	| The file was added.
	
	"""
	
	Deleted = 2
	"""
	| The file was deleted.
	
	"""
	
	Modified = 3
	"""
	| The file content was modified.
	
	"""
	
	Renamed = 4
	"""
	| The file was renamed.
	
	"""
	
	Copied = 5
	"""
	| The file was copied.
	
	"""
	
	Ignored = 6
	"""
	| The file is ignored in the workdir.
	
	"""
	
	Untracked = 7
	"""
	| The file is untracked in the workdir.
	
	"""
	
	TypeChanged = 8
	"""
	| The type (i.e. regular file, symlink, submodule, ...)
	| of the file was changed.
	
	"""
	
	Unreadable = 9
	"""
	| Entry is unreadable.
	
	"""
	
	Conflicted = 10
	"""
	| Entry is currently in conflict.
	
	"""