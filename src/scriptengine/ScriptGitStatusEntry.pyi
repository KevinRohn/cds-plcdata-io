from AbstractScriptGitElement import *
from GitObjectStatus import *


class ScriptGitStatusEntry(AbstractScriptGitElement):
	"""
	| Wrapper of _3S.CoDeSys.Git.GitIntegration.IGitStatusEntry.
	
	.. automethod:: __str__
	.. automethod:: __eq__
	.. automethod:: __ne__
	.. automethod:: __hash__
	
	"""
	
	@property
	def git_object_status(self) -> GitObjectStatus:
		"""
		| see _3S.CoDeSys.Git.GitIntegration.GitObjectStatus
		
		"""
		pass
	
	@property
	def file_path(self) -> str:
		"""
		| path of the file
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		
		"""
		pass
	
	def __eq__(self, other: ScriptGitStatusEntry) -> bool:
		"""
		| Python magic method __eq__
		
		"""
		pass
	
	def __ne__(self, other: ScriptGitStatusEntry) -> bool:
		"""
		| Python magic method __ne__
		
		"""
		pass
	
	def __hash__(self) -> int:
		"""
		| Python magic method __hash__
		
		"""
		pass