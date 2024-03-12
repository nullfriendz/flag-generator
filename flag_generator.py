import secrets
import string

def generate_flags(ctf_chall: str, chall_title: str, gen_str_len: int) -> str:
	gen_str = "".join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(gen_str_len))
	flags = ctf_chall + "{" + chall_title + "__" + gen_str + "}"
	return "\n-> Here's your flag: " + flags + "\n"

def banner() -> str:
	return """
	FLAG{ GENERATOR } by. nullfriendz
	"""

def main() -> str:
    print(banner())

    ctf_chall = input("Your CTF challenge: ")
    chall_title = input("Challenge title: ")
    
    if (not ctf_chall) or (not chall_title):
        raise ValueError("\n-> You've to provide strings (not empty)!\n")
    
    gen_str_len = input("Generated string length: ")
    if (not isinstance(gen_str_len, int)) or (gen_str_len <= 0) or (isinstance(gen_str_len, float)):
        raise ValueError("\n-> The length must be a positive number\n")
    
    return generate_flags(ctf_chall, chall_title, int(gen_str_len))
    
if __name__ == "__main__":
    try:
        print(main())
    except Exception as err:
        print(err)