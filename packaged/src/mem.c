/* -*- coding: utf-8 -*-
 ###############################################################################
 # Author: Pierre Vigneras <pierre.vigneras@bull.net>
 # Created on: May 24, 2013
 # Contributors:
 ###############################################################################
 # Copyright (C) 2013  Bull S. A. S.  -  All rights reserved
 # Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois
 # This is not Free or Open Source software.
 # Please contact Bull S. A. S. for details about its license.
 ###############################################################################
 */

#include <stdlib.h>
#include <assert.h>

#include "bxi/base/mem.h"

// *********************************************************************************
// ********************************** Defines **************************************
// *********************************************************************************


// *********************************************************************************
// ********************************** Types ****************************************
// *********************************************************************************

// *********************************************************************************
// **************************** Static function declaration ************************
// *********************************************************************************

// *********************************************************************************
// ********************************** Global Variables *****************************
// *********************************************************************************

// *********************************************************************************
// ********************************** Implementation   *****************************
// *********************************************************************************

void * bximem_calloc(const size_t n) {
    void * ptr = calloc(1, n);
    assert(ptr != NULL || n == 0);
    return(ptr);
}

/*
 * New realloc
 */
void * bximem_realloc(void* ptr, const size_t n) {
    void * new_ptr = realloc(ptr, n);
    assert(new_ptr != NULL || n == 0);
    return new_ptr;
}


void bximem_destroy(char ** pointer) {

    // Freeing a NULL pointer is allowed and does nothing.
    // Therefore, it is not required to check for *pointer.

    // So *DO NOT* UNCOMMENT THE FOLLOWING LINE UNLESS YOU HAVE GOOD REASONS!! ;-)
    //    if (pointer == NULL || *pointer == NULL) return;

    if (pointer == NULL) return;
    free(*pointer); // Allowed!
    *pointer = NULL;
}

// *********************************************************************************
// ********************************** Static Functions  ****************************
// *********************************************************************************

