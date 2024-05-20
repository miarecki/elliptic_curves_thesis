
message1 = 'KOT'
key = 'MIG'

message1_binary = ''.join(format(ord(i), '08b') for i in message1)
key_binary = ''.join(format(ord(i), '08b') for i in key)

message2_binary = bin(int(message1_binary,2)^int(key_binary,2))[2:].zfill(len(message1_binary))

print(f'{message2_binary=}')

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

message2_textform = decode_binary_string(message2_binary)
print(f'{message2_textform=}')