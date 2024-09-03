# CoolCheckSums

> A simple tool to generate and verify checksums for files.

## Index
| Topic | Go |
|--|--|
| About | [⬇️](#About) |
| Prerequisites/Dependencies | [⬇️](#PrerequisitesDependencies) |
| Installation | [⬇️](#Installation) |
| Usage and Examples | [⬇️](#Usage-and-Examples) |
| Configuration | [⬇️](#Configuration) |
| Roadmap | [⬇️](#Roadmap) |

## About

CoolCheckSums is a simple, cross-platform Python program designed to compute and compare checksums for files. It is designed to be easy to use and understand, and is intended to be used by anyone who needs to verify the integrity of files.

While there are ways to generate checksums on every platform, they are usually different and slow down the process of verifying the integrity of files. CCS shares one syntax across all platforms, and is designed to be as simple as possible.

## Prerequisites/Dependencies

- Written in `Python 3.10`, but should work with most versions of Python 3.
- All dependencies are included in the standard library.
- Any modern operating system with a Python interpreter should be able to run CCS.

## Installation

Currently, there is no way to install per se. You can clone the repository and directly run `ccs.py` with `python3` or `python` depending on your OS.

### Linux / macOS

To run CCS on Linux or macOS, you would have to use the following command:

```bash
python3 src/ccs.py
```

Obviously, this is inconvenient. In that case you have a few options:

#### Option 1: Alias

You can create an alias in your shell configuration file. For example, in `~/.bashrc` or `~/.zshrc`:

```bash
alias ccs="python3 /path/to/ccs.py"
```

#### Option 2: Add to PATH

You can add the directory containing CCS to your `PATH`. For example, in `~/.bashrc` or `~/.zshrc`:

If you choose this option, it's better if you created a bash script that runs CCS, and add the directory containing the bash script to your `PATH`.

You can find an (extremely simple) example bash script in `examples/ccs.sh`.

```bash
export PATH=$PATH:/path/to/ccs.sh
```

### Windows

To run CCS on Windows, you would have to use the following command:

```ps
python src\ccs.py
```

As with Linux and macOS, this is inconvenient. In that case you have a few options:

#### Option 1: Add to PATH

You can add the directory containing CCS to your `PATH`. For example, in `System Properties > Environment Variables`:

If you choose this option, it's better if you created a batch script that runs CCS, and add the directory containing the batch script to your `PATH`.

You can find an (extremely simple) example batch script in `examples\ccs.bat`.

---
Eventually, CCS will have native binaries for Windows, Linux, and macOS. For that release, I plan to streamline/automate the installation process.

## Usage and Examples

There are four main cases in which CCS can be used:

### Case 1: Generate checksum with every algorithm available

If you **don't** specify an algorithm with `-a` or `--algorithm`, CCS will generate checksums for the file using every algorithm available.

```bash
ccs <file_path>
```

### Case 2: Generate checksum with a specific algorithm

If you specify an algorithm with `-a` or `--algorithm`, CCS will generate a checksum for the file using that algorithm.

```bash
ccs <file_path> -a {md5,sha1,sha224,sha256,sha384,sha512}
```

### Case 3: Verify checksum with every algorithm available

If you don't specify an algorithm with `-a` or `--algorithm` to check with, CCS will verify the checksums for the file using every algorithm available (either by guessing or by brute force).

```bash
ccs <file_path> <checksum>
```

### Case 4: Verify checksum with a specific algorithm

If you specify an algorithm with `-a` or `--algorithm` to check with, CCS will verify the checksum for the file using that algorithm.

```bash
ccs <file_path> <checksum> -a {md5,sha1,sha224,sha256,sha384,sha512}
```

Aside from the main cases, there are a few other arguments that can be used:

- `-h` or `--help`: Display the help message.
- `-v` or `--version`: Display the version of CCS.
- `-m` or `--machine-readable`: Output the checksums/compare results in a machine-readable format. It disables the excess output, and displays the information in a format such as a boolean.

## Configuration

At the moment, there is not much to configure in CCS. However, I have implemented a configuration loader that can read a `config.json` file in the root directory of the repository.

An example `config.json` file is as follows:

```json
{
    "buffer_size": 65536
}
```

In the case that the `config.json` file is not found, the default values (`config.py`) will be used.

## Roadmap

Currently, the main goal is to release executables for Windows, Linux, and macOS.