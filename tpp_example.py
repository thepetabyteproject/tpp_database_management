import pymongo
import random
from tpp_insert_in_collection import CreateCollectionAndInsert
from schema import CreateValidator

random.seed(42)

##################################################################################################################
"""
___________________
Results Collection |
-------------------

"""

# Creating a dummy document for result collection
# result_document = {'signal_to_noise': 23.6, 'dispersion_measure': 180}
#
# results_validator = CreateValidator().create_result_validator()
# results = CreateCollectionAndInsert(collection_name='results', document=result_document, validator=results_validator)
# results.check_create_insert_to_collection(results.insert_to_collection)



#####################################################################################################################
"""
_____________________
Raw Data Collection  |
---------------------
"""


# Creating dummy documents for raw_data collection
# raw_data_doc = []
# for x in range(100):
#     instrument_id = random.choice(['gbt', 'chime', 'vla'])
#     ra = random.choice([a for a in range(0, 361)])
#     dec = random.choice([a for a in range(-90, 91)])
#     my_doc = {"ra": ra, "dec": dec, "instrument_id": instrument_id}
#     raw_data_doc.append(my_doc)
#
#
# raw_data_validator = CreateValidator().create_raw_data_validator()
# raw_data = CreateCollectionAndInsert(collection_name='raw_data', document=raw_data_doc, validator=raw_data_validator)
# raw_data.check_create_insert_to_collection(raw_data.insert_to_collection)


######################################################################################################################
"""
_______________________
Instruments Collection |
-----------------------
"""

# Creating a dummy document for instrument collection.
instrument_doc = [{"_id": 'gbt', 'location': 'West Virginia'}, {"_id": "vla", "location": "New Mexico", },
                  {"_id": "chime",
                   "location": "British Columbia"}]

instrument_validator = CreateValidator().instrument_validator()
instruments = CreateCollectionAndInsert(collection_name='instruments', document=instrument_doc,
                                        validator=instrument_validator)

instruments.check_create_insert_to_collection(instruments.insert_to_collection)




####################################################################################################################


















