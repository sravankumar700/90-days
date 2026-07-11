
import random


def get_names(expected=12):
	print(f"Enter {expected} names (separated by commas or newlines).")
	data = []
	try:
		s = input().strip()
	except EOFError:
		s = ''
	if ',' in s:
		parts = [p.strip() for p in s.split(',') if p.strip()]
		data.extend(parts)
	elif s:
		data.append(s)
	# read remaining names if needed
	while len(data) < expected:
		try:
			line = input().strip()
		except EOFError:
			break
		if not line:
			continue
		if ',' in line:
			parts = [p.strip() for p in line.split(',') if p.strip()]
			data.extend(parts)
		else:
			data.append(line)
	return data[:expected]


def make_teams(names, teams=3):
	# create `teams` teams splitting evenly
	random.shuffle(names)
	n = len(names)
	size = n // teams
	res = []
	for i in range(teams):
		res.append(names[i*size:(i+1)*size])
	return res


def main():
	names = get_names(12)
	if len(names) != 12:
		print("Need exactly 12 names. Exiting.")
		return
	print("\nChoose output mode:\n1) 3 teams of 4 players each\n2) 4 teams of 3 players each\n3) list all pairs (combinations of 2)")
	choice = input("Choice [1]: ").strip() or '1'
	if choice == '1':
		teams = make_teams(names, teams=3)
		for i, t in enumerate(teams, 1):
			print(f"Team {i}: {', '.join(t)}")
	elif choice == '2':
		teams = make_teams(names, teams=4)
		for i, t in enumerate(teams, 1):
			print(f"Team {i}: {', '.join(t)}")
	elif choice == '3':
		from itertools import combinations
		pairs = list(combinations(names, 2))
		for i, p in enumerate(pairs, 1):
			print(f"Pair {i}: {p[0]} & {p[1]}")
	else:
		print("Invalid choice.")


if __name__ == '__main__':
	main()
