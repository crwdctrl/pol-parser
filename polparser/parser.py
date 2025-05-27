import struct
from .utils import read_unicode_string, REG_TYPES

def parse_pol(data):
    if not data.startswith(b'PReg'):
        raise ValueError("Invalid .pol file (missing PReg header)")

    output = []
    offset = 4
    while offset < len(data):
        if data[offset:offset+4] == b'\x00\x00\x00\x00':
            offset += 4
            continue
        try:
            key_name, offset = read_unicode_string(data, offset)
            value_name, offset = read_unicode_string(data, offset)
            value_type_str, offset = read_unicode_string(data, offset)

            data_type = struct.unpack('<L', data[offset:offset+4])[0]
            offset += 4

            data_size = struct.unpack('<L', data[offset:offset+4])[0]
            offset += 4

            value_data = data[offset:offset+data_size]
            offset += data_size

            if data_type == 0x0001 or data_type == 0x0002:
                value = value_data.decode('utf-16le', errors='replace').rstrip('\x00')
            elif data_type == 0x3003b:
                with open("efs_blob.bin", "wb") as out:
                    out.write(value_data)
                value = f"<EFS Blob exported: {len(value_data)} bytes>"
            elif data_type == 0x0004:
                value = str(struct.unpack('<L', value_data[:4])[0])
            elif data_type == 0x0003:
                value = value_data.hex()
            elif data_type == 0x0007:
                value = value_data.decode('utf-16le', errors='replace').replace('\x00', ', ')
            else:
                value = f"<Unknown type> ({value_data[:40].hex()}... len={len(value_data)} bytes)"

            reg_type = REG_TYPES.get(data_type, f"0x{data_type:04x}")
            output.append((key_name, value_name, reg_type, value))

        except Exception as e:
            raise RuntimeError(f"Parsing failed at offset {offset}: {e}")

    return output

