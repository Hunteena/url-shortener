from pydantic import BaseModel, HttpUrl

class ShortenRequest(BaseModel):
    url: HttpUrl

class ShortenResponse(BaseModel):
    short_url: HttpUrl
    code: str
    url: HttpUrl
