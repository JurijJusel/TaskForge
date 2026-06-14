from fastapi import APIRouter, HTTPException
from supabase_db.connect_supabase import get_supabase_client
from models.auth import UserAuth, UserAuthEmailReset


supabase = get_supabase_client()

router = APIRouter(prefix="/api", tags=["auth"])

@router.post("/register")
def register(data: UserAuth):
    try:
        response = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })

        return {
            "message": "User created successfully",
            "user_id": response.user.id
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(data: UserAuth):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })

        return {
            "message": "Connected successfully",
            "access_token": response.session.access_token,
            "user_id": response.user.id
        }

    except Exception as e:
        raise HTTPException(status_code=401, detail="email or password is incorrect")


@router.post("/reset-password")
def reset_password(data: UserAuthEmailReset):
    try:
        supabase.auth.reset_password_email(data.email)
        
        return {"message": "Password reset email sent"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
