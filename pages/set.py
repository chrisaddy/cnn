from format import *
import os

base('base.html')

start_content()

h1('Definition')

p(
"""
A <em>set</em> is a collection of objects called <em>elemets</em>.
"""
)

h3('That\'s a little vague, right?')

p('Yes.')

h3('Yea, I thought so. Let\'s take a closer look.')

p(
"""
A collection of numbers, say the integers 1 through 10, can be considered a set.
The primary colors (red, green, blue) could be considered a set. The cities north of the equator form a set.
And so on.
"""
)

h3('Useful Notation')

p(
"""
A set is usually denoted by a capital letter, i.e., $A$.
Elements of a set are often listed inside of brackets, separated by commas.
For example, the set $B$ that contains the odd positive integers less than 10 would be written

$$
	B = \\left\\{1, 3, 5, 7, 9\\right\\}.
$$

This notation is referred to as <em>tabular form</em>. For sets that are hard to specify explicitly, we often
use <em>set-builder form</em>. For example, the set $A$ that contains all values of $x$ in the real numbers whose square root is greater than 10 as

$$
	A = \\left\\{x: x \\in \mathbb{R}, \\sqrt{x} > 10\\right\\}
$$
"""
)

p(
"""
If an element $a$ belongs to a set $A$ we denote this as

$$
	a \\in A.
$$

However, if the object $b$ is not an element of $A$, we denote this as

$$
	b \\not\\in A.
$$
"""
)

h3('Special Sets')

p(
"""
There are a few sets that are used often enough that they have their own notation.

$$
\\begin{align}
	\\mathbb{N} &= \\left\\{0, 1, 2, 3, ...\\right\\}\\\\
	\\mathbb{P} &= \\left\\{1, 2, 3, 4, ...\\right\\}\\\\
	\\mathbb{Z} &= \\left\\{..., -3, -2, -1, 0, 1, 2, 3, ...\\right\\}\\\\
	\\mathbb{Q} &= \\text{The rational numbers.} \\\\
	\\mathbb{R} &= \\text{The real numbers.} \\\\
	\\mathbb{C} &= \\text{The complex numbers.} \\\\
	\\textbf{U} &= \\text{The universal set.} \\\\
	\\emptyset &= \\left\\{\\right\\}
\\end{align}
$$
"""
)

p(
"""
Above, we can define the natural numbers, positive integers, integers, and the null set ($\\mathbb{N}$, $\\mathbb{P}$, $\\mathbb{Z}$, and $\\emptyset$, respectively),
by listing the elements belonging to those sets. These sets are specified or <em>defined</em>.
"""
)

p(
"""
The <em>universal set</em> $\\textbf{U}$ is the set within which all sets belong. See Russell's Paradox.
"""
)

p(
"""
The null set $\\emptyset$ is the set with no elements. There is only one empty set.
"""
)



h3('Set Equality')

p(
"""
We say that two sets $A$ and $B$ are equal, written $A = B$, iff all elements of $A$ are in $B$ and all elements of $B$ are in $A$.
"""
)

h3('Subsets/Containment')

p(
"""
We say that a set $A$ is a <strong>subset</strong> of a set $B$ (or that $B$ contains $A$) if every element in $A$ is also in $B$. We write this

$$
	A \\subseteq B
$$

If one or more elements of $A$ are not in $B$, we write $A$ is <strong>not a subset</strong> of $B$ as

$$
	A \\not\\subseteq B
$$

We can then redefine set equality in terms of subsets

$$
	A = B \\iff A \\subseteq B \\text{ and } B \\subseteq A
$$
"""
)

h4('Other properties of subsets')

p('Consider any sets $A$, $B$, and $C$.')

p(
"""
The null set $\\emptyset$ is a subset of all other sets and all sets are subsets of the universal set $\\textbf{U}$
$$
	\\emptyset \\subseteq A \\subseteq \\textbf{U} \\\\

$$
"""
)

p(
"""
Since $A = A$ by definition,

$$
	A \\subseteq A
$$
"""
)

p(
"""
If $A$ is a subset of $B$ and $B$ is a subset of $C$

$$
	A \\subseteq B \\subseteq C \\Rightarrow A \\subseteq C
$$
"""
)


end_content()