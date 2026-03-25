history = []

def save_task(task, result):
    history.append({
        "task": task,
        "result": result
    })

def get_history():
    return history