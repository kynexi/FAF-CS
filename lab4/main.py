import random
import string

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

def print_table(name, table, cols):
    print(f"\nTable {name}:")

    for i in range(0, len(table), cols):
        row = table[i:i + cols]
        print("  ".join(f"{x:2}" for x in row))

def text_to_bits(text):
    bits = ""
    print("\nStep 1. Convert each character to 8 bits (ASCII):")
    for ch in text:
        b = format(ord(ch), "08b")
        print(f"  '{ch}' -> ASCII {ord(ch):3} -> {b}")
        bits += b
    return bits


def group_bits(bits, size=8):
    return " ".join(bits[i:i + size] for i in range(0, len(bits), size))

def permute(bits, table):
    result = ""
    for pos in table:
        result += bits[pos - 1]
    return result

def get_message():
    choice = input("1 - enter message, 2 - random message: ")
    if choice == "2":
        letters = string.ascii_letters + string.digits
        msg = "".join(random.choice(letters) for _ in range(8))
        print("Generated message:", msg)
        return msg

    msg = input("Enter message (8 characters): ")
    while len(msg) != 8:
        msg = input("Message must have exactly 8 characters, try again: ")
    return msg

def main():
    print("Lab 4 - DES; " \
    "task 2.4: find L1 from the message")
    msg = get_message()

    m_bits = text_to_bits(msg)
    print("\nM  =", group_bits(m_bits))
    print("M (hex) =", format(int(m_bits, 2), "016X"))

    print_table("IP", IP, 8)
    ip_bits = permute(m_bits, IP)
    print("\nStep 2. Apply initial permutation IP:")
    print("IP(M) =", group_bits(ip_bits))

    l0 = ip_bits[:32]
    r0 = ip_bits[32:]
    print("\nStep 3. Split IP(M) into two halves:")
    print("L0 =", group_bits(l0, 4))
    print("R0 =", group_bits(r0, 4))

    l1 = r0
    print("\nStep 4. By the DES round formula L1 = R0:")
    print("L1 =", group_bits(l1, 4))
    print("L1 (hex) =", format(int(l1, 2), "08X"))


if __name__ == "__main__":
    main()