from student_code import shortest_path
import pickle


def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

# map_40 is a bigger map than map_10
map_40 = load_map('map-40.pickle')

path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)