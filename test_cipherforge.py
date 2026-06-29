# test_cipherforge.py
"""
Tests for CipherForge module.
"""

import unittest
from cipherforge import CipherForge

class TestCipherForge(unittest.TestCase):
    """Test cases for CipherForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CipherForge()
        self.assertIsInstance(instance, CipherForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CipherForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
