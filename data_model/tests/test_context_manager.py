from src.context_manager import ContextManager


def test_context_manager():
    context = ContextManager()
    assert context.is_closed is False
    with context:
        assert bool(context) is True

    assert context.is_closed is True
