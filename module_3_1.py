calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    kor = (len(string), string.upper(), string.lower())
    print(kor)
    count_calls()

def is_contains(string, list_to_search):
    string = string.lower()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)