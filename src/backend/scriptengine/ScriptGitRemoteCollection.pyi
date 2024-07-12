from collections.abc import Iterable
from ScriptGitRemote import *


class ScriptGitRemoteCollection(list):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitRemoteCollection.
	
	.. automethod:: __iter__
	.. automethod:: __next__
	.. automethod:: __str__
	.. automethod:: __len__
	.. automethod:: __contains__
	.. automethod:: __getitem__
	
	"""
	
	def __iter__(self) -> Iterable[ScriptGitRemote]:
		"""
		
		"""
		pass
	
	def __next__(self) -> ScriptGitRemote:
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
	
	def __contains__(self, remoteName: str) -> bool:
		"""
		| Python magic method __contains__
		
		"""
		pass
	
	def __getitem__(self, remoteName: str) -> ScriptGitRemote:
		"""
		| Indexer
		
		:type remoteName: str
		:param remoteName: Name of the remoteW
		
		"""
		pass