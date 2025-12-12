import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv(".dev.env")

@dataclass(frozen=True)
class Config:
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")

    @classmethod
    def get_database_url(cls) -> str:
        """
        Retrieve the configured database URL from the environment.
        
        Returns:
            database_url (str): The database connection URL.
        
        Raises:
            ValueError: If the `DATABASE_URL` is not set or is empty.
        """
        if not cls.DATABASE_URL:
            raise ValueError("Database url is not set in .dev.env")

        return cls.DATABASE_URL