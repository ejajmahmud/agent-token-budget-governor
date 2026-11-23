"""Core Token Budget Governor implementation."""
from typing import Dict, Any

class BudgetStatus:
    def __init__(self, consumed: int, total_budget: int, percentage: float, is_exceeded: bool):
        self.consumed = consumed
        self.total_budget = total_budget
        self.percentage = percentage
        self.is_exceeded = is_exceeded

class TokenBudgetGovernor:
    def __init__(self, max_tokens: int = 50000, soft_cap_ratio: float = 0.8):
        self.max_tokens = max_tokens
        self.soft_cap_ratio = soft_cap_ratio
        self.consumed_tokens = 0
        self.turn_history = []

    def record_usage(self, prompt_tokens: int, completion_tokens: int) -> BudgetStatus:
        tokens = prompt_tokens + completion_tokens
        self.consumed_tokens += tokens
        self.turn_history.append({"prompt": prompt_tokens, "completion": completion_tokens, "total": tokens})

        pct = round(self.consumed_tokens / self.max_tokens, 4)
        exceeded = self.consumed_tokens >= self.max_tokens
        return BudgetStatus(self.consumed_tokens, self.max_tokens, pct, exceeded)

    def can_proceed(self, estimated_tokens: int = 1000) -> bool:
        return (self.consumed_tokens + estimated_tokens) <= self.max_tokens

    def is_in_soft_cap(self) -> bool:
        return (self.consumed_tokens / self.max_tokens) >= self.soft_cap_ratio
