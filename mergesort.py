import re, random
from typing import List, Union


def main(inp: Union[List[int], str]) -> Union[List[int], str]:

    if isinstance(inp, str):
        res = do_str(inp.lower())

    elif isinstance(inp, list):
        res = sort(inp)

    else:
        return 1

    return res


def do_str(inp: str, sepWords = True) -> str:
    """This method is used to handle sorting strings. By default, it will 
    preserve words and sort them but can be changed to just sort the 
    words together"""
    
    res = []
    done = ""
    pattern = "[a-z]+"
    myString = re.findall(pattern, inp)
    
    if sepWords == True:
        for word in myString:
            rascii = [ord(char) for char in word]
            sort_this = sort(rascii)
            res.append(sort_this)



    else:
        "".join(myString)
        rascii = [ord(char) for char in myString]
        res = sort(rascii)
        return "".join(res)

    for good_sort in res:
        for number in good_sort:
            done += chr(number)
        
        done += " "

    return done


def sort(inp: List[int]) -> List[int]:
    res = []
    sz = len(inp)

    if sz > 2:
        front = sort(inp[:(sz // 2)])
        back = sort(inp[(sz // 2):])        

        res += merge(front, back)
        
    if sz == 2:
        if inp[0] > inp[1]:
            inp[0], inp[1] = inp[1], inp[0]

    if sz <= 2:
        return inp

    return res


def merge(inp: List[int], pinp: List[int]) -> List[int]:
    res = []
    
    #iterate over the two lists and go as we find the lower of the two
    while inp and pinp:
        if inp[0] > pinp[0]:
            res.append(pinp.pop(0))
            
    
        elif inp[0] < pinp[0]:
            res.append(inp.pop(0))

    
        else:
            res.append(inp.pop(0))
            res.append(pinp.pop(0))

    #whichever list still has input we just put that into our result        
    if inp:
        res += inp

    elif pinp:
        res += pinp

    return res


if __name__ == "__main__":
    randlist = []
    for _ in range(300000):
        randlist.append(random.randint(1, 50000))    
    
    mysort = main(randlist)
    print(mysort)

