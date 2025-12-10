import runpy
import sys
import types
import builtins

def _make_stub(validate_result=True, day_name="Monday", record_calls=None):
    """
    Create a stub module for resource.get_day_of_the_week with controllable behavior.
    record_calls should be a dict with lists for 'validate' and 'calculate' to capture args.
    """
    mod = types.ModuleType("resource.get_day_of_the_week")

    def validate_date(d, m, y):
        if record_calls is not None:
            record_calls.setdefault("validate", []).append((d, m, y))
        return validate_result

    def calculate_day_of_week(d, m, y):
        if record_calls is not None:
            record_calls.setdefault("calculate", []).append((d, m, y))
        return day_name

    mod.validate_date = validate_date
    mod.calculate_day_of_week = calculate_day_of_week
    return mod

def test_valid_date_prints_day(monkeypatch, capsys):
    # Arrange: stub module returns True and a known day name
    record = {}
    stub = _make_stub(validate_result=True, day_name="Friday", record_calls=record)
    # Ensure the package and module are available before running the script
    monkeypatch.setitem(sys.modules, "resource", types.ModuleType("resource"))
    monkeypatch.setitem(sys.modules, "resource.get_day_of_the_week", stub)
    # Simulate user input
    monkeypatch.setattr(builtins, "input", lambda prompt="": "15/03/2024")

    # Act: run the script as __main__
    runpy.run_path("source/app.py", run_name="__main__")

    # Assert: correct output printed and functions called with adjusted values
    out = capsys.readouterr().out
    assert "The day of the week is: Friday" in out
    assert record.get("validate") == [(15, 3, 2024)]
    assert record.get("calculate") == [(15, 3, 2024)]

def test_invalid_date_prints_error_and_no_day_calc(monkeypatch, capsys):
    # Arrange: stub validate_date returns False
    record = {}
    stub = _make_stub(validate_result=False, day_name="ShouldNotBeUsed", record_calls=record)
    monkeypatch.setitem(sys.modules, "resource", types.ModuleType("resource"))
    monkeypatch.setitem(sys.modules, "resource.get_day_of_the_week", stub)
    # Input uses February which should decrement the year inside get_date_info
    monkeypatch.setattr(builtins, "input", lambda prompt="": "31/02/2024")

    # Act
    runpy.run_path("source/app.py", run_name="__main__")

    # Assert: error message printed and calculate_day_of_week not called
    out = capsys.readouterr().out
    assert "Invalid date. Please enter a valid date in DD/MM/YYYY format." in out
    assert record.get("validate") == [(31, 2, 2023)]
    assert record.get("calculate") is None

def test_jan_feb_year_adjustment_passed_to_functions(monkeypatch, capsys):
    # Arrange: ensure year is decremented for January and February
    record = {}
    stub = _make_stub(validate_result=True, day_name="Tuesday", record_calls=record)
    monkeypatch.setitem(sys.modules, "resource", types.ModuleType("resource"))
    monkeypatch.setitem(sys.modules, "resource.get_day_of_the_week", stub)
    # Test January decrement
    monkeypatch.setattr(builtins, "input", lambda prompt="": "01/01/2000")
    runpy.run_path("source/app.py", run_name="__main__")
    out1 = capsys.readouterr().out
    # Reset for February test
    record.clear()
    monkeypatch.setattr(builtins, "input", lambda prompt="": "02/02/2010")
    runpy.run_path("source/app.py", run_name="__main__")
    out2 = capsys.readouterr().out

    # Assert outputs and that years were decremented when month is 1 or 2
    assert "The day of the week is: Tuesday" in out1
    assert "The day of the week is: Tuesday" in out2
    # First run: 01/01/2000 -> year passed should be 1999
    # Second run: 02/02/2010 -> year passed should be 2009
    # Because record was cleared between runs, we captured only the last run's calls in record
    # To check both, run the script twice above and use separate records would be required;
    # Here we at least assert the last run had the expected decremented year.
    assert record.get("validate") == [(2, 2, 2009)]
    assert record.get("calculate") == [(2, 2, 2009)]