pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. Fetch Development Dependencies: ``make install``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example with a bucket name:

::

    $pgbackup postgre://bob@example.com:5432/db_name --driver s3 backups


Local Example with local path:

::

    $$pgbackup postgre://bob@example.com:5432/db_name --driver local /var/local/db_name/backups/dump.sql


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $make

if virtualenv isn't active then use:

::

    $pipenv run make


