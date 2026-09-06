import argparse
import json
import logging

from .parser import parse_file
from .report import build_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze web access logs")
    parser.add_argument("input", help="path to the log file")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    try:
        report = build_report(parse_file(args.input))
    except (OSError, ValueError) as exc:
        logging.error("Could not analyze %s: %s", args.input, exc)
        return 1

    if args.format == "json":
        print(json.dumps(report, indent=2, default=str))
    else:
        for key, value in report.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
