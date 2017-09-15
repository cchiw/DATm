/*! \file init.c
 *
 * \author Charisee
 */

/*
 * This code is part of the Diderot Project (http://diderot-language.cs.uchicago.edu)
 *
 * COPYRIGHT (c) 2015 The University of Chicago
 * All rights reserved.
 */

#include <stdlib.h>
#include <stdio.h>
#include "ex1.h"

void fail (const char *msg, ex1_world_t *wrld)
{
    if ((wrld == 0) || !ex1_any_errors(wrld)) {
        fprintf(stderr, "Error: %s\n", msg);
    }
    else {
        fprintf(stderr, "Error: %s\n%s\n", msg, ex1_get_errors(wrld));
    }
    exit (1);
}

//struct Function;
struct Function {
  int Gdmin;
  int Sdmin;
  int NumCells;
  int ** CellToNode;
  int ** NodeToCoords;
  float ** NodeToPoint;
  float * Coords;
};

void callDiderot_ex1(char *Outfile, int type, void *valF, void *valG){
    
    ex1_world_t *wrld = ex1_new_world ();
    if (wrld == 0) {
        fail ("unable to create world",0);
    }
    
    if (ex1_init_world(wrld)){
        fail ("unable to init world",wrld);
    }
    
    if (ex1_input_set_FF0 (wrld, valF)) {
        fail ("unable to initialize imgRed", wrld);
    }
    if (ex1_input_set_FF1 (wrld, valG)) {
        fail ("unable to initialize imgRed", wrld);
    }
    
    if (ex1_create_strands (wrld)) {
        fail ("unable to create initial strands", wrld);
    }
    
    uint32_t nsteps = ex1_run (wrld, 0);
    if (nsteps == 0) {
        fail ("no steps taken", wrld);
    }
    
    Nrrd *nData = nrrdNew();
    if (nData == 0) {
        fail ("unable to allocate nrrd for output", 0);
    }
    if (ex1_output_get_out (wrld, nData)) {
        fail ("problem getting output", wrld);
    }
    if (nrrdSave(Outfile, nData, 0)) {
        char *err = biffGetDone(NRRD);
        fprintf (stderr, "Error: trouble writing output:\n%s", err);
        free (err);
        exit (1);
    }
    
    nrrdNuke (nData);
    ex1_shutdown (wrld);
    
}
