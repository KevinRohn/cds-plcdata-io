from ScriptGitBranch import *
from collections.abc import Iterable


class ScriptGitBranchCollection(list):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitBranchCollection.
	
	.. automethod:: __iter__
	.. automethod:: __next__
	.. automethod:: __str__
	.. automethod:: __len__
	.. automethod:: __contains__
	.. automethod:: __getitem__
	
	"""
	
	@property
	def current_repository_head(self) -> ScriptGitBranch:
		"""
		| Gets the branch object witch is the current head.
		| returns null if there is no current head.
		
		"""
		pass
	
	
	def __iter__(self) -> Iterable[ScriptGitBranch]:
		"""
		
		"""
		pass
	
	def __next__(self) -> ScriptGitBranch:
		"""
		
		"""
		pass
	
	def __str__(self) -> str:
		"""
		
		"""
		pass
	
	def __len__(self) -> int:
		"""
		| Python magic method __len__
		
		"""
		pass
	
	def __contains__(self, branchName: str) -> bool:
		"""
		| Python magic method __contains__
		
		"""
		pass
	
	def __getitem__(self, branchName: str) -> ScriptGitBranch:
		"""
		| Indexer
		
		:type branchName: str
		:param branchName: Name of the branch
		
		"""
		pass