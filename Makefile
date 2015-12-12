EFILE		= StairJS.exe
RM			= del
GCC			= gcc
SRC_DIR		= src
INCLUDE_DIR	= include
BIN_DIR		= bin

$(EFILE): $(BIN_DIR)/StairJS.o $(BIN_DIR)/StAST.o $(BIN_DIR)/StDict.o \
	$(BIN_DIR)/StEngine.o $(BIN_DIR)/StCal.o $(BIN_DIR)/StObject.o 
	$(GCC) -o $(EFILE) \
		$(BIN_DIR)/StairJS.o $(BIN_DIR)/StAST.o $(BIN_DIR)/StDict.o \
		$(BIN_DIR)/StEngine.o $(BIN_DIR)/StCal.o $(BIN_DIR)/StObject.o
		
$(BIN_DIR)/StairJS.o: $(INCLUDE_DIR)/StairJS.h $(SRC_DIR)/StairJS.c
	$(GCC) -c -o $(BIN_DIR)/StairJS.o $(SRC_DIR)/StairJS.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StAST.o: $(INCLUDE_DIR)/StAST.h $(SRC_DIR)/StAST.c
	$(GCC) -c -o $(BIN_DIR)/StAST.o $(SRC_DIR)/StAST.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StDict.o: $(INCLUDE_DIR)/StDict.h $(SRC_DIR)/StDict.c \
	$(INCLUDE_DIR)/StObject.h
	$(GCC) -c -o $(BIN_DIR)/StDict.o $(SRC_DIR)/StDict.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StEngine.o: $(INCLUDE_DIR)/StEngine.h $(SRC_DIR)/StEngine.c \
	$(INCLUDE_DIR)/StObject.h \
	$(INCLUDE_DIR)/StCal.h \
	$(INCLUDE_DIR)/StDict.h
	$(GCC) -c -o $(BIN_DIR)/StEngine.o $(SRC_DIR)/StEngine.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StParser.o: $(INCLUDE_DIR)/StParser.h $(SRC_DIR)/StParser.c
	$(GCC) -c -o $(BIN_DIR)/StParser.o $(SRC_DIR)/StParser.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StCal.o: $(INCLUDE_DIR)/StCal.h $(SRC_DIR)/StCal.c
	$(GCC) -c -o $(BIN_DIR)/StCal.o $(SRC_DIR)/StCal.c -I$(INCLUDE_DIR)
	
$(BIN_DIR)/StObject.o: $(INCLUDE_DIR)/StObject.h $(SRC_DIR)/StObject.c	
	$(GCC) -c -o $(BIN_DIR)/StObject.o $(SRC_DIR)/StObject.c -I$(INCLUDE_DIR)

.PHONY: clean
clean:
	$(RM) $(BIN_DIR)\*.o $(EFILE)
