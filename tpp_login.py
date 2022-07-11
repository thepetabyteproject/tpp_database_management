#!/usr/bin/python3
import pymongo


def login_connect_to_database(host='localhost', port=27017):
    """
    Connect to the server and check for databases. If no any databases found then create one.
    Also list all the collections in the database if the database already exists.
    :param host: server hosting the database
    :param port: port of the server
    :return: Database object
    """
    client = pymongo.MongoClient(host, port)

    # check for tpp database and if there is no tpp database then create it.
    if 'tpp' in client.list_database_names():
        print("There is already a 'tpp' database. Connecting to it.....")
        db = client.tpp
        print("The followings are the collections in the tpp database:")
        for i, collection in enumerate(db.list_collection_names()):
            print(f"{i + 1}) --> {collection}")

    else:
        print("There is no 'tpp' database so creating one.....")
        db = client.tpp

    return db


if __name__ == "__main__":
    login = login_connect_to_database()
