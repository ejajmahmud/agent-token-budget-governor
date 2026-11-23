"""CLI for Agent Token Budget Governor."""
import argparse
from .core import TokenBudgetGovernor

def main():
    parser = argparse.ArgumentParser(description="Agent Token Budget Governor CLI")
    parser.add_argument("--demo", action="store_true", help="Run token budget governor demo")
    args = parser.parse_args()

    gov = TokenBudgetGovernor(max_tokens=10000)
    status = gov.record_usage(3000, 2000)
    print(f"Recorded 5000 tokens. Consumed: {status.consumed}/{status.total_budget} ({status.percentage*100:.1f}%)")
    print("In soft cap warning?", gov.is_in_soft_cap())
    print("Can proceed with 6000 token step?", gov.can_proceed(6000))

if __name__ == "__main__":
    main()
