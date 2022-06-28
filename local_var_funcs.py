import os


def user_info_exporter(**kwargs):
	for key, value in kwargs.items():
		os.system(f'export {key.upper()}="{value}"')


def user_info_getter(*args):
	res_list = []

	for key in args:
		res_list.append(os.environ.get(key))
	else:
		return res_list
