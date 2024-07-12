from enum import Enum


class ScriptGitMergeStatus(Enum):
	"""
	| Extends the GitMergeStatus-Enum with the Codesys Conflicts for scripting.
	
	"""
	
	UpToDate = 0
	"""
	| Merge was up-to-date.
	
	"""
	
	FastForward = 1
	"""
	| Fast-forward merge.
	
	"""
	
	NonFastForward = 2
	"""
	| Non-fast-forward merge.
	
	"""
	
	Conflicts = 3
	"""
	| Merge resulted in git conflicts.
	
	"""

	RelationshipIssues = 4
	"""
	| Merge resulted in Codesys conflicts.
	
	"""
    