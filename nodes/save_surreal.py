from surrealist import Surreal

SURREAL_URL = ""
SURREAL_NAMESPACE = ""
SURREAL_USER = ""
SURREAL_PASSWORD = ""
SURREAL_TABLE = ""

class SaveJsonToSurreal:
   
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required": {
                "database": ("STRING", {"multiline": False}),
                "json": ("JSON",),
                "id": ("STRING", {"multiline": False}),
                "key": ("STRING", {"multiline": False})
            },
        }

    RETURN_TYPES = ()

    FUNCTION = "main"
    OUTPUT_NODE = True
    CATEGORY = "database_ops"

    def main(self, database: str, id: str, key: str, json: str) -> None:
        surreal_client = Surreal(SURREAL_URL, namespace=SURREAL_NAMESPACE, database=database, credentials=(SURREAL_USER, SURREAL_PASSWORD), use_http=True, timeout=10)
        surreal_connection =  surreal_client.connect()
        query = f"CREATE {SURREAL_TABLE}:`{id}` CONTENT {{'{key}': {json}}};"
        surreal_connection.query(query)


class SaveTextToSurreal:
   
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required": {
                "database": ("STRING", {"multiline": False}),
                "text":  ("STRING", {"multiline": True}),
                "id": ("STRING", {"multiline": False}),
                "key": ("STRING", {"multiline": False})
            },
        }

    RETURN_TYPES = ()

    FUNCTION = "main"
    OUTPUT_NODE = True
    CATEGORY = "database_ops"

    def main(self, database: str, id: str, key: str, text: str) -> None:
        surreal_client = Surreal(SURREAL_URL, namespace=SURREAL_NAMESPACE, database=database, credentials=(SURREAL_USER, SURREAL_PASSWORD), use_http=True, timeout=10)
        surreal_connection =  surreal_client.connect()
        query = f"CREATE {SURREAL_TABLE}:`{id}` CONTENT {{'{key}': '{text}'}};"
        surreal_connection.query(query)
