# Task

It is necessary to create a full-fledged left-sided red-black search tree. And implement
in it a method of adding new elements with balancing.

The red-black tree has the following criteria:

- Each node has a color (red or black)
- The root of the tree is always black
- The new node is always red
- Red nodes can only be the left child
- At the crane node, all children are black

Accordingly, in order for these conditions to be met, after adding an element to
the tree, it is necessary to perform balancing, thanks to which all the criteria
above will become valid. There are 3 operations for balancing – a small left turn,
a small right turn and a color change.
