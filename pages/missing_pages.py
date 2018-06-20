from format import *
import os
# from lxml import html
# from HTMLParser import HTMLParser
# import requests

# class MyHTMLParser(HTMLParser):
# 	def handle_starttag(self, tag, attrs):
# 		print('Encountered a start tag:' + tag)

# 	def handle_endtag(self, tag):
# 		print('Encountered an end tag :' + tag)

# 	def handle_data(self, data):
# 		print('Encountered some data. :' + tag)

# links = tree.xpath('//a[]/text()')

# parser = MyHTMLParser()
# parser.feed('')

def list_missing(title, topic_list):
	h5(title)
	start_ul()
	for topic in topic_list:
		print('<li>' + topic + '</li>')
	end_ul()

base('base.html')

start_content()

h1('Content Needed')

casella_berger = [
	'countable/uncountable sample spaces',
	'event containment/equality',
	'sample space union/intersection/complement',
	'empty set',
	'properties of operation (commutativity, associativity, distributive laws, De Morgan\'s Laws',
	'disjoint events/mutually exclusive',
	'set partition',
	'borel field',
	'trivial sigma algebra',
	'axioms of probability/kolmogorov',
	'theorem 1.2.6',
	'axiom of countable/finite additivity',
	'properties of probability function',
	'theorem 1.2.8/1.2.9',
	'bonferonni\'s inequality',
	'theorem 1.2.11',
	'boole\'s inequality',
	'fundamental theorem of counting',
	'with replacement',
	'without replacement',
	'factorial',
	'ordered, with replacement',
	'ordered, without replacement',
	'unordered, with replacement',
	'unordered, without replacement',
	'combination',
	'permutation',
	'binomial coefficient'
]

schaums_set_theory = [
	'solution set',
	'properties of sets',
	'proper subset',
	'disjoint sets'
]

list_missing('Casella/Berger', casella_berger)
list_missing('Schaum\'s Set Theory', schaums_set_theory)

end_content()