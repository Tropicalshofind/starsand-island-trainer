from starsand_trainer.services.offset_registry import OffsetRegistry


def test_known_build_returns_offsets():
    reg = OffsetRegistry("2026.03")
    assert reg.get("player_stamina") == 0x02A1B4C0
    assert "inventory_base" in reg.keys()


def test_unknown_build_raises():
    try:
        OffsetRegistry("1999.01")
    except KeyError:
        return
    raise AssertionError("expected KeyError for unknown build")