#ifndef __STAST__
#define __STAST__

typedef struct StAstNodeBody
{
	char token[30];
	struct StAstNodeBody* child;
	struct StAstNodeBody* brother;
}*StAstNode, *StAst, StAstNodeBody;
void printAst(StAst ast, int indentation);
void freeAst(StAst* pStAst);

#endif