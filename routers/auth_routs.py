from fastapi import APIRouter, HTTPException
from supabase_db.connect_supabase import get_supabase_client
from models.users import UserAuth, UserAuthEmailReset
from core.security import get_current_user
from fastapi import Depends
from models.users import UserProfile


supabase = get_supabase_client()

router = APIRouter(prefix="/api", tags=["users"])


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



@router.get("/profile", summary="Get user profile", description="Returns current authenticated user profile")
def get_me(current_user = Depends(get_current_user)):
    return {
        "user_id": current_user.id,
        "email": current_user.email,
        "name": current_user.user_metadata.get("name")
    }



@router.put("/profile/name", summary="Add or update user name", description="Add or update current user name")
def update_me(data: UserProfile, current_user = Depends(get_current_user)):
    try:
        response = supabase.auth.update_user({
            "data": {"name": data.name}
        })

        return {
            "message": "Profile updated successfully",
            "name": response.user.user_metadata.get("name")
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
