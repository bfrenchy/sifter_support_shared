# sifter_support_shared

This is a submodule for shared search and ingest functions.

Contains a few different files that should be generally shared across all
the different apps, related to processing and ingesting files to Pinecone
as well as the functions to chat with the LLM with and without memory.

## Updating the Submodule

If you make changes to this submodule and want to push them to GitHub, follow these steps on Mac OS:

1. Navigate to the root directory of the submodule.
2. Stage your changes with `git add .`
3. Commit your changes with `git commit -m "Your commit message"`
4. Push your changes with `git push origin master`

To update this submodule within the main modules it resides in (e.g., garmin_app/), follow these steps:

1. Navigate to the root directory of the main module.
2. Run `git submodule update --remote --merge`
3. Stage the updated submodule with `git add .`
4. Commit the updated submodule with `git commit -m "Updated submodule"`
5. Push the updated submodule with `git push origin master`

## Handy Git Commands

Here are some handy git commands that might be useful:

* `git status`: Check the status of your local repository.
* `git diff`: Show changes between your working directory and the index.
* `git log`: Show commit history.
* `git checkout <branch_name>`: Switch to a different branch.
* `git pull origin master`: Pull the latest changes from the master branch.
* `git reset --hard HEAD`: Discard all local changes in your working directory.

## Managing and Using Branches

Here are some commands for managing and using branches:

* `git branch`: List all local branches.
* `git branch -a`: List all local and remote branches.
* `git branch <branch_name>`: Create a new branch.
* `git checkout <branch_name>`: Switch to a different branch.
* `git merge <branch_name>`: Merge a branch into the current branch.
* `git branch -d <branch_name>`: Delete a branch.
* `git push origin <branch_name>`: Push a branch to the remote repository.
* `git pull origin <branch_name>`: Pull the latest changes from a specific branch.

## Quick reminders for activating the venv

* `python3 -m venv env`: Create a new virtual environment.
* `source venv/bin/activate`: Activate the virtual environment.
* `deactivate`: Deactivate the virtual environment.
