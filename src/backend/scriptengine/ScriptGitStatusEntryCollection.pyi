from collections.abc import Iterable
from ScriptGitStatusEntry import *
from ScriptObject import *


class ScriptGitStatusEntryCollection(list):
	"""
	| Wrapper of _3S.CoDeSys.Git.GitIntegration.IGitRepositoryStatus.
	
	.. automethod:: __iter__
	.. automethod:: __next__
	.. automethod:: __str__
	.. automethod:: __len__
	.. automethod:: __contains__
	.. automethod:: __getitem__
	
	"""
	
	def __iter__(self) -> Iterable[ScriptGitStatusEntry]:
		"""
		
		"""
		pass
	
	def __next__(self) -> ScriptGitStatusEntry:
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
	
	def __contains__(self, extendedObject: ScriptObject) -> bool:
		"""
		| Python magic method __contains__
		
		"""
		pass
	
	def __getitem__(self, extendedObject: ScriptObject) -> list[ScriptGitStatusEntry]:
		"""
		| Indexer
		
		:type extendedObject: ScriptObject
		:param extendedObject: Script object to get status entry list from
		
		"""
		pass