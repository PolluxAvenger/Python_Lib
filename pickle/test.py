# coding=utf-8

import pickle

if __name__ == "__main__":
	data_list = [1, 2, 3]
	data = pickle.dumps(data_list)
	raw_data = pickle.loads(data)