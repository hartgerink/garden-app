# garden-app: A GitHub Workflow Exercise

This repo is a hands-on exercise in the GitHub workflow that software
teams use to manage changes: issues, feature branches, pull requests,
and merging.

The code is deliberately simple. `garden_advice.py` is a short Python
program that asks for a season and a type of plant, then prints
gardening advice. Its only job is to give the workflow something real
to change.

## How the code changed

Follow these links in order to see the file before, between, and after
the two issues.

1. **Starting point:** [`garden_advice.py` as first committed](https://github.com/hartgerink/garden-app/blob/88648b9988da868dafe53dbdc5c64660386a93b0/garden_advice.py),
   before any changes. The season and plant type are hardcoded.
2. **Issue #1 (closed):** [Replace hardcoded season and plant type with user input](https://github.com/hartgerink/garden-app/issues/1),
   resolved by [pull request #3](https://github.com/hartgerink/garden-app/pull/3).
   Its Files changed tab shows exactly what changed.
3. **After issue #1:** [`garden_advice.py` after issue #1 was merged](https://github.com/hartgerink/garden-app/blob/d0ce5a3c648ba5b5b07f573981a16cb110c7c615/garden_advice.py).
   The program now asks the user for both values.
4. **Issue #2 (closed):** [Store advice in dictionaries](https://github.com/hartgerink/garden-app/issues/2),
   resolved by [pull request #4](https://github.com/hartgerink/garden-app/pull/4).
5. **Final version:** [`garden_advice.py` as it stands now](https://github.com/hartgerink/garden-app/blob/main/garden_advice.py).
   The advice is stored in dictionaries instead of `if`/`elif` chains.

## The tools

- **GitHub** is a website that hosts Git repos online and adds team
  features on top of them, such as issues and pull requests. This repo
  lives there.
- **Git** (`git`) is the version control tool that runs on your
  computer. It records changes as commits, manages branches, and moves
  commits to and from GitHub with `git push` and `git pull`.
  - Setup: [Installing and setting up Git](docs/git-setup.md)
- **GitHub CLI** (`gh`) is GitHub's command line tool. It does website
  tasks, such as creating repos, issues, and pull requests, from the
  terminal. It works alongside `git` and does not replace it.
  - Setup: [Installing and setting up the GitHub CLI](docs/gh-setup.md)

## Creating the public repo

The repo starts on your computer and is then published to GitHub.

1. Create a folder for the project and move into it:

   ```bash
   mkdir garden-app
   ```

   ```bash
   cd garden-app
   ```

2. Copy the Python file into the folder (replace `/path/to` with where
   the file is):

   ```bash
   cp /path/to/garden_advice.py .
   ```

3. Turn the folder into a local Git repo, with `main` as its first
   branch:

   ```bash
   git init -b main
   ```

4. Stage the file for the first commit:

   ```bash
   git add garden_advice.py
   ```

5. Commit it:

   ```bash
   git commit -m "Add garden_advice.py"
   ```

6. Create the public repo on GitHub and push the commit to it:

   ```bash
   gh repo create garden-app --public --source . --remote origin --push
   ```

   This one command does three things: it creates the `garden-app` repo
   on GitHub, links your folder to it under the name `origin`, and
   pushes your commit. There is no separate `git push` for this first
   upload.

## The workflow

Every change goes through the same cycle. This walks through one full
pass, using issue #1 as the example. Issue #2 followed the same steps.

1. **Create an issue** describing the change. GitHub gives it a number,
   here #1.

   ```bash
   gh issue create --title "Replace hardcoded season and plant type with user input" --body "Replace the hardcoded season and plant_type values with input()."
   ```

2. **Create a branch** for the issue. Start from an up-to-date `main`,
   so the branch includes everything merged so far:

   ```bash
   git checkout main
   ```

   ```bash
   git pull origin main
   ```

   ```bash
   git checkout -b feature/user-input
   ```

3. **Implement the change** in `garden_advice.py` on the new branch.
   Then compare your edited file with the last committed version, to
   see exactly what you changed:

   ```bash
   git diff
   ```

   Lines starting with `-` were removed, and lines starting with `+`
   were added.

4. **Commit and push your changes to GitHub.** Putting `closes #1` in
   the commit message links the commit to the issue:

   ```bash
   git add garden_advice.py
   ```

   ```bash
   git commit -m "Replace hardcoded season and plant type with user input (closes #1)"
   ```

   ```bash
   git push origin feature/user-input
   ```

5. **Open a pull request** from the branch into `main`. `Fixes #1` in
   the description tells GitHub which issue the pull request resolves.
   GitHub gives the pull request the next free number, here #3.

   ```bash
   gh pr create --base main --head feature/user-input --title "Issue #1 - Replace hardcoded season and plant type with user input" --body "Fixes #1"
   ```

   `gh` prints the new pull request's link, which ends in its number:

   ```
   https://github.com/hartgerink/garden-app/pull/3
   ```

6. **Review and merge the pull request.** The commands below use `3`,
   the pull request number printed in step 5. Look over the changes
   first:

   ```bash
   gh pr diff 3
   ```

   Then merge it into `main`:

   ```bash
   gh pr merge 3 --merge
   ```

   `--merge` keeps the branch's commits and adds a merge commit to
   `main`. Without it, `gh` stops to ask which merge method to use.

7. **Close the issue.** Because of `closes #1` and `Fixes #1`, GitHub
   closes issue #1 automatically when the pull request is merged (see
   [Closing issues automatically](#closing-issues-automatically)).
   Check that it did:

   ```bash
   gh issue view 1
   ```

   If it is still open, close it yourself:

   ```bash
   gh issue close 1
   ```

8. **Delete the branch** on GitHub, now that its work is in `main`:

   ```bash
   git push origin --delete feature/user-input
   ```

9. **Update your local repo.** The merge happened on GitHub, so your
   computer's `main` does not have it yet. Switch to `main` and pull:

   ```bash
   git checkout main
   ```

   ```bash
   git pull origin main
   ```

   Then delete your local copy of the branch:

   ```bash
   git branch -d feature/user-input
   ```

   `-d` only deletes a branch whose work has been merged, so nothing is
   lost. Your local repo now matches GitHub, ready for the next issue.

## Closing issues automatically

GitHub can close an issue for you when the work that fixes it is
merged. To make this happen, write a keyword followed by the issue
number:

- in the pull request description, or
- in a commit message that is part of the pull request.

The keywords are `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`,
`resolve`, `resolves`, and `resolved`. Capital letters do not matter.

The workflow above uses both: `closes #1` in the commit message in
step 4, and `Fixes #1` in the pull request description in step 5.

What happens:

- When the pull request is opened, GitHub links it to the issue.
- Nothing closes yet. The issue stays open while the pull request is
  being reviewed.
- When the pull request is merged into `main`, GitHub closes the issue
  and records which pull request closed it.

Things to watch for:

- A plain mention such as `#1` or `see #1` only links the issue. It
  does not close it.
- Each issue needs its own keyword. To close two issues, write
  `Fixes #1, fixes #2`, not `Fixes #1, #2`.
- Issues only close when the pull request is merged into the repo's
  default branch (here, `main`).
- If you forget the keyword, close the issue yourself with
  `gh issue close 1`.

## Helpful commands

These commands show what is going on without changing anything. They
do not create, close, or merge anything, so they are safe to run at any
time.

### In your local repo (`git`)

- See which branch you are on and which files have changed:

  ```bash
  git status
  ```

- See exactly what you changed in your files since the last commit,
  line by line:

  ```bash
  git diff
  ```

  After `git add`, the changes move out of `git diff`. To see what you
  have staged for the next commit, use:

  ```bash
  git diff --staged
  ```

- See the commit history, one line per commit, with branches and merges
  drawn as a graph:

  ```bash
  git log --oneline --graph
  ```

- List your branches, including the copies of GitHub's branches that
  your computer knows about:

  ```bash
  git branch -a
  ```

- See which GitHub repo your folder is linked to:

  ```bash
  git remote -v
  ```

### On GitHub (`gh`)

- List the open issues (add `--state all` to include closed ones):

  ```bash
  gh issue list
  ```

- Show one issue, with its description and status:

  ```bash
  gh issue view 1
  ```

- List the open pull requests (add `--state all` to include merged and
  closed ones):

  ```bash
  gh pr list
  ```

- Show one pull request, with its description and status (merged,
  open, or closed):

  ```bash
  gh pr view 3
  ```
