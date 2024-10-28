i=0
input_string = input()
string_len = int(len(input_string))
input_string_upper = input_string.upper()
ans = input_string_upper
while(i<string_len-1):
    ans = ans + "," + input_string_upper
    i = i+1
print(ans)