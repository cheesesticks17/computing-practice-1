# Built-in imports

def is_palindrome(s: str) -> bool:
    '''takes in a string and returns bool depending on if its a palindrome '''
    length = len(s)
    if length < 2:
        return True
    if s[0] != s[length - 1]:
        return False
    if length > 2:
        if not is_palindrome(s[1:length - 1]):
            return False
    return True

def generate_permutations(s: str) -> list:
    '''takes in a string and returns a list of every permutation'''
    if len(s) == 0:
        return [""]
    results = []
    for i in range (len(s)):
        newstr = s[:i] + s[i + 1:]
        permlist = generate_permutations(newstr)
        for j in range (len(permlist)):
            for k in range(len(s)):
                letters = list(permlist[j])
                letters.insert(k, s[i])
                permutation = "".join(letters)
                if not permutation in results:
                    results.append(permutation)
    return results

def num_paths(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 1
    sum = num_paths(m - 1, n) + num_paths(m, n - 1)
    return sum

if __name__ == '__main__': #just for testing and bugfixing
    print(num_paths(2, 2))  # Output: 6
    print(num_paths(1, 1))  # Output: 2
    print(num_paths(3, 2))  # Output: 10
    print(num_paths(0, 5))
    pass