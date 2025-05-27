REG_TYPES = {
    0x0001: 'REG_SZ',
    0x0002: 'REG_EXPAND_SZ',
    0x0003: 'REG_BINARY',
    0x0004: 'REG_DWORD',
    0x0007: 'REG_MULTI_SZ',
}

def read_unicode_string(data, offset):
    end = offset
    while end + 1 < len(data) and data[end:end+2] != b'\x00\x00':
        end += 2
    try:
        string = data[offset:end].decode('utf-16le')
    except:
        string = "<undecodable>"
    return string, end + 2
