from AbstractScriptGitElement import *
from ScriptGitTreeEntryChangesCollection import *


class ScriptGitCommit(AbstractScriptGitElement):
	"""
	| Wrapper class around _3S.CoDeSys.Git.GitIntegration.IGitCommit
	
	.. automethod:: __str__
	.. automethod:: __eq__
	.. automethod:: __ne__
	.. automethod:: __hash__
	
	"""
	
	@property
	def sha_string(self) -> str:
		"""
		| Gets the 40 character sha1 of this commit.
		
		"""
		pass
	
	@property
	def author_string(self) -> str:
		"""
		| Gets the author of this commit.
		
		"""
		pass
	
	@property
	def date_string(self) -> str:
		"""
		| Gets the date of this commit.
		
		"""
		pass
	
	@property
	def message_short_string(self) -> str:
		"""
		| Gets the short commit message.
		
		"""
		pass
	
	@property
	def message_string(self) -> str:
		"""
		| Gets the commit message.
		
		"""
		pass
	
	@property
	def tree_entry_changes(self) -> ScriptGitTreeEntryChangesCollection:
		"""
		| Gets the changes.
		
		"""
		pass
	
	
	def __str__(self) -> str:
		"""
		| see "git log" command
		
		"""
		pass
	
	def __eq__(self, other: ScriptGitCommit) -> bool:
		"""
		| Python magic method __eq__
		
		"""
		pass
	
	def __ne__(self, other: ScriptGitCommit) -> bool:
		"""
		| Python magic method __ne__
		
		"""
		pass
	
	def __hash__(self) -> int:
		"""
		| Python magic method __hash__
		
		"""
		pass