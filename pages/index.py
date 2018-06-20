from format import *
import os
import re

def list_pages(title, page_list):
	h3(title)
	start_ul()
	for page in page_list:
		title = re.sub('_', ' ', page).title()
		print('<li><a href="' + page + '">' + title + '</a></li>')
	end_ul()

base('base.html')

start_content()

linear_algebra = ['hadmard_product']
probability = ['event', 'kolmogorov_axioms', 'sample_space', 'sigma_algebra']
set_theory = ['set']

list_pages('Linear Algebra', linear_algebra)
list_pages('Probability Theory', probability)
list_pages('Set Theory', set_theory)

end_content()