# 🔹 Import libraries and modules
from datetime import datetime
import os

def auto_commit(message):
    os.system("git add .")
from datetime import datetime

def auto_commit(action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"[AGENT] {action} | {details} | {timestamp}"

    os.system("git add .")
    os.system(f'git commit -m "{commit_msg}"')

# 🔹 Read previous plans (memory)
def read_previous_plans():
    try:
        with open("memory/plans.md", "r") as f:
            return f.read()
    except:
        return ""


# 🔹 Show progress report (NEW FEATURE)
def show_progress():
    try:
        with open("memory/plans.md", "r") as f:
            data = f.read()
    except:
        data = ""

    entries = data.count("##")

    print("\n📈 Progress Report:")

    if entries == 0:
        print("No plans yet. Start today! 🚀")
    elif entries < 3:
        print(f"You created {entries} plans. Good start 😌")
    elif entries < 7:
        print(f"You created {entries} plans. Nice consistency 💪")
    else:
        print(f"You created {entries} plans. Excellent discipline 🔥")

def improve_resume():
    text = input("\nPaste your resume line: ")

    print("\n✨ Improved Version:")

    # simple improvement logic
    improved = f"Experienced in {text}, with strong problem-solving and practical implementation skills."

    print(improved) 
    auto_commit("ResumeImproved", text)


# 🔹 Main function
def create_plan():
    task = input("What is your main goal today? ")

    previous_data = read_previous_plans()

    date = datetime.now().strftime("%Y-%m-%d")

    plan = f"\n## {date}\n- {task}\n"

    # Save plan
    with open("memory/plans.md", "a") as f:
        f.write(plan)

        auto_commit("DailyPlanCreated", task)

    print("\n✅ Plan saved successfully!")

    # 🔹 Insight logic
    entries = previous_data.count("##")

    print("\n📊 Insight:")

    if entries == 0:
        print("This is your first plan. Let’s start strong 🚀")
    elif entries < 3:
        print("Good start! Try planning daily 😌")
    elif entries < 7:
        print("Nice consistency! Keep pushing 💪")
    else:
        print("Great discipline! You are building a strong habit 🚀")

    # 🔹 Call progress tracker
    show_progress()


# 🔹 Run program
if __name__ == "__main__":
    print("🤖 Welcome to Guidr AI Agent\n")

    print("Choose an option:")
    print("1. Create Daily Plan")
    print("2. Improve Resume")

    choice = input("\nEnter your choice (1/2): ")

    if choice == "1":
        create_plan()
    elif choice == "2":
        improve_resume()
    else:
        print("Invalid choice. Please restart.")