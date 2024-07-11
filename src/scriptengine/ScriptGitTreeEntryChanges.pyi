from AbstractScriptGitElement import *
from GitChangeKind import *


class ScriptGitTreeEntryChanges(AbstractScriptGitElement):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitTreeEntryChanges.
	
	.. automethod:: __str__
	.. automethod:: __eq__
	.. automethod:: __ne__
	.. automethod:: __hash__
	
	"""
	
	@property
	def path(self) -> str:
		"""
		| Gets the path of the changed item.
		
		"""
		pass
	
	@property
	def mode_string(self) -> str:
		"""
		| Gets the change mode as string.
		
		"""
		pass
	
	@property
	def status_string(self) -> str:
		"""
		| Gets the change status as string.
		
		"""
		pass
	
	@property
	def status(self) -> GitChangeKind:
		"""
		| Gets the change status.
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		
		"""
		pass
	
	def __eq__(self, other: ScriptGitTreeEntryChanges) -> bool:
		"""
		| Python magic method __eq__
		
		"""
		pass
	
	def __ne__(self, other: ScriptGitTreeEntryChanges) -> bool:
		"""
		| Python magic method __ne__
		
		"""
		pass
	
	def __hash__(self) -> int:
		"""
		| Python magic method __hash__
		
		"""
		pass