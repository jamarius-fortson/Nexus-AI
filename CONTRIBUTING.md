# Contributing to Nexus AI

Thank you for your interest in contributing to Nexus AI! We hold our codebase to a high standard and appreciate thoughtful, well-scoped contributions.

---

## 🧭 Getting Started

1. **Fork** the repository and clone your fork locally.
2. Create a **feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Set up your development environment:
   ```bash
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   # Populate .env with your credentials
   ```

---

## ✅ Contribution Guidelines

### Code Style
- Follow **PEP 8** and use type hints everywhere.
- All public functions and classes **must have docstrings**.
- Max line length: **120 characters**.

### Commit Messages
We use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Purpose |
|:---|:---|
| `feat:` | A new feature |
| `fix:` | A bug fix |
| `docs:` | Documentation only changes |
| `refactor:` | Code restructuring without behavior change |
| `test:` | Adding or updating tests |
| `chore:` | Build process or tooling changes |

**Example:** `feat: add Slack integration to notification agent`

### Testing
- All new features **must include tests** in the `tests/` directory.
- Ensure existing tests pass: `python -m pytest tests/ -v`
- For integrations requiring credentials, add a `_manual` suffix to the test file (e.g., `test_slack_agent_manual.py`) so CI skips it automatically.

---

## 🔍 Pull Request Process

1. Ensure your branch is **up to date** with `main`.
2. Verify all CI checks are passing (GitHub Actions).
3. Write a clear PR description:
   - **What** does this change do?
   - **Why** is it needed?
   - **How** was it tested?
4. Link any related issues using `Closes #<issue-number>`.

A maintainer will review your PR within **48 hours**.

---

## 🚫 What We Don't Accept

- Commits with API keys, secrets, or credentials (any PR doing this will be immediately closed).
- Changes that remove type hints or docstrings from existing code.
- New dependencies added without a clear justification in the PR description.

---

## 💬 Need Help?

Open a [GitHub Discussion](https://github.com/YOUR_USERNAME/nexus-ai/discussions) or file an [Issue](https://github.com/YOUR_USERNAME/nexus-ai/issues) with the `question` label.

Thank you for helping make Nexus AI better! 🌌
