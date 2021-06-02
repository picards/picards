import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
import uuid
from app import conf

import psycopg2
from psycopg2.errors import SerializationFailure

# Connect to the "studypi" database.
conn = psycopg2.connect(
    dbname = conf.DBNAME,
    user = conf.USER,
    password = conf.PASSWORD,
    sslmode = conf.SSLMODE,
    sslrootcert = conf.SSLROOTCERT,
    port = conf.PORT,
    host = conf.HOST,
    options = conf.OPTIONS
)

# Make each statement commit immediately.
conn.set_session(autocommit=True)

# Open a cursor to perform database operations.
cur = conn.cursor()

def create_tables():
    # create accounts table
    cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
        user_id char(36) NOT NULL UNIQUE,
        email varchar(320) NOT NULL UNIQUE
    );""")

    # create study_sets table
    cur.execute("""CREATE TABLE IF NOT EXISTS study_sets (
        set_id char(36) NOT NULL UNIQUE,
        set_name varchar(255) NOT NULL
    );""")

    # create flashcards table
    cur.execute("""CREATE TABLE IF NOT EXISTS flashcards (
        card_id char(36) NOT NULL UNIQUE,
        set_id char(36) NOT NULL,
        question varchar NOT NULL,
        answer varchar NOT NULL
    );""")

    # create set_perms table
    cur.execute("""CREATE TABLE IF NOT EXISTS set_perms (
        user_id char(36) NOT NULL,
        set_id char(36) NOT NULL,
        perm bit(4) NOT NULL
    );""")

def drop_tables():
    cur.execute("""DROP TABLE IF EXISTS accounts; DROP TABLE IF EXISTS study_sets;
    DROP TABLE IF EXISTS flashcards; DROP TABLE IF EXISTS set_perms;""")

def create_account(user_id, email):
    cur.execute("""
    INSERT INTO accounts (user_id, email)
    VALUES ('{0}', '{1}')
    ON CONFLICT DO NOTHING;
    """.format(user_id, email))
    print_accounts()

def create_flashcard(user_id, set_name, question, answer, set_owner_id = None):
    card_id = str(uuid.uuid3(uuid.NAMESPACE_X500, user_id + question + answer))

    set_id = None
    if set_owner_id == None:
        set_id = str(uuid.uuid3(uuid.NAMESPACE_X500, user_id + set_name))
    else:
        set_id = str(uuid.uuid3(uuid.NAMESPACE_X500, set_owner_id + set_name))

    cur.execute("""
    INSERT INTO study_sets (set_id, set_name)
    VALUES ('{0}', '{1}')
    ON CONFLICT DO NOTHING;
    """.format(set_id, set_name))

    
def print_accounts():
    cur.execute("SELECT * FROM accounts;")
    print("--------------------------------------------------------------------------------------------")
    print("|                                        accounts                                          |")
    print("|------------------------------------------------------------------------------------------|")
    for row in cur.fetchall():
        print("| " + row[0] + " | " + row[1] + (50-len(row[1]))*' ' + '|')
    print("--------------------------------------------------------------------------------------------")


drop_tables()
create_tables()