from password_generator import PasswordGenerator
def random_pass_gerator():
    pwo = PasswordGenerator()
    print(pwo.generate())


if __name__ == "__main__":
    random_pass_gerator()