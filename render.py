import subprocess
import os

def render(page):
	render_directory = 'pages/'
	render_file = page
	file_namestem = page[:-3]
	output_file = 'templates/' + file_namestem + '.html'

	with open(output_file, 'w+') as output:
		subprocess.call(
			['python', render_directory + render_file],
			stdout = output
		)

pages = os.listdir('pages')
pages.remove('__pycache__')
pages.remove('format.py')
pages.remove('format.pyc')

def render_all():
	for page in pages:
		render(page)

if __name__ == '__main__':
    main()