# Class Attributes vs Instance Attributes in Python: One Line That Breaks Your Counter

> [IMAGE GOES HERE — screenshot of your own terminal, see notes at the bottom]

While building a `Rectangle` class for a Holberton project, I had to keep a running count of how many rectangles existed. I wrote `self.number_of_instances += 1` inside `__init__`, and the count stayed stubbornly wrong — every rectangle insisted there was exactly one of it. The fix was a single word: `Rectangle.number_of_instances += 1`. That one-word difference is the whole topic of this post, and once I understood why it mattered, a lot of Python stopped feeling arbitrary.

## What is a class attribute

A class attribute belongs to the class itself, and every instance shares the exact same one. You define it in the body of the class, outside any method:

```python
class Dog:
    species = "Canis familiaris"      # class attribute

    def __init__(self, name):
        self.name = name              # instance attribute


a = Dog("Rex")
b = Dog("Fido")

print(a.species)              # Canis familiaris
print(b.species)              # Canis familiaris
print(a.species is b.species) # True - literally the same object
```

There's one string in memory, and both dogs point at it. Change it on the class and every instance sees the change immediately:

```python
Dog.species = "Canis lupus"
print(a.species, b.species)   # Canis lupus Canis lupus
```

In my `Rectangle` class there are two of these: `number_of_instances = 0`, a counter shared by every rectangle, and `print_symbol = "#"`, a default the class provides for drawing itself.

## What is an instance attribute

An instance attribute belongs to one specific object and nothing else. It's normally created inside `__init__` by assigning to `self`:

```python
def __init__(self, width=0, height=0):
    self.width = width
    self.height = height
```

Each rectangle gets its own `width` and `height`. Changing one rectangle's width has no effect on any other, which is exactly what you want — width is a property of a particular rectangle, not of rectangles in general. That's the question worth asking every time: *does this belong to the thing, or to the kind of thing?*

## Every way to create them, and the Pythonic one

For class attributes, you can declare them in the class body, add them after the class exists, or use `setattr`:

```python
class Empty:
    pass

Empty.added_later = 1
setattr(Empty, "via_setattr", 2)
```

For instance attributes, you can assign to `self` inside any method, assign from outside the class, use `setattr`, or write straight into the instance dictionary:

```python
e = Empty()
e.direct = 3
setattr(e, "via_setattr_inst", 4)
e.__dict__["via_dict"] = 5

print(e.__dict__)
# {'direct': 3, 'via_setattr_inst': 4, 'via_dict': 5}
```

All of these work. Almost none of them are what you should write. The Pythonic approach is boring on purpose: **declare class attributes in the class body, and create every instance attribute in `__init__` by assigning to `self`.** The reason is discoverability — anyone reading your class should be able to see its full shape without hunting through the rest of the codebase for a stray `obj.something = ...`. Reach for `setattr` only when the attribute name itself is computed at runtime, and reach for `__dict__[...]` basically never.

## The differences (and the bug that taught me them)

The critical rule: **reading an attribute falls back to the class, but assigning one never does.** When you write `self.x = value`, Python always creates or updates an attribute on *the instance*, even when a class attribute with that name already exists. It doesn't reach up and modify the class.

That's precisely why my counter broke:

```python
class Counter:
    count = 0

    def bump_wrong(self):
        self.count += 1          # reads class (0), writes instance (1)

    def bump_right(self):
        Counter.count += 1       # reads and writes the class
```

```python
c1, c2 = Counter(), Counter()
c1.bump_wrong()
print(c1.count, c2.count, Counter.count)   # 1 0 0
print(c1.__dict__)                         # {'count': 1}
```

`self.count += 1` expands to `self.count = self.count + 1`. The read finds the class attribute `0`, adds one, and then the assignment creates a brand new instance attribute holding `1`. The class attribute never moves. `c1` now shadows the shared counter with its own private copy, which is why every rectangle thought it was alone.

Do it through the class instead and the shared value actually changes:

```python
c3, c4 = Counter(), Counter()
c3.bump_right()
print(c3.count, c4.count, Counter.count)   # 1 1 1
print(c3.__dict__)                         # {} - nothing on the instance
```

Shadowing isn't always a bug, though. It's a feature when you want it. My `__str__` method draws with `self.print_symbol`, which means any single rectangle can override the class default without affecting the others:

```python
r1 = Rectangle(2, 2)
r2 = Rectangle(3, 2)

r1.print_symbol = "*"

print(r1)                      print(r2)
# **                           # ###
# **                           # ###

print(r1.__dict__)   # {'_Rectangle__width': 2, ..., 'print_symbol': '*'}
print(r2.__dict__)   # {'_Rectangle__width': 3, ...}  - untouched
print(Rectangle.print_symbol)  # '#' - class default intact
```

And because the instance attribute merely hides the class one, deleting it brings the original back:

```python
del r1.print_symbol            # the class default is visible again
```

## Advantages and drawbacks

Class attributes cost memory once no matter how many instances you create, and they give you a single place to change a default for everything at once. They're the right tool for constants, shared defaults and counters. The drawback is that sharing is easy to trigger by accident — especially with mutable values:

```python
class Basket:
    items = []                 # one list, shared by every basket

    def add(self, thing):
        self.items.append(thing)

x, y = Basket(), Basket()
x.add("apple")
print(y.items)                 # ['apple']  <- y never added anything
```

Note that `self.items.append(...)` is a *mutation*, not an assignment, so there's no shadowing to save you here — it reaches the shared list directly. The fix is to make it an instance attribute, which gives each basket its own list:

```python
class FixedBasket:
    def __init__(self):
        self.items = []        # a new list per instance
```

Instance attributes give you exactly that isolation, which makes objects independent and easier to reason about. Their cost is memory: every instance carries its own dictionary of attributes. For a handful of objects this is irrelevant; for millions it isn't, which is where `__slots__` comes in — it drops the per-instance dictionary entirely in exchange for a fixed set of allowed names.

## How Python actually stores all this: `__dict__`

None of the above is magic. Attributes live in ordinary dictionaries, and you can look at them.

Every instance has a `__dict__` holding only what belongs to that object:

```python
r1 = Rectangle(2, 2)
print(r1.__dict__)
# {'_Rectangle__width': 2, '_Rectangle__height': 2}
```

Two things stand out. `print_symbol` and `number_of_instances` are absent — they live on the class, not here. And the private `self.__width` shows up as `_Rectangle__width`, because double-underscore names get mangled with the class name to avoid collisions in subclasses.

The class has its own `__dict__` containing class attributes *and* methods, since methods are just class attributes that happen to be functions:

```python
print([k for k in Rectangle.__dict__ if not k.startswith("__")])
# ['number_of_instances', 'print_symbol', 'width', 'height',
#  'area', 'perimeter', 'bigger_or_equal', 'square']
```

One difference: a class's `__dict__` is a `mappingproxy`, a read-only view, so you can't write through it:

```python
Rectangle.__dict__["print_symbol"] = "@"
# TypeError: 'mappingproxy' object does not support item assignment
```

Use `Rectangle.print_symbol = "@"` instead. (`vars(obj)` is just a friendlier spelling of `obj.__dict__`, and for instances it returns the same dictionary object.)

With that, the lookup rule is simple enough to state in one sentence: **when you read `obj.x`, Python checks `obj.__dict__` first, then the class's `__dict__`, then each parent class up the inheritance chain, and raises `AttributeError` if nobody has it.** Every behaviour in this post follows from that one sentence plus the fact that assignment always writes to the instance.

## What I took away

I used to treat "class attribute" and "instance attribute" as trivia to memorise for a quiz. They're not. They're a design decision you make every time you add a field — does this belong to the thing, or to the kind of thing? — and Python's answer to "where does this value actually live?" is always the same: look in the dictionaries. My broken counter was Python doing exactly what I told it to. I just hadn't understood what I'd said.
