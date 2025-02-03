def palindrome(str):
    return str == str[::-1]

str = input()
if palindrome(str):
    print("phrase is palindrome")
else:
    print("phrase is NOT palindrome")