#ifndef __ST_DICT__
#define __ST_DICT__

#include "StObject.h"

struct _StDict_;

typedef struct _StDict_ StDict;

struct _StDict_{
	
	int blank;
};

StDict* StDcGetObject(StDict* dict, char* name);

void StDcPutObject(StDict* dict, char* name);

#endif