import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure

# Connect to the "studypi" database.
conn = psycopg2.connect(
    database='studypi',
    user='michael',
    password='3H$xlwl1riDrupan4p7#',
    sslmode='verify-full',
    sslrootcert='../cockroach/ca.crt',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=pure-bull"
)


# Make each statement commit immediately.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations.
cur = conn.cursor()

