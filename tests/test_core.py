"""Tests for TokenBudgetGovernor."""
import unittest
from agent_token_budget_governor.core import TokenBudgetGovernor

class TestTokenBudgetGovernor(unittest.TestCase):
    def test_governor_limits(self):
        g = TokenBudgetGovernor(max_tokens=1000, soft_cap_ratio=0.8)
        s1 = g.record_usage(400, 400)
        self.assertEqual(s1.consumed, 800)
        self.assertTrue(g.is_in_soft_cap())
        self.assertFalse(s1.is_exceeded)

        s2 = g.record_usage(200, 50)
        self.assertTrue(s2.is_exceeded)
        self.assertFalse(g.can_proceed(10))
