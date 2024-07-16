from surrealist import Surreal, Connection as SurrealConnection

SURREAL_URL = ""
SURREAL_NAMESPACE = ""
SURREAL_USER = ""
SURREAL_PASSWORD = ""
SURREAL_TABLE = ""

class SaveToSurreal:
   
    @classmethod    
    def INPUT_TYPES(s):
        return {
            "required": {
                "database": ("STRING", {"multiline": False}),
                "json": ("JSON",),
                "id": ("STRING", {"multiline": False})
            },
        }

    RETURN_TYPES = ()

    FUNCTION = "main"
    OUTPUT_NODE = True
    CATEGORY = "database_ops"

    def main(self, database: str, json: str, id: str) -> None:
        surreal_client = Surreal(SURREAL_URL, namespace=SURREAL_NAMESPACE, database=database, credentials=(SURREAL_USER, SURREAL_PASSWORD), use_http=True, timeout=10)
        surreal_connection =  surreal_client.connect()
        query = f"CREATE {SURREAL_TABLE}:`{id}` CONTENT {{'json': {json}}};"
        surreal_connection.query(query)

