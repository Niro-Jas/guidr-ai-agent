# Architecture

This agent follows a Git-native architecture:

- Core logic in Python
- Memory stored in /memory directory
- Skills modularized in /skills
- Agent behavior defined via agent.yaml, SOUL.md, RULES.md

Workflow:
User Input → Skill Execution → Memory Update → Git Commit → Feedback

This simulates GitClaw-style execution within a Git repository.