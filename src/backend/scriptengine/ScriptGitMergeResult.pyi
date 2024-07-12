from AbstractScriptGitElement import *
from ScriptGitMergeStatus import *
from ScriptGitCommit import *


class ScriptGitMergeResult(AbstractScriptGitElement):
	"""
	| Merge result.
	
	.. automethod:: __str__
	
	"""
	
	@property
	def merge_status(self) -> ScriptGitMergeStatus:
		"""
		| Status of the merge.
		
		"""
		pass
	
	@property
	def git_commit(self) -> ScriptGitCommit:
		"""
		| Merge commit.
		
		"""
		pass
	
	@property
	def has_conflicts(self) -> bool:
		"""
		| Returns true, if the merge resulted in a conflict.
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		
		"""
		pass