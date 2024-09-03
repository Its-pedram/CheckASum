#    ______            __________              __   _____
#   / ____/___  ____  / / ____/ /_  ___  _____/ /__/ ___/__  ______ ___  _____
#  / /   / __ \/ __ \/ / /   / __ \/ _ \/ ___/ //_/\__ \/ / / / __ `__ \/ ___/
# / /___/ /_/ / /_/ / / /___/ / / /  __/ /__/ ,<  ___/ / /_/ / / / / / (__  )
# \____/\____/\____/_/\____/_/ /_/\___/\___/_/|_|/____/\__,_/_/ /_/ /_/____/

#                              Its-Pedram - 2024
#                             https://pedram.tech

import argparse, checksum, config, os, json


def print_separator():
    try:
        columns, _ = os.get_terminal_size(0)
    except OSError:
        columns = 76

    columns = min(columns, 76)

    print("-" * columns)


def clean_print(alg, checksum):
    longest_hash = max(len(alg) for alg in config.ALGORITHMS)
    diff = longest_hash - len(alg)
    print(f"{alg}{' ' * diff}: {checksum}")


def print_compare_result(result, machine_readable=False):
    if machine_readable:
        print(result)
        return
    if result:
        print("[!] Checksums Match!")
    else:
        print("[!] Checksums Do Not Match!")


def get_size(file_path):
    size = os.path.getsize(file_path)
    units = ["bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return size, units[unit_index]


def print_file_info(file_path):
    print(f"File Name: {file_path}")
    size, unit = get_size(file_path)
    print(f"File Size: {size:.2f} {unit}")
    print_separator()


def print_logo():
    print(
        f"""
   ______            __________              __   _____                     
  / ____/___  ____  / / ____/ /_  ___  _____/ /__/ ___/__  ______ ___  _____
 / /   / __ \/ __ \/ / /   / __ \/ _ \/ ___/ //_/\__ \/ / / / __ `__ \/ ___/
/ /___/ /_/ / /_/ / / /___/ / / /  __/ /__/ ,<  ___/ / /_/ / / / / / (__  ) 
\____/\____/\____/_/\____/_/ /_/\___/\___/_/|_|/____/\__,_/_/ /_/ /_/____/       

                               Its-Pedram - 2024
                              https://pedram.tech
                                    v{config.CCS_VERSION}"""
    )
    print_separator()


def handle_args():
    parser = argparse.ArgumentParser(
        prog="CoolCheckSums",
        description="CoolCheckSums - A Dead Simple Checksum Tool",
        exit_on_error=True,
        epilog="""If you do not choose an algorithm, CCS will attempt to "guess" it for you.""",
        usage="ccs <file_path> [checksum] [-a <algorithm>] (Use -h for more detailed help)",
    )
    parser.add_argument(
        "file_path", type=str, help="path to the file you want to check the checksum of"
    )
    parser.add_argument(
        "checksum",
        type=str,
        nargs="?",
        help="checksum to compare",
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        help="algorithm to use",
        choices=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"],
        required=False,
    )
    parser.add_argument(
        "-m",
        "--machine-readable",
        action="store_true",
        help="output in a machine-readable format",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {config.CCS_VERSION}",
    )
    return parser.parse_args()


def main():
    args = handle_args()
    config.load()

    if not args.machine_readable:
        print_logo()
        print_file_info(args.file_path)

    if args.checksum is not None and args.algorithm is not None:
        result = checksum.compare(args.file_path, args.checksum, args.algorithm)
        print_compare_result(result, args.machine_readable)
    elif args.checksum is not None:
        result = checksum.compare(args.file_path, args.checksum)
        print_compare_result(result, args.machine_readable)
    elif args.checksum is None and args.algorithm is not None:
        checksum_result = checksum.compute(args.file_path, args.algorithm)
        print(checksum_result)
    elif args.checksum is None:
        if not args.machine_readable:
            print("[!] Computing Checksums...", end="", flush=True)
            checksums = checksum.compute_all(args.file_path)
            print("\r", end="", flush=True)
            for alg, sum in checksums.items():
                clean_print(alg.upper(), sum)
        else:
            checksums = checksum.compute_all(args.file_path)
            print(json.dumps(checksums))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
