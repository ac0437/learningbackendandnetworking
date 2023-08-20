from pydantic import BaseSettings

class Settings(BaseSettings):
    smtp_server: str
    smtp_port: int
    sender_email: str
    sender_password: str
    recipient_email: str
    json_file:str

    class Config:
        env_file = '.env'

settings = Settings()