# Makefile

all: out

out: out.o
	ld out.o -o out

out.o: out.s
	as out.s -o out.o

clean:
	rm -f out.o out
