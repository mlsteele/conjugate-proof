# We will set out to prove the equation
#   (a - b)* = a* - b*
# where * means complex conjugate.

# We will do this by exploring through programming.
# First, we will tell python what a complex number is
# by creating a class to store the real and imaginary
# components and teach it how to manipulate the numbers
# in such ways as addition and subtraction by using methods
# on the complex number class.

# Python actually has support for complex numbers built in.
# This is fantastic, but we are not going to use its built in
# support. The reason is two-fold. First, it is fun to see
# the inner workings of the complex number class. Secondly,
# writing our own will make it easier to debug, understand,
# and ensure the validity of the funny business we will be doing
# later, which will involve shoveling things that are not quite
# numbers through the complex number class machinery.


class ComplexNumber(object):
  """
  Class for manipulating complex numbers.

  This example is limited to things which might be useful for the
  exercise and thus does not include multiplication or division.
  """

  def __init__(self, real, imag):
    """ Complex numbers have a real and imaginary part. """
    self.real = real
    self.imag = imag

  def conj(self):
    """ Complex conjugate of the number. """
    return ComplexNumber(self.real, -self.imag)

  def __add__(left, right):
    """ Addition operator: x + y """
    return ComplexNumber(left.real + right.real, left.imag + right.imag)

  def __sub__(left, right):
    """ Subtraction operator: x - y """
    return left + (-right)

  def __pos__(self):
    """ Unary plus operator: (+x) """
    return self

  def __neg__(self):
    """ Unary minus operator: -x """
    return ComplexNumber(-self.real, -self.imag)

  def __eq__(left, right):
    """ Equality testing: x == y """
    return (left.real == right.real) and (left.imag == right.imag)

  def __ne__(left, right):
    """ Inequality testing: x != y """
    return not left == right

  def __repr__(self):
    """
    This tells python how to represent ComplexNumber's as strings.
    This way, when we print a ComplexNumber, it shows something
    nice like "8 + 3i"
    """
    return "{} + {}i".format(self.real, self.imag)


# Now that we have our complex number class,
# let's test it out on a few examples.
print "Complex number examples:"
x = ComplexNumber(8, 5)
y = ComplexNumber(3, 2)
print x                        # -> 8 + 5i
print y                        # -> 3 + 2i
print -x                       # -> -8 + -5i
print x + y                    # -> 11 + 7i
print x - y                    # -> 5 + 3i
print -y + x                   # -> 5 + 3i
print x == y                   # -> False
print x == ComplexNumber(8, 5) # -> True
print x.conj()                 # -> 8 + -5i

# Looks good so far.
# The printing for negative imaginary components is a little funky,
# but it's readable enough.

# Now let's try the equation in question with a few examples.
# (a - b)* = a* - b*
print "Equation example:"
a = ComplexNumber(8, 5)
b = ComplexNumber(3, 2)
print (a - b).conj()                        # -> 5 + -3i
print a.conj() - b.conj()                   # -> 5 + -3i
print (a - b).conj() == a.conj() - b.conj() # -> True

# Great, it looks like the equation holds for those values.
# How about a few more?
print "More equation examples:"
az = [ComplexNumber(8, 5),  ComplexNumber(-2, 3), ComplexNumber(-9, -3), ComplexNumber(1027, -304)]
bz = [ComplexNumber(9, -2), ComplexNumber(8, 4),  ComplexNumber(6, 9),   ComplexNumber(0, 0)      ]
for a,b in zip(az, bz):
  print (a - b).conj() == a.conj() - b.conj() # -> True every time!

# But this does not prove the equation true, you say.
# Well, what if we try for 10000 different randomly generated examples?
# TODO uncomment this block.
print "Randomly generated examples:"
# from random import randint
# for _ in xrange(10000):
#   a = ComplexNumber(randint(-1000, 1000), randint(-1000, 1000))
#   b = ComplexNumber(randint(-1000, 1000), randint(-1000, 1000))
#   print (a - b).conj() == a.conj() - b.conj() # -> ... True

# Those all worked!
# The equation seems to hold up.
# It seems very unlikely for there to be holes in the coverage of this equation.
# Is that good enough?
# No?
# Ok. Well let's try to show it more generally then.

# In order to prove the equation generally,
# we will have to stop plugging in actual complex numbers.
# Every time we plug in an actual complex number, we doom ourselves
# to a loss of generality.
# But does that mean that all of our hard work in creating the machinery
# of the ComplexNumber class will go to waste? Certainly not.
# We wil
