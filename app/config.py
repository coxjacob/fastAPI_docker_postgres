from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = "university_api_db"
    DATABASE_USER: str = "university_api_user"
    DATABASE_PASSWORD: str = "university_api_password"


settings = Settings()

# Adding values to config.py is not ideal, but pytest.ini did not work. 