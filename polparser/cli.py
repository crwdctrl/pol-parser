import sys
from .parser import parse_pol

def main():
    if len(sys.argv) != 2:
        print("Usage: pol_parser <Registry.pol>")
        return
    filename = sys.argv[1]
    with open(filename, 'rb') as f:
        data = f.read()
    try:
        results = parse_pol(data)
        print(f"Parsed {len(results)} entries")
    except Exception as e:
        print(f"Error: {e}")
        return

    print(f"{'Key':<60} {'Value Name':<30} {'Type':<12} {'Value'}")
    print("=" * 120)
    for key, name, typ, value in results:
        print(f"{key:<60} {name:<30} {typ:<12} {value}")

if __name__ == '__main__':
    main()
