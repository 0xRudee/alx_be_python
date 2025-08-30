task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time = str(input("Is it time-bound? (yes/no): "))
task_date = ''

match priority :
  case 'high' :
    if time=="yes":
      task_date = input('When should you finish the task?: ')
  case 'medium' :
    if time=="yes":
      task_date = input('When should you finish the task?: ')
  case 'low' :
    if time=="yes":
      task_date = input('When should you finish the task?: ')
if task_date :
  print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention {task_date}!")
else :
  print(f"Note: '{task}' is a {priority} priority task.\nConsider completing it when you have free time.")
