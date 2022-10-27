from typing import List

unique_words = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen"
]

tens_words = [
    "Zero",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety"
]

places = ["Thousand", "Million", "Billion"]


def number_to_words(num: int) -> str:
        
    unassembled_number = []
    
    num_list = map(int, str(num)[::-1])
    
    chunks = split_into_chunks(num_list)
    
    for i, chunk in enumerate(chunks):
        chunk_words = chunk_to_words(chunk, i)
        if chunk_words != "":
            unassembled_number.append(chunk_words)
    
    assembled_nummber = assemble_number(unassembled_number)
        
    return assembled_nummber

def assemble_number(unassembled_number: List[str]) -> str:
    assembled_number = ""
    reversed_number = unassembled_number[::-1]

    for i, s in enumerate(reversed_number):
        assembled_number += s
        if i < len(reversed_number) - 1:
            assembled_number += " "

    return assembled_number

def chunk_to_words(chunk: List[int], chunk_num: int) -> str:
    has_complex_number = False
    chunk_str = ""
    
    if len(chunk) > 2:
        third = chunk[2]
        if third != 0:
            chunk_str += f"{unique_words[third]} Hundred"
    
    if len(chunk) > 1:
        second = chunk[1]
        if second != 0 and second > 1:
            if len(chunk_str) > 0:
                chunk_str += " "
            chunk_str += f"{tens_words[second]}"
        else:
            has_complex_number = True
    
    first = chunk[0]
    number = first
    if has_complex_number:
        number += chunk[1] * 10
    
    if number != 0 or (len(chunk_str) == 0 and chunk_num != 0):
        if len(chunk_str) > 0:
            chunk_str += " "
        chunk_str += f"{unique_words[number]}"

    if chunk_num != 0:
        if len(chunk_str) > 0:
            chunk_str += " "
            chunk_str += f"{places[chunk_num-1]}"

    return chunk_str
        
def split_into_chunks(num_list: List[int]) -> List[List[int]]:
    chunks = []
    current_chunk = []
    
    for i, num in enumerate(num_list):
        if i != 0 and i % 3 == 0:
            chunks.append(current_chunk)
            current_chunk = list()
        current_chunk.append(num)
        
    if len(current_chunk) > 0:
        chunks.append(current_chunk)
    
    return chunks
# split_into_chunks

if __name__ == "__main__":
    print(*[f"{i}: {number_to_words(i)}\n" for i in range(10_000)])
         
                
        
        
        
        
        
        
        
        