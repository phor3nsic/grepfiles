import re
import sys

file = sys.stdin

expressions = {
	"PDF":".*\\.pdf$",
	"JSON":".*\\.json$",
	"DOC":".*\\.(doc|docx|docm|dot|dotm|dotx|odt)$",
	"XLS":".*\\.(xls|xlsx|xlsm|xlsb|xltx|xltm|xltm|xlt)$",
	"CSV":".*\\.csv$",
	"DB":".*\\.db$",
	"SQL":".*\\.sql$"
}

def check(line):
	for exp in expressions:
		res = re.search(expressions[exp],line)
		if res:
			print(f"[{exp}] [info] {res.group(0)}")

def main():
	for x in file:
		check(x)


if __name__ == '__main__':
	main()