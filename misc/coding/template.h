/* -*- coding: utf-8 -*-
 ########################################################################################
 # Author: First Last <first.last@bull.net>
 # Created on: YYYY/MM/DD
 # Contributors:
 ########################################################################################
 # Copyright (C) YYYY  Bull S. A. S.  -  All rights reserved
 # Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois
 # This is not Free or Open Source software.
 # Please contact Bull S. A. S. for details about its license.
 ########################################################################################
 */


/****************************************************************************************
 * Quickly, as a title, present the API of this component
 ***************************************************************************************/


#ifndef TEMPLATE_H_
#define TEMPLATE_H_


/****************************************************************************************
 * *********************************  HOWTO USE  ****************************************
 *
 * To be defined ...
 *
 * **************************************************************************************
 ***************************************************************************************/


//***************************************************************************************
//***********************************  Includes  ****************************************
//***************************************************************************************

// => only the necessary includes! => compatibility with CFFI


//***************************************************************************************
//***********************************  Defines  *****************************************
//***************************************************************************************


//***************************************************************************************
//************************************  Types  ******************************************
//***************************************************************************************

typedef struct something_s * something_p; // We almost always use pointers 
					  // on abstract data type -> do not expose
					  // the content of the struct unless it is 
					  // required.

typedef struct {} other_s;		  // If you need so, do it like this.


//***************************************************************************************
//********************************  Global Variables  ***********************************
//***************************************************************************************


//***************************************************************************************
//***********************************  Interface  ***************************************
//***************************************************************************************

// * What is the purpose of this function? 
int fct();

#endif /* TEMPLATE_H_ */
