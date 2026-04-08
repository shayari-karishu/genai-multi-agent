from database import add_event, add_task

# Calendar Agent
def calendar_agent(user_input):
    print("Calendar Agent Activated")

    date = "tomorrow" if "tomorrow" in user_input else "unknown"
    time = "5 PM" if "5" in user_input else "unknown"

    add_event("Meeting", date, time)
    return "Meeting scheduled"


# Task Agent
def task_agent(user_input):
    print("Task Agent Activated")

    task = "Prepare slides" if "slides" in user_input else "General task"
    add_task(task, "tomorrow")

    return "Task added"


#  Notes Agent (NEW)
def notes_agent(user_input):
    print(" Notes Agent Activated")

    # For prototype, we just simulate saving note
    note = user_input
    return "Note saved"


# Main Agent (Coordinator)
def main_agent(user_input):
    print("Main Agent Processing...")

    responses = []

    if "schedule" in user_input or "meeting" in user_input:
        responses.append(calendar_agent(user_input))

    if "remind" in user_input or "task" in user_input:
        responses.append(task_agent(user_input))

    if "note" in user_input:
        responses.append(notes_agent(user_input))

    return responses