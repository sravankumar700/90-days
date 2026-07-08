
def print_section(title):
	print('\n' + '=' * 60)
	print(title)
	print('=' * 60)


def basics():
	print_section('1) Variables and basic types')
	a = 10                # int
	b = 3.14              # float
	c = True              # bool
	d = 'hello'           # str
	print('int:', a, 'float:', b, 'bool:', c, 'str:', d)


def collections():
	print_section('2) Collections: list, tuple, set, dict')
	lst = [1, 2, 3]
	tpl = (1, 2, 3)
	st = {1, 2, 3}
	dd = {'a': 1, 'b': 2}
	print('list:', lst)
	print('tuple:', tpl)
	print('set:', st)
	print('dict:', dd)


def control_flow():
	print_section('3) Control flow: if/else, for, while')
	x = 5
	if x % 2 == 0:
		print('x is even')
	else:
		print('x is odd')

	print('for loop:')
	for i in range(3):
		print(i, end=' ')
	print('\nwhile loop:')
	n = 3
	while n > 0:
		print(n, end=' ')
		n -= 1
	print()


def functions_and_args():
	print_section('4) Functions, args, kwargs, lambda')

	def add(a, b=1):
		return a + b

	print('add(2):', add(2))
	print('add(2,3):', add(2, 3))
	f = lambda x: x * 2
	print('lambda:', f(5))


def comprehensions_generators():
	print_section('5) List/set/dict comprehensions & generator')
	sq = [i * i for i in range(5)]
	st = {i for i in range(5)}
	dd = {i: str(i) for i in range(3)}
	gen = (i for i in range(3))
	print('squares:', sq)
	print('set comp:', st)
	print('dict comp:', dd)
	print('generator values:', list(gen))


def classes_exceptions():
	print_section('6) Classes and exception handling')

	class Greeter:
		def __init__(self, name):
			self.name = name

		def greet(self):
			return f'Hello, {self.name}!'

	g = Greeter('World')
	print(g.greet())

	try:
		1 / 0
	except ZeroDivisionError as e:
		print('Caught exception:', type(e).__name__)


def file_io_modules():
	print_section('7) File I/O and modules')
	# write and read a temporary file
	fname = 'temp_demo.txt'
	with open(fname, 'w', encoding='utf-8') as f:
		f.write('line1\nline2')
	with open(fname, 'r', encoding='utf-8') as f:
		print('file contents:', f.read())


def useful_tools():
	print_section('8) map/filter/zip/enumerate/sorted')
	data = [3, 1, 2]
	print('sorted:', sorted(data))
	print('map*2:', list(map(lambda x: x * 2, data)))
	print('filter>1:', list(filter(lambda x: x > 1, data)))
	print('zip:', list(zip(['a', 'b'], [1, 2])))
	print('enumerate:', list(enumerate(['x', 'y'])))


def advanced_brief():
	print_section('9) Generators, iterators, decorators (brief)')

	def gen():
		for i in range(3):
			yield i

	print('generator produced:', list(gen()))

	def deco(f):
		def wrapper(*a, **k):
			return f(*a, **k)

		return wrapper

	@deco
	def say(x):
		return x

	print('decorator call:', say('hi'))


def main():
	basics()
	collections()
	control_flow()
	functions_and_args()
	comprehensions_generators()
	classes_exceptions()
	file_io_modules()
	useful_tools()
	advanced_brief()


if __name__ == '__main__':
	main()
