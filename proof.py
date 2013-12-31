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
print "\nComplex number examples:"
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
print "\nEquation example:"
a = ComplexNumber(8, 5)
b = ComplexNumber(3, 2)
print (a - b).conj()                        # -> 5 + -3i
print a.conj() - b.conj()                   # -> 5 + -3i
print (a - b).conj() == a.conj() - b.conj() # -> True

# Great, it looks like the equation holds for those values.
# How about a few more?
print "\nMore equation examples:"
az = [ComplexNumber(8, 5),  ComplexNumber(-2, 3), ComplexNumber(-9, -3), ComplexNumber(1027, -304)]
bz = [ComplexNumber(9, -2), ComplexNumber(8, 4),  ComplexNumber(6, 9),   ComplexNumber(0, 0)      ]
for a,b in zip(az, bz):
  print (a - b).conj() == a.conj() - b.conj() # -> True every time!

# But this does not prove the equation true, you say.
# Well, what if we try for 10000 different randomly generated examples?
# TODO uncomment this block.
print "\nRandomly generated examples:"
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

# We will now create a class to represent something that is not quite a number.
# It will behave a lot like a number, but without every having an actual value.
# We will call such nebulous artifacts "variables" for now. I'm not sure that is
# quite the right word, you can decide for yourself.
# TODO explain uniqueness.
# TODO note "immature method of dealing" with possible equality, crashing.

# We will put Variables inside ComplexNumbers as real and imaginary components.
# So Variables will need to be able to do everything that a number does.

class Variable(object):
  """
  Variables are like numbers, but they have no value.

  Variables must be able to do everything that
  """

  def __init__(self):
    """
    Each Variable we create will have its own unique identity.
    It will be distinctly differentiable from every other Variable
    that exists. However, we must make this so WITHOUT assigning
    a value to the variable.

    I will whimsically name each Variable's bit of uniqueness
    it's immortal soul. There are many ways to do this, but in
    this example the soul is implemented as a dictionary which we
    will only use by comparing it's location in memory to other
    dictionary souls using the 'is' operator.
    """
    self.soul = {}

  def __add__(left, right):
    """ The sum of two variables in an object representing just that. """
    return VariableSum(left, right)

  def __sub__(left, right):
    """ The difference of two variables in an object representing just that. """
    return VariableDifference(left, right)

  def __pos__(self):
    """ +v is the same as v """
    return self

  def __neg__(self):
    """ -v is the negated version of the variable v """
    return NegatedVariable(self)

  def __eq__(left, right):
    # TODO WHAT!?!?
    # This is called explicit type checking.
    # Some python people would tell me this is bad.
    # They would rather I just found a way for NegatedVariables to have souls
    # and compare them without knowing it.
    # NegatedVariables do not currently have souls. Oh well.
    if isinstance(left, NegatedVariable) and isinstance(right, NegatedVariable):
      return -left == -right
    elif left.soul is right.soul:
      return True
    else:
      # TODO this is dumb.
      raise Exception("I'm confused. Are two distinct variables equal. Who am I to say? They could be. Is one variable equal to its negative?")

  def __ne__(left, right):
    # TODO WHAT!?!?
    if left.soul is right.soul:
      return False
    else:
      # TODO this is dumb.
      raise Exception("I'm confused. Are two distinct variables not equal?")

# Whew, that's pretty weird.
# We seem to have referenced a bunch of classes in the methods of Variable
# which do not exist yet. Let's go ahead and create those classes.

class VariableSum(object):
  """ A VariableSum represents the result of adding two Variables """

  def __init__(self, left, right):
    """ A variable sum stores the left and right elements in the addition """
    self.left = left
    self.right = right

  def __neg__(self):
    """
    To negate a sum like -(x + y),
    just negate it's parts  (-x + -y)
    """
    return VariableSum(-self.left, -self.right)

  def __eq__(left, right):
    """ Check whether a sum of variables is the same as another sum of variables. """
    # Yes, this line is confusing.
    if left.left == right.left and left.right == right.right:
      return True
    else:
      # Yeah, there are other ways that sums could be equal.
      # For example, (a + b) = (b + a)
      # I think we should just crash.
      raise Exception("Sums could be equal, not sure. If you want to use this comparison in a proof then write more code.")

  def __neq__(left, right):
    """ Check whether a sum of variables is NOT the same as another sum of variables. """
    if left.left == right.left and left.right == right.right:
      return False
    else:
      # Yeah, there are other ways that sums could be equal.
      # For example, (a + b) = (b + a)
      # I think we should just crash.
      raise Exception("Sums could be equal, not sure. If you want to use this comparison in a proof then write more code.")


def VariableDifference(left, right):
  """
  Surprise! I'm not going to make VariableDifference a class.
  I know, and you were just starting to see where this was going.
  I'm sorry. But think about it like this.

  A VariableDifference is really just a VariableSum
  but where the second operand has been negated.
  In other words (a - b) = (a + (-b)).

  Since we know how to add, and we know how to negate, we
  can make VariableDifference look like a constructor, but
  really return an instance of VariableSum.
  """
  return VariableSum(left, -right)

class VariableDifference(object):
  """
  A VariableDifference is just like a VariableSum.
  """
  def __init__(self, left, right):
    self.left = left
    self.right = right

class NegatedVariable(Variable):
  """
  Notice the Variable appears above instead of object.
  This denotes that a NegatedVariable is really a kind of Variable.
  Technically, NegatedVariable inherits all of the methods of
  from Variable. So NegatedVariables know how to do all the same tricks,
  like participating in addition and stuff.

  The exception is negation. NegatedVariable has its own special definition
  of negation, which you will see below.
  """
  def __init__(self, variable):
    self.variable = variable

  def __neg__(self):
    """
    A twice negated variable is just the original variable.
    -(-v) = v
    """
    return self.variable

# TODO im confused
print "\nGeneral evaluation:"
a = ComplexNumber(Variable(), Variable())
b = ComplexNumber(Variable(), Variable())
print (a - b).conj() == a.conj() - b.conj() # -> True


# TODO tada
