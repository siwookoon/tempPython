# -*- coding: utf-8 -*-

# context manager 작성
import contextlib
import sqlite3

@contextlib.c.ontextmanager
def db_coonect(url):

    db = sqlite3.connect(url)
    yield db
    db.close()

def main():
    url = None
    db_coonect(url)