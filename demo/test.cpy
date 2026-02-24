def main_j():
#{
#$ test #$
	#declare x,y
	
	x = int(input());
	
	if(x > 5):
	#{
		while(x >0):
		#{
			print(x);
			x = x - 1;
		#}
	#}	
		else:
		#{
			y = 10;
			while(x<y):
			#{	
				print(x);
				x = x + 1;
			#}
		#}
#}

if __name__ == "__main__":
	main_j();