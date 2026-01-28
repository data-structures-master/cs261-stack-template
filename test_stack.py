# DO NOT MODIFY THIS FILE
# For credit, uncomment one test at a time and make sure to commit and push after each test passes
# with a commit message that specifies the test name that passed.
# Run me via: python3 -m unittest test_stack or py -m unittest test_stack

import os
import random
import string
import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A Stack exists.
        """
        try:
            Stack()
        except NameError:
            self.fail("Could not instantiate Stack.")

    # def test_initially_empty(self):
    #     """
    #     Test 2: A stack is initially empty.
    #     """
    #     s = Stack()
    #     self.assertTrue(s.is_empty())

    # def test_initial_pop(self):
    #     """
    #     Test 3: Popping from an empty stack raises IndexError.
    #     """
    #     s = Stack()
    #     self.assertRaises(IndexError, s.pop)

    # def test_initial_peek(self):
    #     """
    #     Test 4: Peeking at an empty stack raises IndexError.
    #     """
    #     s = Stack()
    #     self.assertRaises(IndexError, s.peek)

    # def test_initial_push(self):
    #     """
    #     Test 5: Pushing a value onto the stack means the stack is no longer empty.
    #     """
    #     s = Stack()
    #     s.push("fee")
    #     self.assertFalse(s.is_empty())

    # def test_peek_one(self):
    #     """
    #     Test 6: A value pushed onto the stack can be peeked at.
    #     """
    #     s = Stack()
    #     s.push("fee")
    #     self.assertEqual("fee", s.peek())

    # def test_pop_one(self):
    #     """
    #     Test 7: A value pushed onto the stack can be popped.
    #     """
    #     s = Stack()
    #     s.push("fee")
    #     self.assertEqual("fee", s.pop())

    # def test_peek_two(self):
    #     """
    #     Test 8: Peeking at a stack with two values returns the last pushed value.
    #     """
    #     s = Stack()
    #     s.push("fee")
    #     s.push("fi")
    #     self.assertEqual("fi", s.peek())

    # def test_peek_state(self):
    #     """
    #     Test 9: Peeking doesn't mutate the stack.
    #     """
    #     s = Stack()
    #     s.push("fee")
    #     s.push("fi")
    #     self.assertEqual("fi", s.peek())
    #     self.assertEqual("fi", s.peek())

    # def test_pop_two_with_nontrivial_values(self):
    #     """
    #     Test 10: Popping from a stack with two values returns the last pushed value,
    #     even when values are not simple literals.
    #     """
    #     rng = seeded_rng()
    #     s = Stack()
    #     first_value = make_value(rng, 1)
    #     second_value = make_value(rng, 2)
    #     s.push(first_value)
    #     s.push(second_value)
    #     self.assertIs(second_value, s.pop()) if isinstance(second_value, _Token) else self.assertEqual(second_value, s.pop())

    # def test_pop_state(self):
    #     """
    #     Test 11: Popping removes the last pushed value from the stack.
    #     """
    #     rng = seeded_rng()
    #     s = Stack()
    #     first_value = make_value(rng, 1)
    #     second_value = make_value(rng, 2)
    #     s.push(first_value)
    #     s.push(second_value)
    
    #     if isinstance(second_value, _Token):
    #         self.assertIs(second_value, s.pop())
    #     else:
    #         self.assertEqual(second_value, s.pop())
    
    #     if isinstance(first_value, _Token):
    #         self.assertIs(first_value, s.pop())
    #     else:
    #         self.assertEqual(first_value, s.pop())
    
    #     self.assertTrue(s.is_empty())

# --- helpers ---

class _Token:
    def __init__(self, label):
        self.label = label
    def __repr__(self):
        return f"_Token({self.label})"


def seeded_rng():
    seed = os.environ.get("STACK_SEED", "local-default-seed")
    return random.Random(seed)


def rand_text(rng, n=12):
    chars = string.ascii_letters + string.digits
    return "".join(rng.choice(chars) for _ in range(n))


def make_value(rng, i):
    # Mix of tokens and normal strings
    if i % 2 == 0:
        return _Token(rand_text(rng, 8))
    return f"VAL-{rand_text(rng, 10)}"

if __name__ == "__main__":
    unittest.main()
