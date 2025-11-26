# Git Rebase
In **Git**, `rebase` is a command used to **move or combine a series of commits** onto a new base commit.
It’s one of the most powerful — and potentially dangerous — tools in Git, used to keep your commit history **clean, linear, and easy to follow**.

---

## 🧩 What Rebase Does

When you run:

```bash
git rebase <branch>
```

Git takes all the commits from your **current branch** that are **not in `<branch>`**, temporarily removes them, updates your branch to point to `<branch>`, and then **re-applies your commits** on top of it.

In simple terms:
➡ It’s like **changing the base (starting point)** of your branch.

---

## 🧠 Example

### Without rebase

```
A---B---C  (main)
         \
          D---E  (feature)
```

You created a branch `feature` from commit `B`, made some commits (`D`, `E`), and meanwhile, `main` moved forward (`C`).

If you **merge**:

```bash
git merge main
```

You get:

```
A---B---C---M  (feature)
         \   /
          D---E
```

✅ All history is preserved, but there’s a **merge commit (M)** — history becomes non-linear.

---

### With rebase

```bash
git checkout feature
git rebase main
```

Now Git takes `D` and `E`, re-applies them **on top of `C`**:

```
A---B---C---D'---E'  (feature)
```

✅ No merge commit
✅ Clean, linear history

---

## ⚙️ Common Use Cases

1. **Update your feature branch before merging:**

   ```bash
   git checkout feature
   git fetch origin
   git rebase origin/main
   ```

   This ensures your branch includes the latest `main` updates.

2. **Edit or reorder commits (interactive rebase):**

   ```bash
   git rebase -i HEAD~3
   ```

   Lets you:

   * Edit commit messages
   * Squash (combine) commits
   * Reorder commits

3. **Avoid merge conflicts later** by rebasing regularly during development.

---

## ⚠️ Important Notes

* **Never rebase commits that are already pushed to a shared/public branch.**
  → It rewrites history and can confuse others.

* Safe to rebase **local** branches before pushing.

* If you get a conflict during rebase:

  ```bash
  # Fix the conflict manually
  git add <fixed_files>
  git rebase --continue
  ```

  To cancel:

  ```bash
  git rebase --abort
  ```

---

## 🧭 Summary Table

| Command                  | Purpose                                                 |
| ------------------------ | ------------------------------------------------------- |
| `git rebase <branch>`    | Move current branch commits on top of `<branch>`        |
| `git rebase -i <commit>` | Interactive rebase (edit/squash/reorder commits)        |
| `git rebase --continue`  | Continue after fixing conflicts                         |
| `git rebase --abort`     | Cancel an ongoing rebase                                |
| `git pull --rebase`      | Pull changes from remote and rebase your commits on top |

---
![visual diagram](images/git-rebase.png)
