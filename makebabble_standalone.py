#!/usr/bin/env python3
# description: generate random gibberish resembling business-like talk.
#              Very useful during meetings and interviews.
# author: Carmelo C
# email: carmelo.califano@gmail.com
# date (ISO 8601): 2020-08-18

# Import some modules
import argparse	# Parser for command-line options, arguments and sub-commands
import random	# Generate pseudo-random numbers
import sqlite3	# DB-API 2.0 interface for SQLite databases

# Global variables
dbName = 'gibberish.db'
tables = ['adjectives', 'nouns', 'verbs']
itemsCount = {'numA':0, 'numN':0, 'numV':0}

def main():
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    for t, i in zip(tables, sorted(itemsCount.keys())):
        c.execute('SELECT count(*) FROM {table};'.format(table=t))
        itemsCount[i] = c.fetchone()[0]

    getA = random.randrange(itemsCount['numA']) + 1
    getN = random.randrange(itemsCount['numN']) + 1
    getV = random.randrange(itemsCount['numV']) + 1

    c.execute('SELECT adj FROM adjectives WHERE id = {id};'.format(id=getA))
#    print(itemsCount['numA'], getA, c.fetchone())
    out = list(c.fetchone())

    c.execute('SELECT noun FROM nouns WHERE id = {id};'.format(id=getN))
#    print(itemsCount['numN'], getN, c.fetchone())
    out += list(c.fetchone())

    c.execute('SELECT verb FROM verbs WHERE id = {id};'.format(id=getV))
#    print(itemsCount['numV'], getV, c.fetchone())
    out += list(c.fetchone())

    print(out)

    conn.close()

if __name__ == '__main__':
	main()

