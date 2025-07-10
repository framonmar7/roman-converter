import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Roman number converter CLI")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--decimal", type=int, help="Convert decimal to Roman number")
    group.add_argument("-r", "--roman", type=str, help="Convert Roman number to decimal")

    return parser.parse_args()
