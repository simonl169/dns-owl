import json
import argparse
import os


def get_current_version(file: str = "package.json") -> tuple[str, str, str]:
    """
    This reads a json file and return the current version from the field 'version'

    :param file: input a json file which has the key 'data'
    :return: returns major, minor and patch version as a tuple of strings
    """
    # print(f'Reading current version from file {file}')
    with open(file, 'r') as f:
        data = json.load(f)
    major, minor, patch = data['version'].split(".")

    return major, minor, patch


def print_current_version(major: str, minor: str, patch: str) -> None:
    print(f"Current Version: {major}.{minor}.{patch}")


def print_next_version(major: str, minor: str, patch: str) -> None:
    print(f"Next Version: {major}.{minor}.{patch}")


def parse_version_bump():
    parser = argparse.ArgumentParser(description="Script that adds 3 numbers from CMD")
    parser.add_argument("--server", "-s", required=False, type=str)
    args = parser.parse_args()

    if args.server == "major":
        return "major"
    elif args.server == "minor":
        return "minor"
    elif args.server == "patch":
        return "patch"
    elif args.server == "False":
        return "None"
    else:
        return "None"


def bump_version(current_major: str, current_minor: str, current_patch: str, bump: str) -> tuple[str, str, str]:
    next_major = current_major
    next_minor = current_minor
    next_patch = current_patch
    if bump == "major":
        next_major = str(int(next_major) + 1)
    elif bump == "minor":
        next_minor = str(int(next_minor) + 1)
    elif bump == "patch":
        next_patch = str(int(next_patch) + 1)
    elif bump == "False":
        pass

    return next_major, next_minor, next_patch


def update_json_file(next_major: str, next_minor: str, next_patch: str, file: str = "package.json"):
    with open(file, 'r') as f:
        data = json.load(f)
        f.close()
    data['version'] = f"{next_major}.{next_minor}.{next_patch}"
    with open(file, 'w') as f:
        json_object = json.dumps(data, indent=4)
        f.write(json_object)
        f.close()
    print("Updated Version")


if __name__ == "__main__":

    major, minor, patch = get_current_version()
    print_current_version(major, minor, patch)
    bump = parse_version_bump()
    next_major, next_minor, next_patch = bump_version(major, minor, patch, bump)
    print_next_version(next_major, next_minor, next_patch)
    update_json_file(next_major, next_minor, next_patch)

    if os.getenv("GITHUB_ACTIONS") == "true":
        import os

        env_file = os.getenv('GITHUB_ENV')

        with open(env_file, "a") as myfile:
            myfile.write(f"NEXT_SERVER={next_major}.{next_minor}.{next_patch}")