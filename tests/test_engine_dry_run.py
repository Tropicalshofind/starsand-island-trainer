from starsand_trainer.core.engine import TrainerEngine


def test_engine_attaches_in_dry_run():
    cfg = {"process_name": "StarsandIsland.exe", "game_build": "2026.03"}
    engine = TrainerEngine(config=cfg, dry_run=True)
    engine.attach()
    assert engine.memory is not None
    assert engine.memory.dry_run is True
    engine.shutdown()