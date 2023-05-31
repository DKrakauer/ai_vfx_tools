import sys
import re
from driver import generate_vfx

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_vfx.py <prompt>")
        return

    prompt = sys.argv[1]
    if not re.match(r'^[A-Za-z, ]+$', prompt):
        print("Invalid prompt. Please provide a string with only letters, spaces, and commas.")
        return

    generate_vfx(prompt)

if __name__ == '__main__':
    main()
