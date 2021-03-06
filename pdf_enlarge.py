"""
PDF Enlarge
===========

Scale the contents of a PDF document 2x.

- Split each page into two parts along the perpendicular axis (e.g. one
  A4 page into two A5 pages).
- Scale each split part 2 times (e.g. A5 -> A4)
- Merge scaled parts into a new PDF document.
"""

import sys


def main() -> int:
    """Console script entry point function."""
    print('PDF Enlarge')
    return 0


if __name__ == '__main__':
    sys.exit(main())
