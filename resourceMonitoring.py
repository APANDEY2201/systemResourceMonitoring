import psutil
import time
from win10toast import ToastNotifier

# Initialize the ToastNotifier object
toaster = ToastNotifier()

# Set the threshold values for CPU usage, memory usage, GPU usage, and battery level
cpu_threshold = 40  # Percentage
memory_threshold = 40  # Percentage
gpu_threshold = 40  # Percentage
battery_threshold = 100  # Percentage

try:
    # Get system resource information
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    gpu_usage = psutil.virtual_memory().percent  # Placeholder for GPU usage, as accurate monitoring requires specific libraries
    battery = psutil.sensors_battery()

    # Check CPU usage
    if cpu_usage >= cpu_threshold:
        message = f"CPU usage is high: {cpu_usage}%"
        toaster.show_toast("Resource Alert", message, duration=10)

    # Check memory usage
    if memory_usage >= memory_threshold:
        message = f"Memory usage is high: {memory_usage}%"
        toaster.show_toast("Resource Alert", message, duration=10)

    # Check GPU usage - Note: This is still using memory usage as a placeholder.
    if gpu_usage >= gpu_threshold:
        message = f"GPU usage is high: {gpu_usage}%"
        toaster.show_toast("Resource Alert", message, duration=10)

    # Check battery level
    if battery is not None and battery.percent <= battery_threshold and not battery.power_plugged:
        message = f"Battery level is low: {battery.percent}%"
        toaster.show_toast("Battery Alert", message, duration=10)

except Exception as e:
    print("An error occurred:", str(e))
