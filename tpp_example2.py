import tpp_login

db = tpp_login.login_connect_to_database()


results_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["signal_to_noise", "dispersion_measure"],
                "properties": {
                    "signal_to_noise": {
                        "bsonType": "double",
                        "description": "must be a float or integer and is required"
                    },
                    "dispersion_measure": {
                        "bsonType": ["int","double"],
                        "description": "must be a float and is required"
                    }
                },
                "additionalProperties": False
            }
        }


try:
    db.command("collMod", 'results', validator=results_validator)
    print('Validator update successful....')

except Exception as e:
    print(e)



