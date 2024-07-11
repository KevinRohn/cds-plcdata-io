from ScriptGitStatusEntryCollection import *
from ScriptGitCommitCollection import *
from ScriptObject import *
from ScriptGitCommit import *
from ScriptGitBranchCollection import *
from ScriptGitBranch import *
from ScriptProject import *
from typing import overload
from ScriptGitMergeResult import *
from ScriptGitMergeOptions import *
from ScriptGitRemoteCollection import *
from ScriptGitRemote import *
from CurrentGitOperation import *
from ScriptGitPullOptions import *


class GitScriptProject(object):
	"""
	
	"""
	
	@property
	def project_handle(self) -> int:
		"""
		| Gets the current project handle.
		
		"""
		pass
	
	@property
	def git_config_user_name(self) -> str:
		"""
		| Gets the user name from the git configuration.
		| Makes use of the "user.name" setting.
		
		"""
		pass
	
	@property
	def git_config_user_email(self) -> str:
		"""
		| Gets the user email from the git configuration.
		| Makes use of the "user.email" setting.
		
		"""
		pass
	
	@property
	def git_config_init_default_branch(self) -> str:
		"""
		| Gets the default branch name.
		| Makes use of the "init.defaultBranch" setting.
		
		"""
		pass
	
	
	def init(self, gitProjectStoragePath: str) -> None:
		"""
		| Add the given project to Git version control.
		| NO INITIAL COMMIT!
		| git-init - Create an empty Git repository or reinitialize an existing one
		
		:type gitProjectStoragePath: str
		:param gitProjectStoragePath: Directory of the local git repository
		
		"""
		pass
	
	def de_init(self, cleanUpFileSystem: bool=False) -> None:
		"""
		| Removes the Git connection from the project and optionally deletes the working tree directory.
		
		:type cleanUpFileSystem: bool
		:param cleanUpFileSystem: Flag for deleting the working tree directory
		
		"""
		pass
	
	def status(self) -> ScriptGitStatusEntryCollection:
		"""
		| Retrieves the current status for the working tree.
		| git-status - Show the working tree status
		
		"""
		pass
	
	def log(self, extendedObject: ScriptObject=None) -> ScriptGitCommitCollection:
		"""
		| Lookup and enumerate commits in the repository.
		| git-log - Show commit logs
		
		:type extendedObject: ScriptObject
		:param extendedObject: ScriptObject to get the log from
		
		"""
		pass
	
	def add_all(self) -> None:
		"""
		| Adds all unstaged changes to the index.
		| git-add --all - Add file contents to the index, all files in the entire working tree are concerned
		
		"""
		pass
	
	def commit(self, sCommitMessage: str, sUserName: str, sUserEmail: str, bAllowEmptyCommits: bool=False, bAmendCommit: bool=False) -> ScriptGitCommit:
		"""
		| Commits all staged changes (the index) to the repository.
		| git-commit - Record changes to the repository
		
		:type sCommitMessage: str
		:param sCommitMessage: Commit message
		
		:type sUserName: str
		:param sUserName: Username
		
		:type sUserEmail: str
		:param sUserEmail: E-mail
		
		:type bAllowEmptyCommits: bool
		:param bAllowEmptyCommits: Flag for creating a commit without any changes
		
		:type bAmendCommit: bool
		:param bAmendCommit: Flag for amending the last commit
		
		"""
		pass
	
	def commit_complete(self, sCommitMessage: str, sUserName: str, sUserEmail: str, bAllowEmptyCommits: bool=False, bAmendCommit: bool=False) -> ScriptGitCommit:
		"""
		| Adds all unstaged changes to the index and then commits the index to the repository.
		| git add --all + git commit
		| git-add - Add file contents to the index
		| git-commit - Record changes to the repository
		
		:type sCommitMessage: str
		:param sCommitMessage: Commit message
		
		:type sUserName: str
		:param sUserName: Username
		
		:type sUserEmail: str
		:param sUserEmail: E-mail
		
		:type bAllowEmptyCommits: bool
		:param bAllowEmptyCommits: Flag for creating a commit without any changes
		
		:type bAmendCommit: bool
		:param bAmendCommit: Flag for amending the last commit
		
		"""
		pass
	
	def branch(self) -> ScriptGitBranchCollection:
		"""
		| Retreives information on currently existing branches.
		| git-branch --vv - List branches
		
		"""
		pass
	
	def branch_show_current(self) -> ScriptGitBranch:
		"""
		| Gets the current branch.
		| git branch --show-current
		
		"""
		pass
	
	@overload
	def branch_copy(self, oldBranchName: str, newBranchName: str, force: bool=False, checkout: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Create a new branch from an existing branch name or commit SHA1.
		| git branch (-c | -C) [<oldbranch>] <newbranch> - Copy a branch and the corresponding reflog.
		
		:type oldBranchName: str
		:param oldBranchName: Name of the branch or commit to copy
		
		:type newBranchName: str
		:param newBranchName: Name of the new branch that will be created
		
		:type force: bool
		:param force: Flag to force copy
		
		:type checkout: bool
		:param checkout: Flag to checkout the created branch
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates. Only effective, if checkout is True
		
		"""
		pass
	
	@overload
	def branch_copy(self, oldScriptGitBranch: ScriptGitBranch, newBranchName: str, force: bool=False, checkout: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Create a new branch from an existing branch name or commit SHA1.
		| git branch (-c | -C) [<oldbranch>] <newbranch> - Copy a branch and the corresponding reflog.
		
		:type oldScriptGitBranch: ScriptGitBranch
		:param oldScriptGitBranch: Branch object of the branch to copy
		
		:type newBranchName: str
		:param newBranchName: Name of the new branch that will be created
		
		:type force: bool
		:param force: Flag to force copy
		
		:type checkout: bool
		:param checkout: Flag to checkout the created branch
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates. Only effective, if checkout is True
		
		"""
		pass
	
	@overload
	def branch_copy(self, newBranchName: str, force: bool=False, checkout: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Create a new branch from an existing branch name or commit SHA1.
		| git branch (-c | -C) [<oldbranch>] <newbranch> - Copy a branch and the corresponding reflog.
		
		:type newBranchName: str
		:param newBranchName: Name of the new branch that will be created (using current branch)
		
		:type force: bool
		:param force: Flag to force copy
		
		:type checkout: bool
		:param checkout: Flag to checkout the created branch
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates. Only effective, if checkout is True
		
		"""
		pass
	
	@overload
	def branch_copy(self, scriptGitCommit: ScriptGitCommit, newBranchName: str, force: bool=False, checkout: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Create a new branch from an existing branch name or commit SHA1.
		| git branch (-c | -C) [<oldbranch>] <newbranch> - Copy a branch and the corresponding reflog.
		
		:type scriptGitCommit: ScriptGitCommit
		:param scriptGitCommit: Commit object of the commit to copy
		
		:type newBranchName: str
		:param newBranchName: Name of the new branch that will be created
		
		:type force: bool
		:param force: Flag to force copy
		
		:type checkout: bool
		:param checkout: Flag to checkout the created branch
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates. Only effective, if checkout is True
		
		"""
		pass
	
	def branch_copy(self) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Create a new branch from an existing branch name or commit SHA1.
		| git branch (-c | -C) [<oldbranch>] <newbranch> - Copy a branch and the corresponding reflog.
		
		:type oldBranchName: str
		:param oldBranchName: Name of the branch or commit to copy
		
		:type oldScriptGitBranch: ScriptGitBranch
		:param oldScriptGitBranch: Branch object of the branch to copy
		
		:type scriptGitCommit: ScriptGitCommit
		:param scriptGitCommit: Commit object of the commit to copy
		
		:type newBranchName: str
		:param newBranchName: Name of the new branch that will be created
		
		:type force: bool
		:param force: Flag to force copy
		
		:type checkout: bool
		:param checkout: Flag to checkout the created branch
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates. Only effective, if checkout is True
		
		"""
		pass
	
	@overload
	def branch_delete(self, branchName: str, force: bool=False) -> None:
		"""
		| Delete the branch with the given name
		| git-branch (-d | -D) <branchname> - delete branches
		
		:type branchName: str
		:param branchName: Name of the branch to delete
		
		:type force: bool
		:param force: Flag to force deletion
		
		"""
		pass
	
	@overload
	def branch_delete(self, scriptGitBranch: ScriptGitBranch, force: bool=False) -> None:
		"""
		| Delete the branch with the given name
		| git-branch (-d | -D) <branchname> - delete branches
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to delete
		
		:type force: bool
		:param force: Flag to force deletion
		
		"""
		pass
	
	def branch_delete(self) -> None:
		"""
		| Delete the branch with the given name
		| git-branch (-d | -D) <branchname> - delete branches
		
		:type branchName: str
		:param branchName: Name of the branch to delete
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to delete
		
		:type force: bool
		:param force: Flag to force deletion
		
		"""
		pass
	
	@overload
	def checkout(self, branchName: str, force: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Checkout branch with the given name.
		| git-checkout [-f | --force] <branch> - Switch branches
		| The project gets resynchronized to match the working tree.
		
		:type branchName: str
		:param branchName: Name of the branch or commit to checkout
		
		:type force: bool
		:param force: Flag to force checkout
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def checkout(self, scriptGitBranch: ScriptGitBranch, force: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Checkout branch with the given name.
		| git-checkout [-f | --force] <branch> - Switch branches
		| The project gets resynchronized to match the working tree.
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to checkout
		
		:type force: bool
		:param force: Flag to force checkout
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def checkout(self, scriptGitCommit: ScriptGitCommit, force: bool=False, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Checkout commit.
		| git-checkout [-f | --force] <commit> - Checkout commit
		| The project gets resynchronized to match the working tree.
		
		:type scriptGitCommit: ScriptGitCommit
		:param scriptGitCommit: Commit object of the commit to checkout
		
		:type force: bool
		:param force: Flag to force checkout
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	def checkout(self) -> tuple[ScriptProject, ScriptGitBranch]:
		"""
		| Checkout branch with the given name.
		| git-checkout [-f | --force] <branch> - Switch branches
		| The project gets resynchronized to match the working tree.
		
		:type branchName: str
		:param branchName: Name of the branch or commit to checkout
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to checkout
		
		:type scriptGitCommit: ScriptGitCommit
		:param scriptGitCommit: Commit object of the commit to checkout
		
		:type force: bool
		:param force: Flag to force checkout
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def merge(self, branchName: str, userName: str, userEmail: str, scriptGitMergeOptions: ScriptGitMergeOptions=None, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Merges the branch with the given name into the current branch.
		| git-merge - Join two or more development histories together
		
		:type branchName: str
		:param branchName: Name of the branch to merge into current branch
		
		:type userName: str
		:param userName: Username
		
		:type userEmail: str
		:param userEmail: E-mail
		
		:type scriptGitMergeOptions: ScriptGitMergeOptions
		:param scriptGitMergeOptions: Merge Options
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def merge(self, scriptGitBranch: ScriptGitBranch, userName: str, userEmail: str, scriptGitMergeOptions: ScriptGitMergeOptions=None, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Merges the branch with the given name into the current branch.
		| git-merge - Join two or more development histories together
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to merge into current branch
		
		:type userName: str
		:param userName: Username
		
		:type userEmail: str
		:param userEmail: E-mail
		
		:type scriptGitMergeOptions: ScriptGitMergeOptions
		:param scriptGitMergeOptions: Merge Options
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	def merge(self) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Merges the branch with the given name into the current branch.
		| git-merge - Join two or more development histories together
		
		:type branchName: str
		:param branchName: Name of the branch to merge into current branch
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to merge into current branch
		
		:type userName: str
		:param userName: Username
		
		:type userEmail: str
		:param userEmail: E-mail
		
		:type scriptGitMergeOptions: ScriptGitMergeOptions
		:param scriptGitMergeOptions: Merge Options
        
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	def reset_mixed_all(self) -> None:
		"""
		| Resets the index but not the working tree.
		| git-reset --mixed - Reset current HEAD to the specified state
		
		"""
		pass
	
	def discard_all_changes(self, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> ScriptProject:
		"""
		| Discard all changes.
		| Does a git reset --hard and additionally removes all untracked files.
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	def path(self) -> str:
		"""
		| Gets the path of the working tree.
		
		"""
		pass
	
	def has_working_tree(self) -> bool:
		"""
		| Checks if the given project handle has a git working tree.
		
		"""
		pass
	
	def has_working_object(self, extendedObject: ScriptObject) -> bool:
		"""
		| Checks if the given object has a git working tree object (is under version control).
		
		:type extendedObject: ScriptObject
		:param extendedObject: ScriptObject to check for working tree object
		
		"""
		pass
	
	def has_uncommitted_changes(self) -> bool:
		"""
		| Checks if there are uncommitted changes.
		
		"""
		pass
	
	def has_working_tree_changes(self) -> bool:
		"""
		| Checks if there are changes in the working tree which are not staged.
		
		"""
		pass
	
	def has_index_changes(self) -> bool:
		"""
		| Checks if there are changes in the index which are not committed.
		
		"""
		pass
	
	def remote(self) -> ScriptGitRemoteCollection:
		"""
		| Lookup and enumerate remotes in the repository.
		| git-remote - Manage set of tracked repositories
		
		"""
		pass
	
	def remote_add(self, remoteName: str, sUrlOrDirectoryPath: str) -> ScriptGitRemote:
		"""
		| Adds a remote with the given name and URL.
		| git remote add <name> <url> - Add a remote named <name> for the repository at <url>.
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type sUrlOrDirectoryPath: str
		:param sUrlOrDirectoryPath: URL or path of the remote
		
		"""
		pass
	
	@overload
	def remote_remove(self, remoteName: str) -> None:
		"""
		| Removes a remote with the given name.
		| git remote remove <name> - Remove the remote named <name>. All remote-tracking branches and configuration settings for the remote are removed.
		
		:type remoteName: str
		:param remoteName: Name of the remote to remove
		
		"""
		pass
	
	@overload
	def remote_remove(self, remote: ScriptGitRemote) -> None:
		"""
		| Removes a remote with the given name.
		| git remote remove <name> - Remove the remote named <name>. All remote-tracking branches and configuration settings for the remote are removed.
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to remove
		
		"""
		pass
	
	def remote_remove(self) -> None:
		"""
		| Removes a remote with the given name.
		| git remote remove <name> - Remove the remote named <name>. All remote-tracking branches and configuration settings for the remote are removed.
		
		:type remoteName: str
		:param remoteName: Name of the remote to remove
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to remove
		
		"""
		pass
	
	@overload
	def remote_rename(self, oldRemoteName: str, newRemoteName: str) -> ScriptGitRemote:
		"""
		| Rename the remote with the given old name to the given new name.
		| git remote rename <old> <new> - Rename the remote named <old> to <new>. All remote-tracking branches and configuration settings for the remote are updated.
		
		:type oldRemoteName: str
		:param oldRemoteName: Name of the remote to rename
		
		:type newRemoteName: str
		:param newRemoteName: New name of the remote
		
		"""
		pass
	
	@overload
	def remote_rename(self, remote: ScriptGitRemote, newRemoteName: str) -> ScriptGitRemote:
		"""
		| Rename the remote with the given old name to the given new name.
		| git remote rename <old> <new> - Rename the remote named <old> to <new>. All remote-tracking branches and configuration settings for the remote are updated.
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to rename
		
		:type newRemoteName: str
		:param newRemoteName: New name of the remote
		
		"""
		pass
	
	def remote_rename(self) -> ScriptGitRemote:
		"""
		| Rename the remote with the given old name to the given new name.
		| git remote rename <old> <new> - Rename the remote named <old> to <new>. All remote-tracking branches and configuration settings for the remote are updated.
		
		:type oldRemoteName: str
		:param oldRemoteName: Name of the remote to rename
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to rename
		
		:type newRemoteName: str
		:param newRemoteName: New name of the remote
		
		"""
		pass
	
	@overload
	def remote_set_url(self, remoteName: str, urlOrDirectoryPath: str) -> None:
		"""
		| Change for the given remote the URL.
		| git remote set-url <name> <newurl> - Changes URLs for the remote
		
		:type remoteName: str
		:param remoteName: Name of the remote to rename
		
		:type urlOrDirectoryPath: str
		:param urlOrDirectoryPath: New URL or path of the remote
		
		"""
		pass
	
	@overload
	def remote_set_url(self, remote: ScriptGitRemote, urlOrDirectoryPath: str) -> None:
		"""
		| Change for the given remote the URL.
		| git remote set-url <name> <newurl> - Changes URLs for the remote
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to rename
		
		:type urlOrDirectoryPath: str
		:param urlOrDirectoryPath: New URL or path of the remote
		
		"""
		pass
	
	def remote_set_url(self) -> None:
		"""
		| Change for the given remote the URL.
		| git remote set-url <name> <newurl> - Changes URLs for the remote
		
		:type remoteName: str
		:param remoteName: Name of the remote to rename
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to rename
		
		:type urlOrDirectoryPath: str
		:param urlOrDirectoryPath: New URL or path of the remote
		
		"""
		pass
	
	@overload
	def branch_track(self, trackedBranchName: str, localBranchName: str=None) -> None:
		"""
		| Let the local branch track a remote branch.
		| Tracking branches are local branches that have a direct relationship to a remote branch.
		| git-branch --track <branchname> [<start-point>] - Track branch
		
		:type trackedBranchName: str
		:param trackedBranchName: Name of the branch to track
		
		:type localBranchName: str
		:param localBranchName: Name of the tracking branch
		
		"""
		pass
	
	@overload
	def branch_track(self, trackedBranchName: str, localScriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Let the local branch track a remote branch.
		| Tracking branches are local branches that have a direct relationship to a remote branch.
		| git-branch --track <branchname> [<start-point>] - Track branch
		
		:type trackedBranchName: str
		:param trackedBranchName: Name of the branch to track
		
		:type localScriptGitBranch: ScriptGitBranch
		:param localScriptGitBranch: Branch object of the tracking branch
		
		"""
		pass
	
	@overload
	def branch_track(self, trackedScriptGitBranch: ScriptGitBranch, localBranchName: str=None) -> None:
		"""
		| Let the local branch track a remote branch.
		| Tracking branches are local branches that have a direct relationship to a remote branch.
		| git-branch --track <branchname> [<start-point>] - Track branch
		
		:type trackedScriptGitBranch: ScriptGitBranch
		:param trackedScriptGitBranch: Branch object of the branch to track
		
		:type localBranchName: str
		:param localBranchName: Name of the tracking branch
		
		"""
		pass
	
	@overload
	def branch_track(self, trackedScriptGitBranch: ScriptGitBranch, localScriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Let the local branch track a remote branch.
		| Tracking branches are local branches that have a direct relationship to a remote branch.
		| git-branch --track <branchname> [<start-point>] - Track branch
		
		:type trackedScriptGitBranch: ScriptGitBranch
		:param trackedScriptGitBranch: Branch object of the branch to track
		
		:type localScriptGitBranch: ScriptGitBranch
		:param localScriptGitBranch: Branch object of the tracking branch
		
		"""
		pass
	
	def branch_track(self) -> None:
		"""
		| Let the local branch track a remote branch.
		| Tracking branches are local branches that have a direct relationship to a remote branch.
		| git-branch --track <branchname> [<start-point>] - Track branch
		
		:type trackedBranchName: str
		:param trackedBranchName: Name of the branch to track
		
		:type localBranchName: str
		:param localBranchName: Name of the tracking branch
		
		:type trackedScriptGitBranch: ScriptGitBranch
		:param trackedScriptGitBranch: Branch object of the branch to track
		
		:type localScriptGitBranch: ScriptGitBranch
		:param localScriptGitBranch: Branch object of the tracking branch
		
		"""
		pass
	
	@overload
	def branch_set_upstream_to(self, remoteName: str, branchName: str=None) -> None:
		"""
		| Set up the tracking information of the local branch.
		| git branch --set-upstream-to=<upstream> [<branchname>] - Set up <branchname>'s tracking
		| information so <upstream> is considered <branchname>'s upstream branch.
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type branchName: str
		:param branchName: Name of the branch
		
		"""
		pass
	
	@overload
	def branch_set_upstream_to(self, remoteName: str, scriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Set up the tracking information of the local branch.
		| git branch --set-upstream-to=<upstream> [<branchname>] - Set up <branchname>'s tracking
		| information so <upstream> is considered <branchname>'s upstream branch.
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch
		
		"""
		pass
	
	@overload
	def branch_set_upstream_to(self, remote: ScriptGitRemote, branchName: str=None) -> None:
		"""
		| Set up the tracking information of the local branch.
		| git branch --set-upstream-to=<upstream> [<branchname>] - Set up <branchname>'s tracking
		| information so <upstream> is considered <branchname>'s upstream branch.
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type branchName: str
		:param branchName: Name of the branch
		
		"""
		pass
	
	@overload
	def branch_set_upstream_to(self, remote: ScriptGitRemote, scriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Set up the tracking information of the local branch.
		| git branch --set-upstream-to=<upstream> [<branchname>] - Set up <branchname>'s tracking
		| information so <upstream> is considered <branchname>'s upstream branch.
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch
		
		"""
		pass
	
	def branch_set_upstream_to(self) -> None:
		"""
		| Set up the tracking information of the local branch.
		| git branch --set-upstream-to=<upstream> [<branchname>] - Set up <branchname>'s tracking
		| information so <upstream> is considered <branchname>'s upstream branch.
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type branchName: str
		:param branchName: Name of the branch
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch
		
		"""
		pass
	
	@overload
	def branch_unset_upstream(self, branchName: str=None) -> None:
		"""
		| Remove the tracking information of the local branch.
		| git branch --unset-upstream <branchname> - Remove the upstream information for <branchname>.
		
		:type branchName: str
		:param branchName: Name of the branch
		
		"""
		pass
	
	@overload
	def branch_unset_upstream(self, scriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Remove the tracking information of the local branch.
		| git branch --unset-upstream <branchname> - Remove the upstream information for <branchname>.
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch
		
		"""
		pass
	
	def branch_unset_upstream(self) -> None:
		"""
		| Remove the tracking information of the local branch.
		| git branch --unset-upstream <branchname> - Remove the upstream information for <branchname>.
		
		:type branchName: str
		:param branchName: Name of the branch
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch
		
		"""
		pass
	
	@overload
	def fetch(self, remoteName: str, prune: bool=False) -> None:
		"""
		| Fetch from remote.
		| git fetch <remote> - Download objects and refs from another repository
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type prune: bool
		:param prune: Flag for pruning
		
		"""
		pass
	
	@overload
	def fetch(self, remoteName: str, username: str, password: str, prune: bool=False) -> None:
		"""
		| Fetch from remote.
		| git fetch <remote> - Download objects and refs from another repository
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		:type prune: bool
		:param prune: Flag for pruning
		
		"""
		pass
	
	@overload
	def fetch(self, remote: ScriptGitRemote, prune: bool=False) -> None:
		"""
		| Fetch from remote.
		| git fetch <remote> - Download objects and refs from another repository
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type prune: bool
		:param prune: Flag for pruning
		
		"""
		pass
	
	@overload
	def fetch(self, remote: ScriptGitRemote, username: str, password: str, prune: bool=False) -> None:
		"""
		| Fetch from remote.
		| git fetch <remote> - Download objects and refs from another repository
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Passowrd
		
		:type prune: bool
		:param prune: Flag for pruning
		
		"""
		pass
	
	def fetch(self) -> None:
		"""
		| Fetch from remote.
		| git fetch <remote> - Download objects and refs from another repository
		
		:type remoteName: str
		:param remoteName: Name of the remote
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		:type prune: bool
		:param prune: Flag for pruning
		
		"""
		pass
	
	@overload
	def pull(self, userName: str, userEmail: str, scriptGitPullOptions: ScriptGitPullOptions, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Pull changes from remote.
		| git-pull - Fetch from and integrate with another repository or a local branch
		| https://git-scm.com/docs/git-pull
		| Incorporates changes from a remote repository into the current branch.
		| In its default mode, git pull is shorthand for git fetch followed by git merge FETCH_HEAD.
		
		:type userName: str
		:param userName: Username used for merge commit
		
		:type userEmail: str
		:param userEmail: E-mail used for merge commit
		
		:type scriptGitPullOptions: ScriptGitPullOptions
		:param scriptGitPullOptions: Pull options
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def pull(self, userName: str, userEmail: str, fetchUsername: str, fetchPassword: str,  scriptGitPullOptions: ScriptGitPullOptions, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Pull changes from remote.
		| git-pull - Fetch from and integrate with another repository or a local branch
		| https://git-scm.com/docs/git-pull
		| Incorporates changes from a remote repository into the current branch.
		| In its default mode, git pull is shorthand for git fetch followed by git merge FETCH_HEAD.
		
		:type userName: str
		:param userName: Username used for merge commit
		
		:type userEmail: str
		:param userEmail: E-mail used for merge commit
		
		:type fetchUsername: str
		:param fetchUsername: Username used for fetch
		
		:type fetchPassword: str
		:param fetchPassword: Password used for fetch
		
		:type scriptGitPullOptions: ScriptGitPullOptions
		:param scriptGitPullOptions: Pull options
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	def pull(self) -> tuple[ScriptProject, ScriptGitMergeResult]:
		"""
		| Pull changes from remote.
		| git-pull - Fetch from and integrate with another repository or a local branch
		| https://git-scm.com/docs/git-pull
		| Incorporates changes from a remote repository into the current branch.
		| In its default mode, git pull is shorthand for git fetch followed by git merge FETCH_HEAD.
		
		:type userName: str
		:param userName: Username used for merge commit
		
		:type userEmail: str
		:param userEmail: E-mail used for merge commit
		
		:type fetchUsername: str
		:param fetchUsername: Username used for fetch
		
		:type fetchPassword: str
		:param fetchPassword: Password used for fetch
		
		:type scriptGitPullOptions: ScriptGitPullOptions
		:param scriptGitPullOptions: Pull options
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		"""
		pass
	
	@overload
	def push(self, branchName: str=None) -> None:
		"""
		| Push the local change to remote.
		| git-push - Updates remote refs using local refs, while sending objects necessary to complete the given refs.
		| With given RemoteName and RemoteBranchName this can be used as git push --set-upstream <RemoteName> <RemoteBranchName>
		
		:type branchName: str
		:param branchName: Name of the branch to push
		
		"""
		pass
	
	@overload
	def push(self, branchName: str, username: str, password: str) -> None:
		"""
		| Push the local change to remote.
		| git-push - Updates remote refs using local refs, while sending objects necessary to complete the given refs.
		| With given RemoteName and RemoteBranchName this can be used as git push --set-upstream <RemoteName> <RemoteBranchName>
		
		:type branchName: str
		:param branchName: Name of the branch to push
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		"""
		pass
	
	@overload
	def push(self, scriptGitBranch: ScriptGitBranch) -> None:
		"""
		| Push the local change to remote.
		| git-push - Updates remote refs using local refs, while sending objects necessary to complete the given refs.
		| With given RemoteName and RemoteBranchName this can be used as git push --set-upstream <RemoteName> <RemoteBranchName>
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to push
		
		"""
		pass
	
	@overload
	def push(self, scriptGitBranch: ScriptGitBranch, username: str, password: str) -> None:
		"""
		| Push the local change to remote.
		| git-push - Updates remote refs using local refs, while sending objects necessary to complete the given refs.
		| With given RemoteName and RemoteBranchName this can be used as git push --set-upstream <RemoteName> <RemoteBranchName>
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to push
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		"""
		pass
	
	def push(self) -> None:
		"""
		| Push the local change to remote.
		| git-push - Updates remote refs using local refs, while sending objects necessary to complete the given refs.
		| With given RemoteName and RemoteBranchName this can be used as git push --set-upstream <RemoteName> <RemoteBranchName>
		
		:type branchName: str
		:param branchName: Name of the branch to push
		
		:type scriptGitBranch: ScriptGitBranch
		:param scriptGitBranch: Branch object of the branch to push
		
		:type username: str
		:param username: Username
		
		:type password: str
		:param password: Password
		
		"""
		pass
	
	@overload
	def push_delete(self, remoteName: str, branchName: str, force: bool=False) -> None:
		"""
		| Deletes a remote branch.
		| git push <remote_name> --delete <branch_name>
		
		:type remoteName: str
		:param remoteName: Name of the remote to push the deletion to
		
		:type branchName: str
		:param branchName: Name of the branch to delete
		
		:type force: bool
		:param force: Flag for forcing
		
		"""
		pass
	
	@overload
	def push_delete(self, remote: ScriptGitRemote, branchName: str, force: bool=False) -> None:
		"""
		| Deletes a remote branch.
		| git push <remote_name> --delete <branch_name>
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to push the deletion to
		
		:type branchName: str
		:param branchName: Name of the branch to delete
		
		:type force: bool
		:param force: Flag for forcing
		
		"""
		pass
	
	@overload
	def push_delete(self, remoteName: str, branch: ScriptGitBranch, force: bool=False) -> None:
		"""
		| Deletes a remote branch.
		| git push <remote_name> --delete <branch_name>
		
		:type remoteName: str
		:param remoteName: Name of the renote to push the deletion to
		
		:type branch: ScriptGitBranch
		:param branch: Branch object of the branch to delete
		
		:type force: bool
		:param force: Flag for forcing
		
		"""
		pass
	
	@overload
	def push_delete(self, remote: ScriptGitRemote, branch: ScriptGitBranch, force: bool=False) -> None:
		"""
		| Deletes a remote branch.
		| git push <remote_name> --delete <branch_name>
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to push the deletion to
		
		:type branch: ScriptGitBranch
		:param branch: Branch object of the branch to delete
		
		:type force: bool
		:param force: Flag for forcing
		
		"""
		pass
	
	def push_delete(self) -> None:
		"""
		| Deletes a remote branch.
		| git push <remote_name> --delete <branch_name>
		
		:type branchName: str
		:param branchName: Name of the branch to delete
		
		:type remoteName: str
		:param remoteName: Name of the remote to push the deletion to
		
		:type remote: ScriptGitRemote
		:param remote: Remote object of the remote to push the deletion to
		
		:type branch: ScriptGitBranch
		:param branch: Branch object of the branch to delete
		
		:type force: bool
		:param force: Flag for forcing
		
		"""
		pass
	
	def get_current_git_operation(self) -> CurrentGitOperation:
		"""
		| Gets the current Git operation.
		
		"""
		pass
	
	def last_commit(self) -> ScriptGitCommit:
		"""
		| Gets the commit the current repository head points to.
		
		:rtype: ScriptGitCommit
		:returns: The commit the current repository head points to.
		
		"""
		pass
	
	def is_last_commit_pushed(self) -> bool:
		"""
		| Returns true if the most recent commit in the current branch is already pushed to remote.
		
		"""
		pass
	
	def synchronize_project(self) -> None:
		"""
		| Synchronizes the CODESYS project to the git project storage.
		
		"""
		pass
	
	def resynchronize_project(self, update_flags: VersionUpdateFlags=VersionUpdateFlags.NoUpdates) -> ScriptProject:
		"""
		| Enforces resynchronization of the CODESYS project from the content of the CODESYS Git project storage.
		
		:type update_flags: VersionUpdateFlags
		:param update_flags: Flags for handling project updates
		
		:rtype: ScriptProject
		:returns: Resulting CODESYS project
		
		"""
		pass