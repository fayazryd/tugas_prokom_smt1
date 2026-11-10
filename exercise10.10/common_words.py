from pathlib import Path

path = Path('sample.txt')
contents = path.read_text()

print(f"Kata 'the' muncul sekitar {contents.lower().count('the')} kali.")
print(f"Kata 'the ' (dengan spasi) muncul {contents.lower().count('the ')} kali.")
