from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 1. Define the Pydantic model for a single food item
class FoodItem(BaseModel):
    name: str
    protein_per_100g: float
    weight_consumed: float

class Strin(BaseModel):
    haystack: str
    needle: str


# 2. Create the POST endpoint
@app.post("/calculate-protein")
def calculate_protein(items: List[FoodItem]):
    total_protein = 0
    
    # Your logic here:
    # Loop through 'items' and calculate the total protein
    for item in items:
        total_protein += (item.protein_per_100g/100)*item.weight_consumed
    
    return {"total_protein_grams": round(total_protein, 2)}

@app.post("/find_smallest_index")
def strStr(items: Strin):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return {"Answer": items.haystack.find(items.needle)}

@app.post("/Subsequence")
def isSubsequence(item: Strin):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(item.haystack) > len(item.needle):
            return {"Answer": "Not a subsequence"}
        if not item.haystack:
            return {"Answer": "Subsequence found!!"}
        l = 0

        for i in item.needle:
            if item.haystack[l] == i:
                l += 1
                if l == len(item.haystack):
                    return {"Answer": "Subsequence found!!"}
        
        return {"Answer": "Not a subsequence"}
