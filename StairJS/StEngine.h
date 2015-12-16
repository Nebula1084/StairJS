#ifndef _ST_ENGINE_
#define _ST_ENGINE_

#include "StObject.h"
#include "StCal.h"
#include "StDict.h"

void StEgAsgExp(char* name, StObject* object);
void StEgAddExp();
void StEgSubExp();
void StEgFucExp();

void StEgDefStmt(char* name);
void StEgForStmt();
void StEgIfStmt();
void StEgWhlStmt();

#endif