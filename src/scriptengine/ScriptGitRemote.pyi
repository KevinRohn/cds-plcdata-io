from AbstractScriptGitElement import *


class ScriptGitRemote(AbstractScriptGitElement):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitRemote.
	
	.. automethod:: __str__
	.. automethod:: __eq__
	.. automethod:: __ne__
	.. automethod:: __hash__
	
	"""
	
	@property
	def name(self) -> str:
		"""
		| Name of the remote (alias).
		
		"""
		pass
	
	@property
	def url(self) -> str:
		"""
		| URL of the remote.
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		| see "git remote -v" command
		
		"""
		pass
	
	def __eq__(self, other: ScriptGitRemote) -> bool:
		"""
		| Python magic method __eq__
		
		"""
		pass
	
	def __ne__(self, other: ScriptGitRemote) -> bool:
		"""
		| Python magic method __ne__
		
		"""
		pass
	
	def __hash__(self) -> int:
		"""
		| Python magic method __hash__
		
		"""
		pass