from flask import Flask, render_template, request, Response
from flask import jsonify
import glob
import os
import sys
from io import BytesIO 

def is_safe_path(basedir, path, follow_symlinks=True):
  # resolves symbolic links
  if follow_symlinks:
    return os.path.realpath(path).startswith(basedir)

  return os.path.abspath(path).startswith(basedir)

app = Flask(__name__)
tree_pub = { "title" : "kb", "expanded": "true", "folder": "true" , "children": [] }
# tree_stack = []

@app.route('/')
def index():
	return render_template("index.html", title = 'Projects')


@app.route('/download', methods=["POST"])
def download(file_type = '.md'):
	paths = request.json
	paths.sort()
	output = "#Secure Code Advisor\nBy @[vikasprogrammer](https://twitter.com/vikasprogrammer)\n\n"
	for path in paths:
		
		orig_path = path
		path = "kb/" + path
		if is_safe_path(os.getcwd(), path):
			print(path)
			f = open(path, "r")
			contents = f.read()
			print(contents)
			output = output + "## " + orig_path + "\n"
			output = output + contents + "\n"
			f.close()
			# break
	
	return output


@app.route('/json')
def json():
	global tree_pub
	from pathlib import Path
	tree_int = {}
	for path in Path('kb').rglob('*'):
		items = str(path).split('/')
		root = tree_int
		deep_level = 1
		for item in items:
			# print(root)
			deep_level = deep_level + 1
			if item not in root:
				root[item] = {}
				# add_pub(item, deep_level)
				# root[item]
			root = root[item]
			pass


# 	# print(tree_int['kb'])
# 	# exit()
	# tree_int = { "kb" : { "2" : { "a" : { "x" : {} }, "b" : {}}}}

	maketree(tree_int['kb'], tree_pub)
	tree_final = tree_pub
	# tree_pub = 
	tree_pub = { "title" : "kb", "expanded": "true", "folder": "true" , "children": [] }
# 	print(tree_final)
# 	# tree_final = { "a" : {"title": "Books", "expanded": true, "folder": true, "children":[]}};
	return jsonify(tree_final)


def maketree(d, current_root):
  for k, v in d.items():
  	# print("{0} : {1}".format(k, v))
  	empty = { "title" : "", "expanded": True, "folder": True , "children": [] }
  	empty['title'] = k
  	if v != {}:
  		# print("F - {0} : {1}".format(k, v))
  		current_root['children'].append(empty)
  		maketree(v, empty)
  	else:
  		# print("S - {0} : {1}".format(k, v)
  		empty["folder"] = False
  		current_root['children'].append(empty)
  		# return empty
  		# return empty
		





if __name__ == '__main__':
   app.run(debug = True)