import os
from subprocess import call

### general html format
### <tag>content</tag>

def html(tag, content = '', classes = '', ids = ''):
	open_tag = '<' + tag + ' class="' + classes + '" id="' + ids + '"">'
	close_tag = '</' + tag + '>'

	out = open_tag + content + close_tag

	print(out)

### meta

def base(base_file):
	print('{%- extends "' + base_file + '" %}')

def start_content():
	print('{% block content %}<div class="container center-block content section">')

def end_content():
	print('</div>{%- endblock %}')

def start_div(classes = '', ids = ''):
	print('<div class="' + classes + '" id="' + ids + '">')

def end_div():
	print('</div>')
### headlines

def headline(level = '1', content = '', classes = '', ids = ''):
	tag = 'h' + level
	return html(tag, content, classes, ids)

def h1(content = '', classes = '', ids = ''):
	return headline('1', content, classes, ids)

def h2(content = '', classes = '', ids = ''):
	return headline('2', content, classes, ids)

def h3(content = '', classes = '', ids = ''):
	return headline('3', content, classes, ids)

def h4(content = '', classes = '', ids = ''):
	return headline('4', content, classes, ids)

def h5(content = '', classes = '', ids = ''):
	return headline('5', content, classes, ids)

### paragraphs

def p(paragraph, classes = '', ids = ''):
	return html('p', paragraph, classes, ids)

### code blocks
def code(expression, classes = '', ids = ''):
	tempin_file = 'tempin.py'
	tempout_file = 'tempout.txt'

	# tempin = open(tempin_file, 'w')
	# tempin.write(expression)

	with open(tempin_file, 'w') as tempin:
		tempin.write(expression)

	with open(tempout_file, 'w+') as output:
		call(
			['python', tempin_file],
			stdout = output
		)

	# with open(tempout_file) as file:
	# 	output_text = file.readlines()

	# out = ''

	# if os.path.getsize(tempout_file) > 0:
	# 	out = out + '<pre></code>' + output_text + '</code></pre>'

	open_tag = '<pre><code'
	close_tag = '</code></pre>'

	print(open_tag + expression + close_tag)

### lists

def start_ul(classes='', ids=''):
	print('<ul class="' + classes + '" id="' + ids + '">')

def end_ul():
	print('</ul>')

def li(content='', classes='', ids=''):
	print('<li class="' + classes + '" id="' + ids + '">' + content + '</li>')

### hyperlinks

def link(content, href = '#', local = True):
	if local:
		url = href# + '.html'
	else:
		url = href

	return '<a href="' + url + '">' + content + '</a>'

def youtube(source = '', width='560', height='315'):
	div = '<div class="embed-responsive embed-responsive-16by9">'
	iframe = '<iframe width="' + width + '" height="' + height + '" src="' + source + '"></iframe>'
	print(div + iframe + '</div>')

if __name__ == '__main__':
    main()