# src/cli.py

from fact_checker import fact_check
import sys

if __name__ == "__main__":
    while True:
        query = input("Enter a claim or question (or 'quit' to exit): ")
        if query.lower() in ["quit", "exit"]:
            sys.exit()
        result = fact_check(query)
        print(result)






