DESTDIR ?= 
PREFIX ?= /usr/local

task:
	g++ task.cpp -o task

install: task
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 task $(DESTDIR)$(PREFIX)/bin
