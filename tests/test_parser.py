import pytest
from polparser.parser import parse_pol

def test_invalid_file():
    with pytest.raises(ValueError):
        parse_pol(b"NotAPRegFile")

def test_minimal_valid_pol():
    header = b'PReg'

    def utf16le(s):
        return s.encode('utf-16le') + b'\x00\x00'  # proper null-termination

    key = utf16le('Software\\Test')
    value_name = utf16le('ValueName')
    value_type_str = utf16le('REG_SZ')

    data_type = b'\x01\x00\x00\x00'  # REG_SZ
    value = 'Test123'.encode('utf-16le')
    data_len = len(value).to_bytes(4, 'little')

    data = header + key + value_name + value_type_str + data_type + data_len + value

    result = parse_pol(data)

    assert result[0][0] == 'Software\\Test'
    assert result[0][1] == 'ValueName'
    assert result[0][2] == 'REG_SZ'
    assert result[0][3] == 'Test123'
