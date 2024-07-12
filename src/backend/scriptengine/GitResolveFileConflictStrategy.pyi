from enum import Enum


class GitResolveFileConflictStrategy(Enum):
	"""
	| Defines how to handle file conflicts.
	| Our conflict handling relies on checkout of both conlficted versions of a file and then choosing
	| what to do with them.
	
	"""
	
	Normal = 0
	"""
	| Use the default behavior for handling file conflicts. 
	
	"""
	
	Ours = 1
	"""
	| For conflicting files, checkout the "ours" version of
	| the file from the index and use it as the resolved version.
	
	"""
	
	Theirs = 2
	"""
	| For conflicting files, checkout the "theirs" version of
	| the file from the index and use it as the resolved version.
	
	"""