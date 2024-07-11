from collections.abc import Iterable
from ScriptGitCommit import *


class ScriptGitCommitCollection(list):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitCommitLog.
	
	.. automethod:: __iter__
	.. automethod:: __next__
	.. automethod:: __str__
	.. automethod:: __len__
	.. automethod:: __getitem__
	
	"""
	
	def __iter__(self) -> Iterable[ScriptGitCommit]:
		"""
		
		"""
		pass
	
	def __next__(self) -> ScriptGitCommit:
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
		
		:rtype: int
		:returns: Number of items.
		
		"""
		pass
	
	def __getitem__(self, index: int) -> ScriptGitCommit:
		"""
		| Indexer
		
		:type index: int
		:param index: Index of the commit in the collection
		
		"""
		pass