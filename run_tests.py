import os
import subprocess

COMPILER = "cutePy-compiler.py"
EXAMPLES_DIR = "examples"

passed = 0
total = 0


def run_file(filepath):
    global passed, total

    total += 1
    print(f"\n=== Running: {filepath} ===")

    result = subprocess.run(
        ["py", COMPILER, filepath],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("SUCCESS")
        passed += 1
    else:
        print("ERROR")

    print(result.stdout)
    print(result.stderr)


def run_all_examples():
    for root, _, files in os.walk(EXAMPLES_DIR):
        for file in files:
            if file.endswith(".cpy"):
                full_path = os.path.join(root, file)
                run_file(full_path)

    print("\n======================")
    print(f"Passed: {passed}/{total}")
    print("======================")


if __name__ == "__main__":
    run_all_examples()