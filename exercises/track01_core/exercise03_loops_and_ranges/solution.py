from __future__ import annotations


def project_balances(
    initial: float, monthly_deposit: float, months: int
) -> list[float]:
    if months < 0:
        raise ValueError("months must not be negative")

    balances: list[float] = []
    balance = initial
    for _ in range(months):
        balance += monthly_deposit
        balances.append(balance)
    return balances
