import os
from supabase import create_client
from dotenv import load_dotenv


def get_supabase_client():
    """
    Create a Supabase client using environment variables.
    Returns:
        Client: A Supabase client instance.
    """
    load_dotenv()

    url = os.getenv("SUPABASE_API_URL_TASKFORGE")
    key = os.getenv("SUPABASE_API_KEY_TASKFORGE")

    client = create_client(url, key)
    return client


def test_connection(client):
    """Patikrina ryšį su Supabase."""
    try:
        client.auth.get_session()
        print("Supabase klientas sukurtas sėkmingai!")
    except Exception as e:
        print(f"Error from test_connection: {e}")


if __name__ == "__main__":
    client = get_supabase_client()
    test_connection(client)
