from ScriptProject import *
from ScriptProjects import *
from typing import overload
from ScriptGitMergeOptions import *
from ScriptGitPullOptions import *


class ScriptDriverGitImpl(object):
	"""
	
	"""
	
	@overload
	def clone(self, stProjectLocation: str, stProjectName: str, sSourceUrl: str, gitProjectStoragePath: str, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> ScriptProject:
		"""
		| Clone a git repository into a new CODESYS Project
		| git-clone - Clone a repository into a new directory
		
		:type stProjectLocation: str
		:param stProjectLocation: Directory of the project files
		
		:type stProjectName: str
		:param stProjectName: Name of the project
		
		:type sSourceUrl: str
		:param sSourceUrl: Source URL of the repository
		
		:type gitProjectStoragePath: str
		:param gitProjectStoragePath: Directory of the local repository
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handeling project updates
		
		"""
		pass
	
	@overload
	def clone(self, stProjectLocation: str, stProjectName: str, sSourceUrl: str, gitProjectStoragePath: str, username: str, password: str, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> ScriptProject:
		"""
		| Clone a git repository into a new CODESYS Project
		| git-clone - Clone a repository into a new directory
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		"""
		pass
	
	def clone(self) -> ScriptProject:
		"""
		| Clone a git repository into a new CODESYS Project
		| git-clone - Clone a repository into a new directory
		
		:type stProjectLocation: str
		:param stProjectLocation: Directory of the project files
		
		:type stProjectName: str
		:param stProjectName: Name of the project
		
		:type sSourceUrl: str
		:param sSourceUrl: Source URL of the repository
		
		:type gitProjectStoragePath: str
		:param gitProjectStoragePath: Directory of the local repository
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handeling project updates
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		"""
		pass
	
	def recover_project(self, stProjectLocation: str, stProjectName: str, gitProjectStoragePath: str, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> ScriptProject:
		"""
		| Recover a CODESYS Project from a local git repository.
		
		:type stProjectLocation: str
		:param stProjectLocation: Directory of the project files
		
		:type stProjectName: str
		:param stProjectName: Name of the project
		
		:type gitProjectStoragePath: str
		:param gitProjectStoragePath: Directory of the local git repository
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handeling project updates
		
		"""
		pass
	
	def get_merge_options(self) -> ScriptGitMergeOptions:
		"""
		| Gets Git merge options.
		
		"""
		pass
	
	def get_pull_options(self) -> ScriptGitPullOptions:
		"""
		| Gets Git pull options.
		
		"""
		pass