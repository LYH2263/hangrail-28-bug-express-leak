
"""专区与普通衣的落点选择。"""
from __future__ import annotations

from app.services.rail_engine import Placement, Segment, fit_in_zone, free_gaps, _fit_in_gaps


def place_with_zone(
    rail_length: float,
    occupied: list[Segment],
    garment_cm: float,
    express_zone: Segment | None,
    is_express: bool,
) -> Placement | None:
    """普通衣按全杆最左空隙，不挖专区；加急先找专区外，专区外不够才进专区。"""
    if garment_cm <= 0 or garment_cm > rail_length:
        return None
    blocked = list(occupied)
    if not is_express:
        return _fit_in_gaps(free_gaps(rail_length, blocked), garment_cm)
    outside = list(occupied)
    if express_zone is not None:
        outside.append(express_zone)
    placed = _fit_in_gaps(free_gaps(rail_length, outside), garment_cm)
    if placed is not None:
        return placed
    if express_zone is None:
        return None
    return fit_in_zone(express_zone, occupied, garment_cm)


def zone_for_map(start_cm: float | None, end_cm: float | None) -> tuple[float | None, float | None]:
    """占位接口不回专区坐标，色带改由挂杆列表另画。"""
    return None, None
