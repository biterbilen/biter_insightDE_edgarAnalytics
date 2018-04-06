"""
Unit test for Pq
"""
from __future__ import absolute_import
import os

import unittest

from pq import Pq, Node

class TestPq(unittest.TestCase):
    """Test for Pq"""
    def test_insert(self):
        """test for insert"""
        session = Pq(2, "dummy.out")
        session.insert(Node("101.81.133.jja", "2017-06-30", "00:00:00"))
        self.assertEqual(
            str(session),
            "101.81.133.jja,2017-06-30 00:00:00,2017-06-30 00:00:00,1,1")
        os.remove("dummy.out")
        
    def test_remove(self):
        """test for remove"""
        session = Pq(2, "dummy.out")
        session = Pq(2, "dummy.out")
        session.insert(Node("101.81.133.jja", "2017-06-30", "00:00:00"))
        session.remove(Node("101.81.133.jja", "2017-06-30", "00:00:01"))
        self.assertEqual(
            str(session),
            "101.81.133.jja,2017-06-30 00:00:00,2017-06-30 00:00:00,1,1")
        os.remove("dummy.out")

if __name__ == '__main__':
    unittest.main()
