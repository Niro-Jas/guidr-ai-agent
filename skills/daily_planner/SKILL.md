---
name: daily_planner
description: Generates structured daily plans, stores them in Git memory, and tracks user consistency over time.
---

# 🧠 Daily Planner Skill

## 🎯 Purpose
To help users plan their daily activities in a structured and consistent way using Git-based memory.

---

## ⚙️ How It Works

When a user asks for planning:

1. Understand the user’s main goal or task
2. Break it into simple actionable steps
3. Generate a structured daily plan
4. Save the plan in /memory/plans.md
5. Commit the update to Git

---

## 📝 Plan Format

Each plan includes:

- 📅 Date  
- 🎯 Main Goal  
- ✅ Task Breakdown  
- 🧠 Notes (optional)

---

## 💾 Memory Behavior

- Plans are appended to plans.md
- Previous plans are never deleted
- All entries are stored chronologically
- Git commits act as memory history

---

## 📊 Intelligence Layer

The agent can:

- Compare current plan with previous entries  
- Identify:
  - missed tasks  
  - repeated goals  
- Suggest improvements  

Example:
"You planned 5 tasks yesterday but completed only 2. Try reducing overload."

---

## 🌍 Language Support

- Primary: English  
- Supports Tamil and Hindi (mixed responses)

Example:
"Here’s your plan 😌 — step by step pannu, overload pannadhe."

---

## 🚀 Goal

To build user consistency and discipline  
by tracking daily activities using Git as memory.