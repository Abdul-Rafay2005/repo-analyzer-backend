from pydantic import BaseModel, HttpUrl, validator

class AnalyzeRequest(BaseModel):
    input_type: str  # "github" or "url"
    value: HttpUrl

    @validator("input_type")
    def validate_input_type(cls, v):
        if v.lower() not in ["github", "url"]:
            raise ValueError("input_type must be 'github' or 'url'")
        return v.lower()
