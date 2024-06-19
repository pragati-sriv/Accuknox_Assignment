import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO)

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')

def check_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory.percent}%')

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk.percent}%')

def main():
    check_cpu()
    check_memory()
    check_disk()

if __name__ == '__main__':
    main()
