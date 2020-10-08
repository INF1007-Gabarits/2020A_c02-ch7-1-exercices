#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index):
	return (
		0 if index == 0 else
		1 if index == 1 else
		get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2)
	)

def get_fibonacci_sequence(length, sequence=[0, 1]):
	return (
		sequence[0:length] if length <= len(sequence) else
		get_fibonacci_sequence(length, sequence + [sequence[-1] + sequence[-2]])
	)

def get_sorted_dict_by_decimals(dict_arg):
	return dict(sorted(dict_arg.items(), key = lambda elem: elem[1] % 1.0))

def fibonacci_numbers(length):
	yield 0
	if length >= 2:
		yield 1
	last_elems = deque([0, 1])
	for i in range(2, length):
		fibo_number = last_elems[0] + last_elems[1]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number

def build_recursive_sequence_generator(initial_values, definition, keep_whole_sequence=False):
	def recursive_generator(length):
		for elem in zip(initial_values, range(length)):
			yield elem[0]
		last_elems = deque(initial_values)
		for i in range(len(initial_values), length):
			current_number = definition(last_elems)
			last_elems.append(current_number)
			if not keep_whole_sequence:
				last_elems.popleft()
			yield current_number
	return recursive_generator

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2, 1], lambda seq: seq[-1] + seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda seq: seq[-2] + seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda seq: seq[-seq[-1]] + seq[-seq[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
