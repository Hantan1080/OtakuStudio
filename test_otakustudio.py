# test_otakustudio.py
"""
Tests for OtakuStudio module.
"""

import unittest
from otakustudio import OtakuStudio

class TestOtakuStudio(unittest.TestCase):
    """Test cases for OtakuStudio class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OtakuStudio()
        self.assertIsInstance(instance, OtakuStudio)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OtakuStudio()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
