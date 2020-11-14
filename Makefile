EXECS=ExportForTracking
CC=gcc
all:${EXECS}

ExportGalaxies:ExportForTracking.c
	${CC} -o ExportForTracking ExportForTracking.c
	
Clean:
	rm -f ${EXECS}
