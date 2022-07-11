# A python module to validate schema for different collections.

class CreateValidator:
    """
    A class to create validator for different collections.
    """

    def __init__(self):
        pass

    @staticmethod
    def create_result_validator():
        """
        Create a validator for result collection
        :return: result validator
        """
        results_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["signal_to_noise", "dispersion_measure"],
                "properties": {
                    "signal_to_noise": {
                        "bsonType": "double",
                        "description": "must be a float and is required"
                    },
                    "dispersion_measure": {
                        "bsonType": ["double", "int"],
                        "description": "must be a float or integer and is required"
                    }
                }
            }
        }

        return results_validator

    @staticmethod
    def create_raw_data_validator():
        """
        Create a validator for raw_data collection.
        :return: raw_data validator
        """
        raw_data_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["ra", "dec", "instrument_id"],
                "properties": {
                    "ra": {
                        "bsonType": ["double", "int"],
                        "description": "must be a float or integer and is required"
                    },
                    "dec": {
                        "bsonType": ["double", "int"],
                        "description": "must be a float or integer and is required"
                    },
                    "instrument_id": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        }

        return raw_data_validator

    @staticmethod
    def instrument_validator():
        """
        Create a validator for instrument collection
        :return: instrument validator
        """
        instrument_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["_id", "location"],
                "properties": {
                    "_id": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "location": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        }

        return instrument_validator
