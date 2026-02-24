def main_error():
#{
#$ syntax error test: missing ';' #$
	#declare x
	x = 5
	print(x);
#}

if __name__ == "__main__":
	main_error();