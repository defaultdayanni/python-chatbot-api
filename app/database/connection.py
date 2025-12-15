import pyodbc


def get_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=ChatbotDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return connection


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Conexão com SQL Server realizada com sucesso!")
        conn.close()
    except Exception as e:
        print("❌ Erro ao conectar no SQL Server")
        print(e)
