
import argparse
from pdf_utils import extract_text_from_pdf

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf-file", required=True)
    ap.add_argument("--out", default="extracted.txt")
    args = ap.parse_args()
    text = extract_text_from_pdf(args.pdf_file)
    with open(args.out, "w") as f:
        f.write(text)
    print(f"Wrote extracted text to {args.out}")
