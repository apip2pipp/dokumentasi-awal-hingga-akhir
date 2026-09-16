from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
FINAL_NAME = "Progress_AuditChain_Gateway_September_2026_Lengkap_Update.pdf"


def run_xelatex() -> None:
    command = [
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory=output",
        "main.tex",
    ]
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    OUTPUT.mkdir(exist_ok=True)

    try:
        run_xelatex()
        run_xelatex()
    except FileNotFoundError:
        print("xelatex tidak ditemukan. Install MiKTeX/TeX Live atau jalankan dari terminal yang mengenali xelatex.")
        return 1
    except subprocess.CalledProcessError:
        print("Build gagal. Cek output/main.log untuk detail error.")
        return 1

    source = OUTPUT / "main.pdf"
    target = OUTPUT / FINAL_NAME
    shutil.copyfile(source, target)
    print(f"Build selesai: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
