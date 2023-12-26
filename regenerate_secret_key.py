from django.core.management.utils import get_random_secret_key
import os


def main():
    secret_key = get_random_secret_key()
    path = os.path.join(os.getcwd(), ".env.web")
    print(f'Writing new secret key to {path}')
    with open(path) as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        if line.startswith("SECRET_KEY"):
            lines[index] = f"SECRET_KEY = '{secret_key}'\n"
            break
    with open(path, "w") as file:
        file.writelines(lines)


if __name__ == '__main__':
    main()
