def process_task(task, task_type):
    """
    Simulated AI agent (no API required)
    """

    # Normalize input
    task = task.strip()
    task_type = task_type.lower().strip()

    # CODE TASKS
    if task_type == "code":
        return f"""💻 Code Assistant

Task: {task}

Here is a simple example solution:

```python
# Example code for: {task}
def solution():
    print("This is a simulated code response")

solution()
"""
    # WRITING TASKS
    elif task_type == "writing":
     return f"""✍️ Writing Assistant
     Task: {task}

Generated paragraph:

"{task.capitalize()} is an interesting topic. This is a simulated AI-generated paragraph to demonstrate how your AI agent works."
"""
    
    # GENERAL TASKS
    else:
     return f"""🤖 General Assistant
     Task: {task}

Result:
This is a simulated response.
Your AI agent is working correctly 🚀
"""