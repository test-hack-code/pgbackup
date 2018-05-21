import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_name"

def test_dump_call_pg_dump(mocker):
    """
    Utilize pg_dump to interact with Database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_without_timestamp():
    """
    pgdump.dump_file_name returns the name of the database.
    """
    assert pgdump.dump_file_name(url) == "db_name.sql"


def test_dump_file_name_with_timestamp():
    """
    pgdump.dump_file_name returns the name of the database
    with timestamp appended
    """

    timestamp = "2018-05-21T22:03"
    assert pgdump.dump_file_name(url, timestamp) == "db_name-2018-05-21T22:03.sql"
