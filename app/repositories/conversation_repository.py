from app.database.connection import get_connection


def save_conversation(user_message: str, bot_response: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations (user_message, bot_response)
        VALUES (?, ?)
        """,
        (user_message, bot_response)
    )

    conn.commit()
    conn.close()


def get_conversations(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT TOP (?) id, user_message, bot_response, created_at
        FROM conversations
        ORDER BY id DESC
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    return rows
