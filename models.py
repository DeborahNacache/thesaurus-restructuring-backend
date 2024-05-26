from typing import List
from pydantic import BaseModel

class TreeTerm(BaseModel):
    level: int
    address: str
    hebrewDescription: str
    englishDescription: str    
    termId: int
    wordInTermId: int    
    category: str
    numOfDescendants: int    
    
class Term(BaseModel):  
    termId: int
    termHebrewDescription: str
    termEnglishDescription: str       
    termYears: List[str]
    termkeysWords: List[str] 
    termWords: List[str]
    numOfWordsInTerm:int
    numOfWordsInDictionary:int
    wordHebrewDecsription: str
    wordEnglishDecsription: str
    additionalsTermAppearance : List[str]
    numOfAdditionalsTermAppearance: int
    
    
class Word(BaseModel):
    wordIdInTerm: int
    wordId: int
    wordHebrewDescription: str
    wordEnglishDescription: str
    unpreferedWords: List[str]