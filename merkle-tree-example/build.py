import hashlib
import json
from collections import OrderedDict
import leveldb

class MerkTree:
	def __init__(self, datas=None):
		self.datas = datas
		self.tree = OrderedDict()

	def create_tree(self):
		datas = self.datas
		data_length = len(datas)
		tree = self.tree
		temp_data = []

		for index in range(0,data_length,2):
			current = datas[index]

			if index+1 != data_length:
				current_right = datas[index+1]
			else:
				current_right = ''
			current_hash = hashlib.sha256(current.encode('utf-8'))

			if current_right != '':
				current_right_hash = hashlib.sha256(current_right.encode('utf-8'))

			tree[datas[index]] = current_hash.hexdigest()

			if current_right != '':
				tree[datas[index+1]] = current_right_hash.hexdigest()

			if current_right != '':
				temp_data.append(current_hash.hexdigest() + current_right_hash.hexdigest())
			else:
				temp_data.append(current_hash.hexdigest())

		# call function again
		if len(datas) != 1:
			self.datas = temp_data
			self.tree = tree
			self.create_tree()

	def get_tree(self):
		return self.tree

	def get_root_leaf(self):
		lastkey = next(reversed(self.tree))
		return self.tree[lastkey]

if __name__ == "__main__":
	test_datas = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
	merktree = MerkTree()
	
	hexs = []
	for test_data in test_datas:
		tmp_merktree = MerkTree()
		tmp_merktree.datas = test_data
		tmp_merktree.create_tree()
		hexs.append(tmp_merktree.get_root_leaf())
		print("====================")
		print('root : ',tmp_merktree.get_root_leaf())
		print('tree : ', json.dumps(tmp_merktree.get_tree(), indent=4))
	
	merktree.datas = hexs
	merktree.create_tree()
	print("====================")
	print('root : ',merktree.get_root_leaf())
	print('tree : ', json.dumps(merktree.get_tree(), indent=4))

