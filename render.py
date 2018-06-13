import subprocess

def render(page):
	render_directory = 'pages/'
	render_file = page + '.py'
	output_file = 'templates/' + page + '.html'

	with open(output_file, 'w+') as output:
		subprocess.call(
			['python', render_directory + render_file],
			stdout = output
		)

# def render_all():
# 	for page in pages:


if __name__ == '__main__':
    main()