import csv
import time
import os  # Import os to check if the file already exists

# Function to start a new task
def start_task(task_name):
    start_time = time.time()
    return start_time, task_name

# Function to stop a task and calculate the time spent
def stop_task(start_time, task_name):
    end_time = time.time()
    time_spent = round(end_time - start_time)
    seconds = time_spent % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    time_spent_on_task = "%d:%02d:%02d" % (hour, minutes, seconds)
    log_time(task_name, time_spent_on_task)

# Function to log the time spent in a CSV file
def log_time(task_name, time_spent_on_task):
    file_exists = os.path.isfile("time_log.csv")  # Check if the file already exists
    with open("time_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Task Name', 'Time Spent'])  # Write header only if file doesn't exist
        writer.writerow([task_name, time_spent_on_task])

while True:
    task_name = input("Enter task name: ")
    print(f'Task Loaded: {task_name}')
    print("Go Ahead and Start your work.....\n")
    start_time, task_name = start_task(task_name)
    
    input("Press 'Enter' to stop this task...")
    stop_task(start_time, task_name)

    print("Task logged.")
    print("\n")

    if int(input('Press \n1 to continue \n2 to exit\n')) == 2:
        print('Nice Work!!')
        print('Time Tracking Successful !!')
        break
