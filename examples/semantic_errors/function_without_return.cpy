def main_error():
#{
#$ semantic error test: function without return #$
	foo();
#}

def foo():
#{
	#declare x
	x = 5;
#}

if __name__ == "__main__":
	main_error();