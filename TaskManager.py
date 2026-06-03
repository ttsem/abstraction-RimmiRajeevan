class Printer:
    def print(self):
        print("Printing document...")


class Scanner:
    def scan(self):
        print("Scanning document...")


class TaskManager:
    def print_task(self, task_id, printer):
        print(f"Executing Print Task: {task_id}")
        printer.print()

    def scan_task(self, task_id, scanner):
        print(f"Executing Scan Task: {task_id}")
        scanner.scan()


# Usage
printer = Printer()
scanner = Scanner()

scheduler = TaskManager()

scheduler.print_task(101, printer)
scheduler.scan_task(102, scanner)
