from enum import Enum


class GitObjectStatus(Enum):
	"""
	| Calculated status of a CODESYS object.
	
	"""
	
	Nonexistent = (1 << 31)
	"""
	| The object doesn't exist.
	
	"""
	
	Unaltered = 0
	"""
	| The object hasn't been modified.
	
	"""
	
	NewInIndex = (1 << 0)
	"""
	| New object has been added to the Index. It's unknown from the Head.
	
	"""
	
	ModifiedInIndex = (1 << 1)
	"""
	| New version of a object has been added to the Index. A previous version exists in the Head.
	
	"""
	
	DeletedFromIndex = (1 << 2)
	"""
	| The deletion of a object has been promoted from the working directory to the Index. A previous version exists in the Head.
	
	"""
	
	RenamedInIndex = (1 << 3)
	"""
	| The renaming of a object has been promoted from the working directory to the Index. A previous version exists in the Head.
	
	"""
	
	TypeChangeInIndex = (1 << 4)
	"""
	| A change in type for a object has been promoted from the working directory to the Index. A previous version exists in the Head.
	
	"""
	
	NewInWorkdir = (1 << 7)
	"""
	| New object in the working directory, unknown from the Index and the Head.
	
	"""
	
	ModifiedInWorkdir = (1 << 8)
	"""
	| The object has been updated in the working directory. A previous version exists in the Index.
	
	"""
	
	DeletedFromWorkdir = (1 << 9)
	"""
	| The object has been deleted from the working directory. A previous version exists in the Index.
	
	"""
	
	TypeChangeInWorkdir = (1 << 10)
	"""
	| The object type has been changed in the working directory. A previous version exists in the Index.
	
	"""
	
	RenamedInWorkdir = (1 << 11)
	"""
	| The object has been renamed in the working directory.  The previous version at the previous name exists in the Index.
	
	"""
	
	Unreadable = (1 << 12)
	"""
	| The object is unreadable in the working directory.
	
	"""
	
	Ignored = (1 << 14)
	"""
	| The object is
	
	"""
	
	Conflicted = (1 << 15)
	"""
	| The object is
	
	"""
	
	Pending = (1 << 16)
	"""
	| The status for this object has not been retreived yet.
	
	"""