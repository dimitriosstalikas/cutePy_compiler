def main_sum():
#{
#$ test #$
	#declare x, sum

	x = int(input());
	sum = 0;

	while (x > 0):
	#{
		sum = sum + x;
		x = x - 1;
	#}

	print(sum);
#}

if __name__ == "__main__":
	main_sum();