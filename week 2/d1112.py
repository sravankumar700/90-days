"""
Mini-project: "Data Play" — demonstrates basics from variables to arrays (lists) in Python.
Features:
- Greeting using variables
- Simple to-do list (list operations)
- Number array stats (min/max/avg)
- Basic calculator (variables, functions)
- Responsive CLI menu

Run the file and follow prompts.
"""

def greet():
	name = input("Enter your name: ").strip() or "Player"
	print(f"Hello, {name}! Welcome to Data Play.")
	return name


def todo_menu(todos):
	while True:
		print("\nTo-Do List:")
		if todos:
			for i, t in enumerate(todos, 1):
				print(f" {i}. {t}")
		else:
			print(" (empty)")
		print("a) add  r) remove  c) clear  b) back")
		cmd = input("Choose: ").strip().lower()
		if cmd == 'a':
			item = input("Add item: ").strip()
			if item:
				todos.append(item)
		elif cmd == 'r':
			idx = input("Remove index: ").strip()
			if idx.isdigit():
				i = int(idx) - 1
				if 0 <= i < len(todos):
					todos.pop(i)
		elif cmd == 'c':
			todos.clear()
		elif cmd == 'b':
			break
		else:
			print("Unknown command")


def stats_menu():
	s = input("Enter numbers separated by spaces: ").strip()
	if not s:
		print("No numbers entered.")
		return
	parts = s.split()
	nums = []
	for p in parts:
		try:
			nums.append(float(p))
		except ValueError:
			pass
	if not nums:
		print("No valid numbers parsed.")
		return
	n = len(nums)
	total = sum(nums)
	avg = total / n
	print(f"Count: {n}, Min: {min(nums)}, Max: {max(nums)}, Sum: {total}, Avg: {avg}")


def calculator():
	expr = input("Enter simple expression (e.g. 2 + 3 * 4): ").strip()
	try:
		# safe eval: allow only digits, operators and dots/spaces
		allowed = set("0123456789+-*/(). eE")
		if set(expr) <= allowed:
			result = eval(expr, { })
			print("Result:", result)
		else:
			print("Expression contains invalid characters.")
	except Exception as e:
		print("Error evaluating expression.")


def main():
	todos = []
	user = greet()
	while True:
		print("\nMain Menu: 1) To-Do  2) Numbers Stats  3) Calculator  4) About  q) Quit")
		choice = input("Choose: ").strip().lower()
		if choice in ('1', 'to-do', 'todo'):
			todo_menu(todos)
		elif choice in ('2', 'numbers', 'stats'):
			stats_menu()
		elif choice in ('3', 'calc', 'calculator'):
			calculator()
		elif choice in ('4', 'about'):
			print(f"Data Play - demo project. User: {user}. Uses variables, lists, functions.")
		elif choice in ('q', 'quit', 'exit'):
			print("Goodbye!")
			break
		else:
			print("Unknown option")


if __name__ == '__main__':
	main()

