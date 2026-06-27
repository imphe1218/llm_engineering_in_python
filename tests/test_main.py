from llm_engineering_in_python import main


def test_main_runs_without_error(capsys):
    main()
    captured = capsys.readouterr()
    assert "llm-engineering-in-python" in captured.out
