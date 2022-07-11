import pymongo
import tpp_login
import schema

# first login to the database
db = tpp_login.login_connect_to_database()



class CreateCollectionAndInsert:
    """
    Create a collection and insert or if a collection already exists then insert documents.
    """

    def __init__(self, collection_name, document, validator):
        """
        Initialize the following attributes.
        :param collection_name: Name of the collection we want to create or work on.
        :param document: A dictionary file or a list of dictionary or a tuple of dictionary we want to insert.
        :param validator: A schema validator that sets a schema for the collection_name we want to create.
        """
        self.document = document
        self.validator = validator
        self.collection_name = collection_name

    def check_create_insert_to_collection(self, insert_to_coll):
        """
        This checks for a collection and if no collection exists then create the collection.
        :param insert_to_coll: This is a method from the same class which performs insertion.
        :return:  None

        """

        if self.collection_name not in db.list_collection_names():
            print(f"The collection '{self.collection_name}' doesn't exist so creating one...")

            # This creates a collection with a validator/schema
            db.create_collection(self.collection_name, validator=self.validator)
            insert_to_coll()


        else:
            print(f"The collection '{self.collection_name}' already exists so performing insertion.")

            # If a collection already exists then this implements schema on the collection.
            db.command("collMod", self.collection_name, validator=self.validator)
            insert_to_coll()


    def insert_to_collection(self):
        """
        Inserts dictionary, list of dictionaries or a tuple of dictionaries to a collection.
        :return: None
        """

        collection_name = db[self.collection_name]
        try:
            if isinstance(self.document, list) or isinstance(self.document, tuple):
                insert_process = collection_name.insert_many(self.document)

                if insert_process.acknowledged:
                    print(f"Insert was successful.\n The inserted ids are {insert_process.inserted_ids}")
                else:
                    print(f"Sorry! The insert was not successful.")

            else:
                insert_process = collection_name.insert_one(self.document)
                if insert_process.acknowledged:
                    print(f"Insert was successful.\n The inserted id is {insert_process.inserted_id}")
                else:
                    print(f"Sorry! The insert was not successful.")

        except Exception as e:
            print(f"\n{e}")





# if __name__ == '__main__':
#     pass

    # results = CreateCollectionAndInsert(collection_name= , document=, validator= )
    # surveys.check_create_insert_to_collection(surveys.insert_to_collection)
