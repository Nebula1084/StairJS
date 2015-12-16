#ifndef __ST_OBJECT__
#define __ST_OBJECT__

#include "StAST.h"

enum _StType_{
	FUNCPROTO, FUNCTION, OBJECT, INT, FLOAT, STRING
};

typedef enum _StType_ StType;

struct _StObject_;

typedef struct _StObject_ StObject;

struct _StObject_{
	StType type;
	char* name;
	void* fileds;
	char** arguments;
	StObject* this;
	StObject* outFunction;
};

#endif