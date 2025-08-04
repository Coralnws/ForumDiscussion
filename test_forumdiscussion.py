# test_forumdiscussion.py
"""
Tests for ForumDiscussion module.
"""

import unittest
from forumdiscussion import ForumDiscussion

class TestForumDiscussion(unittest.TestCase):
    """Test cases for ForumDiscussion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ForumDiscussion()
        self.assertIsInstance(instance, ForumDiscussion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ForumDiscussion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
