# Installing and setting up Git

[Back to README](../README.md)

Git is the version control tool that runs on your computer. These steps
install it, check that it works, and give it the few settings it needs
before your first commit.

## 1. Install Git

**Windows:**

```bash
winget install --id Git.Git -e
```

This also installs Git Bash, a terminal that accepts the Unix-style
commands used in this repo. You can also download the installer from
<https://git-scm.com/downloads>.

**macOS** (requires [Homebrew](https://brew.sh)):

```bash
brew install git
```

**Linux (Debian or Ubuntu):**

```bash
sudo apt install git
```

Close and reopen your terminal after installing, so it can find the new
`git` command.

## 2. Check that it works

```bash
git --version
```

This prints the installed version, for example `git version 2.56.0`.

## 3. Tell Git who you are

Every commit records a name and an email address. Set them once for all
your repos:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

Use the same email address as your GitHub account, so GitHub can link
your commits to your profile.

## 4. Set the default branch name for new repos

This is a one-time setting, not a branch. It tells Git what to call the
starting branch whenever you create a new repo with `git init` in the
future. Setting it to `main` matches GitHub:

```bash
git config --global init.defaultBranch main
```

It does not change repos you already have, and it does not affect
branches you create later with `git checkout -b`.

## 5. Check your settings

```bash
git config --global --list
```

You should see `user.name`, `user.email`, and `init.defaultBranch` in
the list.
