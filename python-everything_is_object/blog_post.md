# Everything in Python Is an Object — and Three Bugs That Taught Me What That Means

> [IMAGE GOES HERE — screenshot of your own terminal, see notes at the bottom]

I just finished a project called "Python: Mutable, Immutable... everything is object!" and going in, I thought this was going to be the easy one. Variables hold values, some things can be changed, some can't, move on. Then I opened my own repo to finish the last few tasks and found three files I'd gotten wrong. One of them was a function that returned an empty string every single time it was called, and I had never noticed, because it didn't crash. It just quietly did nothing. That's the thing about this topic — when you misunderstand it, Python usually doesn't yell at you. It just gives you the wrong answer. So this post is what I actually learned, mostly by being wrong first.

## id and type

Every value in Python is an object, and every object carries three things around with it: a type, an identity, and a value. `type()` gives you the first one, `id()` gives you the second. The identity is a number that's unique to that object for as long as it exists — in CPython it's literally the memory address.

```python
n = 42
s = "hello"

print(type(n))   # <class 'int'>
print(type(s))   # <class 'str'>
print(id(n))     # 140703...  (a big number, different on your machine)
```

Where this gets useful is the difference between `==` and `is`. `==` asks "do these have the same value?" and `is` asks "are these literally the same object?"

```python
p = [1, 2, 3]
q = [1, 2, 3]

print(p == q)   # True  - same contents
print(p is q)   # False - two separate objects
```

There's a wrinkle here I want to flag, because almost every tutorial I read while studying got it wrong. Python keeps a permanent cache of small integers from -5 to 256, so `a = 256; b = 256; a is b` is `True`. Those same tutorials then say that 257 will give you `False`. On my machine (Python 3.12) it gives `True`:

```python
c = 257
d = 257
print(c is d)   # True (!)
```

The reason is that the compiler stores `257` once as a constant for that block of code, and both names point at that one constant. To actually see two distinct objects, you have to force one to be built at runtime:

```python
print(int("257") is int("257"))   # False
```

I spent a while confused by this, and the takeaway stuck with me better than the original lesson would have: `is` is a question about objects, not about numbers. And the answer can depend on *when* the object gets created.

## Mutable objects

A mutable object can be changed in place. Its value changes, its identity doesn't. Lists, dictionaries and sets are the ones you meet first.

```python
my_list = [1, 2, 3]
before = id(my_list)

my_list.append(4)

print(my_list)                # [1, 2, 3, 4]
print(id(my_list) == before)  # True - still the same object
```

Same object, different contents. Which sets up the trap that got me:

```python
a_list = [1, 2, 3]
b_list = a_list
b_list.append(4)

print(a_list)   # [1, 2, 3, 4]
```

I didn't copy anything there. `b_list = a_list` just handed the same object a second name, and now anything I do through one name shows up through the other.

## Immutable objects

An immutable object can't be changed, full stop. Integers, floats, strings, tuples, booleans and frozensets. When it *looks* like you're modifying one, what's really happening is that Python builds a brand new object and re-points the name at it:

```python
t = "Best"
before = id(t)

t += "School"

print(t)                # BestSchool
print(id(t) != before)  # True - this is a different object now
```

The original `"Best"` was never touched. It just lost its last name and got cleaned up.

Tuples deserve a warning of their own, because "immutable" is narrower than it sounds. A tuple can't change *which* objects it holds — but if one of those objects is itself mutable, that object is still fair game:

```python
tup = (1, [2, 3])
tup[1].append(4)
print(tup)      # (1, [2, 3, 4])

tup[0] = 99     # TypeError: 'tuple' object does not support item assignment
```

The tuple is frozen. Its contents are not.

## Why the distinction matters

Three practical reasons, and they're worth knowing before you hit them the hard way.

The first is shared state. Because assignment never copies, two parts of your program can end up pointing at one mutable object without anybody intending it, and a change made in one place surfaces somewhere unrelated. Immutable objects are immune to this by construction, which is exactly why Python can hand out the same cached `256` to everyone without any risk.

The second is hashability. Dictionary keys and set members have to be hashable, and mutability breaks that — if an object's value could change after it was filed away under a hash, you'd never find it again. That's why `d[(1, 2)] = "ok"` works and `d[[1, 2]] = "nope"` raises `TypeError: unhashable type: 'list'`.

The third is that Python optimises aggressively around immutability. Caching small integers, reusing identical string constants, storing literals once per code block — all of that is only safe because nobody can modify those objects out from under anyone else.

## How arguments get passed to functions

Python is not pass-by-value and it's not pass-by-reference. The phrase that finally made it click for me is **pass-by-assignment**: the parameter name inside the function gets bound to the same object the caller passed in, exactly as if you'd written `parameter = argument`.

So whether a function can affect the caller has nothing to do with functions, and everything to do with whether the object is mutable and what you do to it:

```python
def add_item(items):
    items.append("new")      # mutates the object

def rebind(items):
    items = ["different"]    # rebinds the local name only

def increment(number):
    number += 1              # int is immutable - makes a new object

lst = ["original"]

add_item(lst)
print(lst)      # ['original', 'new']   <- caller sees it

rebind(lst)
print(lst)      # ['original', 'new']   <- caller sees nothing

val = 5
increment(val)
print(val)      # 5                     <- caller sees nothing
```

`add_item` reached through the name and changed the object itself. `rebind` only pointed its own local name at a new list, and the caller's list never heard about it. `increment` couldn't have worked no matter what, because integers can't be modified. Same syntax, three different outcomes, and the deciding factor is always the object rather than the call.

## The advanced tasks, and the three bugs

The advanced tasks are where this stopped being theory for me.

**Copying a list** had to be done in three lines, no imports. The answer is a slice: `return a_list[:]`, which builds a new list object holding the same references. `new == old` is `True` and `new is old` is `False`, which is the whole point. My existing version worked but I'd named the parameter `l` — a single lowercase L, which pycodestyle flags as ambiguous because it's hard to tell from `1` in a lot of fonts. Fair. Worth also knowing the limit: a slice is a *shallow* copy, so a list of lists still shares its inner lists.

```python
nested = [[1, 2], [3, 4]]
shallow = nested[:]
shallow[0].append(99)
print(nested)   # [[1, 2, 99], [3, 4]] - inner lists are shared
```

**`magic_string()`** was the empty-string bug. It has to return "BestSchool" repeated once more on each call, in four lines, with no imports and no global variable. My old version set a counter to 0 *inside* the function, so it reset on every call and multiplied the string by zero — no error, no output, nothing. The fix uses the mutable default argument, which is normally considered a Python gotcha:

```python
def magic_string(count=[0]):
    count[0] += 1
    return ", ".join(["BestSchool"] * count[0])
```

Default arguments are evaluated once, when the function is defined, and then stored on the function object itself. Because that default is a *list*, it's mutable, so it survives between calls and carries the count. This is the exact behaviour that causes the classic `def f(x, bucket=[])` bug where results pile up across calls — here it's the feature instead of the bug. You can even see the state hanging off the function afterwards with `magic_string.__defaults__`.

**`LockedClass`** had to block new instance attributes except `first_name`. My file for it was empty. The answer is `__slots__`:

```python
class LockedClass:
    __slots__ = ["first_name"]
```

Normally every instance carries a `__dict__` — a dictionary of its attributes — which is why you can bolt anything onto a Python object at runtime. `__slots__` removes that dictionary and reserves fixed storage for exactly the names you list. Anything else fails:

```python
lc = LockedClass()
lc.first_name = "John"     # fine
lc.last_name = "Snow"      # AttributeError: 'LockedClass' object has no attribute 'last_name'
```

The task is titled "low memory cost" and that's the real reason `__slots__` exists — dropping the per-instance dictionary saves a significant amount of memory when you're creating a lot of objects. Locking the attributes is a side effect.

## What I'm taking away

The sentence "everything in Python is an object" sounded like trivia to me a week ago. It isn't. It's the thing that explains why two variables can share a list, why `+=` on a string is secretly building a new one, why a function can change your data or completely fail to, and why a default argument can remember things between calls. Once you start asking "which object is this name pointing at, and can that object be changed?" a whole category of confusing bugs stops being confusing.

Three of mine had been sitting in my repo the whole time.
