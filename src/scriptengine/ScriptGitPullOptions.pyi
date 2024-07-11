from GitFastForwardStrategy import *
from GitResolveFileConflictStrategy import *


class ScriptGitPullOptions(object):
	"""
	| Wrapper around _3S.CoDeSys.Git.GitIntegration.IGitPullOptions.
	
	"""
	
	@property
	def fail_on_conflict(self) -> bool:
		"""
		| If set, do not create conflicts, but stop and return an error
		| result after finding the first conflict.
		
		"""
		pass
	
	@property
	def commit_on_success(self) -> bool:
		"""
		| Automatically create a merge commit, if merging results in no conflict.
		| This includes conlficts, that have been resolved automatically.
		
		"""
		pass
	
	@property
	def fast_forward_strategy(self) -> GitFastForwardStrategy:
		"""
		| Defines, if the branch tip should be moved forward instead of creating
		| an automatic merge commit (see "commit_on_success") - if applicable.
		
		"""
		pass
	
	@property
	def resolve_file_conflict_strategy(self) -> GitResolveFileConflictStrategy:
		"""
		| Defines how to automatically resolve conflicts.
		
		"""
		pass
	
	@property
	def use_auto_merger(self) -> bool:
		"""
		| Defines, whether to apply CODESYS' "ProjectCompare.IObject3WayMerger" for conflicts.
		| These are only applied, if "resolve_file_conflict_strategy" is set to
		| "GitResolveFileConflictStrategy.Normal".
		
		"""
		pass