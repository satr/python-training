from __future__ import annotations


def delivery_fee(
    order_total: float, distance_km: float, is_member: bool = False
) -> float:
    if is_member or order_total >= 50.0:
        return 0.0

    fee = 5.0
    if distance_km > 5.0:
        fee += (distance_km - 5.0) * 1.5
    return fee
