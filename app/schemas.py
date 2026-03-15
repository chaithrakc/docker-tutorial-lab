"""
Bank Note measurements for API input validation using Pydantic models.

Created on: 2026-03-15
@author: Chaithra Cheluvaiah
"""
from pydantic import BaseModel

class BankNoteFeatures(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float