from __future__ import annotations


def delivery_fee(
    order_total: float, distance_km: float, is_member: bool = False
) -> float:
    raise NotImplementedError
