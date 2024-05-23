from typing import List
from pydantic import BaseModel

class TreeTerm(BaseModel):
    level: int
    address: str
    hebrewDescription: str
    englishDescription: str    
    term: int
    wordInTerm: int    
    category: str
    numOfDescendants: int    
    
class Term(BaseModel):  
    term: int
    hebrewDescription: str
    englishDescription: str       
    termYears: List[str]
    keysWords: List[str] 