import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
import uuid

import psycopg2
from psycopg2.errors import SerializationFailure

# Connect to the "studypi" database.
conn = psycopg2.connect(
    database='studypi',
    user='michael',
    password='3H$xlwl1riDrupan4p7#',
    sslmode='verify-full',
    sslrootcert='app/ca.crt',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=pure-bull-2141"
)

# Make each statement commit immediately.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations.
cur = conn.cursor()

# Create the "accounts" table
cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
    uuid UUID,
    email STRING,
    card_uuids UUID[]
);""")

# Create the "cards" table
cur.execute("""CREATE TABLE IF NOT EXISTS cards (
    uuid UUID,
    question STRING,
    answer STRING
);""")

def print_accounts():
    cur.execute("SELECT * FROM accounts;")
    for record in cur:
        print(record)

def create_account(uuid, email):
    cur.execute("""INSERT INTO accounts (uuid, email)
     VALUES ('{0}', '{1}');""".format(uuid, email))

def create_card(account_uuid, question, answer):
    card_uuid = str(uuid.uuid4())
    cur.execute("SELECT uuid, card_uuids FROM accounts WHERE uuid = {}".format(account_uuid))
    card_uuids = [cur.fetchone()[1], card_uuid]
    cur.execute("""INSERT INTO cards (uuid, question, answer)
     VALUES ('{0}', '{1}', '{2}');""".format(card_uuid, question, answer))
    cur.execute("""UPDATE accounts SET card_uuids = '{0}' WHERE uuid = '{1}';""".format(card_uuids, account_uuid))