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
