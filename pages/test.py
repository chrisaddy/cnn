from format import *
import os

base('base.html')

start_content()

h1('This is a header')
h2('This is also a header')
h3('Ditto')
h4('Samezees')
h5('Enough already with the headers, we get it.')

p('This is a paragraph')

### this is some code that isn't displayed

n = 1000
m = 100


### this is some code that is displayed

p(str(n) + ' youth have taken the survey in ' + str(m) + ' programs.')

outside_link = link("Google", "http://google.com", False)
inside_link = link("Hadamard Product", "linear_algebra/hadamard_product")



p('this is a ' + str(outside_link))
p('this is a ' + str(inside_link))

p('the hadamard is ' + str(link('here', 'linear_algebra/hadamard_product')))

# p('this is a ' + str(in_link))

end_content()

# for page in pages