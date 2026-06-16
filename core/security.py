from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase_db.connect_supabase import get_supabase_client


security = HTTPBearer()
supabase = get_supabase_client()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        user = supabase.auth.get_user(token)

        if not user:
            raise HTTPException(status_code=401, detail="Token invalid")

        return user.user

    except Exception as e:
        print("KLAIDA:", e)
        raise HTTPException(status_code=401, detail="Token invalid")
