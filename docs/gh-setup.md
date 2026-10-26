# Installing and setting up the GitHub CLI

[Back to README](../README.md)

The GitHub CLI (`gh`) is GitHub's command line tool for creating repos,
issues, and pull requests from the terminal. It is a separate program
from Git, so install [Git](git-setup.md) first.

## 1. Install the GitHub CLI

**Windows:**

```bash
winget install --id GitHub.cli -e
```

**macOS** (requires [Homebrew](https://brew.sh)):

```bash
brew install gh
```

**Linux and other options:** see <https://cli.github.com>.

Close and reopen your terminal after installing, so it can find the new
`gh` command.

## 2. Check that it works

```bash
gh --version
```

## 3. Sign in to GitHub

```bash
gh auth login
```

It asks a few questions. These answers work for most people:

- Where do you use GitHub? **GitHub.com**
- Preferred protocol for Git operations? **HTTPS**
- Authenticate Git with your GitHub credentials? **Yes**
- How would you like to authenticate? **Login with a web browser**

`gh` then shows a one-time code and opens GitHub in your browser. Enter
the code and approve access. Answering **Yes** to the Git question also
lets `git push` and `git pull` sign in to GitHub without asking for a
password.

## 4. Check that you are signed in

```bash
gh auth status
```

This shows which GitHub account you are signed in as.

## 5. Try it out

List your GitHub repos:

```bash
gh repo list
```

## 6. Make sure Git can sign in to GitHub

The GitHub CLI signs in for `gh` commands. Git signs in separately, for
`git push`, `git pull`, and `git clone`. Git does this through a
sign-in helper, a small program that supplies your GitHub login so you
are not asked for it each time. Usually one is already set up:

- **The GitHub CLI.** If you answered **Yes** to "Authenticate Git with
  your GitHub credentials?" in step 3, `gh` set itself up as Git's
  sign-in helper for GitHub.
- **Git Credential Manager.** Git for Windows includes this helper. The
  first time you push, it opens a browser window to sign in to GitHub,
  then remembers you.

To see which helper Git uses, run:

```bash
git config --get-regexp credential
```

- `gh auth git-credential` in the output means Git uses the GitHub CLI.
- `credential.helper manager` means Git uses Git Credential Manager.

Either one works. If neither appears, or `git push` keeps asking for a
username and password, connect Git to the GitHub CLI:

```bash
gh auth setup-git
```

Then retry the command that asked you to sign in.
