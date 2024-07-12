from AbstractScriptGitElement import *


class ScriptGitBranch(AbstractScriptGitElement):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitBranch.
	
	.. automethod:: __str__
	.. automethod:: __eq__
	.. automethod:: __ne__
	.. automethod:: __hash__
	
	"""
	
	@property
	def canonical_name(self) -> str:
		"""
		| Gets the canonical name of the branch.
		
		"""
		pass
	
	@property
	def friendly_name(self) -> str:
		"""
		| Gets the friendly name of the branch.
		
		"""
		pass
	
	@property
	def is_current_repository_head(self) -> bool:
		"""
		| Returns true, if the branch is the current branch.
		
		"""
		pass
	
	@property
	def is_remote(self) -> bool:
		"""
		| Returns true, if the branch is a remote branch.
		
		"""
		pass
	
	@property
	def is_tracking(self) -> bool:
		"""
		| Returns true, if the branch tracks a remote branche.
		
		"""
		pass
	
	@property
	def remote_name(self) -> str:
		"""
		| Gets the name of the remote, if the branch is a remote branch.
		
		"""
		pass
	
	@property
	def upstream_branch_canonical_name(self) -> str:
		"""
		| Gets the upstream canonical name of a tracked branch.
		
		"""
		pass
	
	@property
	def tracked_branch(self) -> ScriptGitBranch:
		"""
		| Gets the tracked branch object.
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		| See "git branch" command
		
		"""
		pass
	
	def __eq__(self, other: ScriptGitBranch) -> bool:
		"""
		| Python magic method __eq__
		
		"""
		pass
	
	def __ne__(self, other: ScriptGitBranch) -> bool:
		"""
		| Python magic method __ne__
		
		"""
		pass
	
	def __hash__(self) -> int:
		"""
		| Python magic method __hash__
		
		"""
		pass