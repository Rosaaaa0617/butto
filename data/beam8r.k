$
$ANSA_VERSION;23.0.1;
$
$
$ file created by  A N S A  Thu Jan 18 14:11:52 2024
$
$ output from :
$
$ d:/Users/ADMIN/Desktop/nogui/ansa/2dmesh/beam8.k
$
$ Settings :
$
$ Output format : R11
$
$ Output : All
$
$
$
$
*KEYWORD
*TITLE
LS-DYNA keyword deck by LS-PrePost                                              
*NODE
       1              0.              0.              0.       0       0
       2            512.              0.              0.       0       0
*ELEMENT_BEAM
       1       1       1       2                                               2
*PART
Beam1
         1         1        70                             0                    
*SECTION_BEAM_TITLE
Beam1
         1         8        1.         2        0.                  0.
        5.        5.        5.        0.
*BOUNDARY_SPC_SET_ID
         1                                                                      
         1                   1         1         1         1         1         1
*MAT_RIGID_TITLE
beam
        70     8.E-9  2000000.       0.3        0.        0.        0.          
       0.0        0.        0.
        0.        0.        0.        0.        0.        0.
*SET_NODE_TITLE
beam-end
         1                                                  
         1         2
$ANSA_COLOR;1;SECTION_BEAM_ELFORM_8;.952941179275513;.874509811401367;.105882354
$080677;1.;
$ANSA_COLOR;1;MAT20 MAT_RIGID;0.5686274766922;.407843142747879;0.5686274766922;1
$.;
$ANSA_PART;GROUP;ID;1;NAME;beam8.k;BELONGS_HERE;YES;PID_OFFSET;0;COLOR;201;236;1
$18;0;IS_COLOR_ACTIVE;-1;PART_TYPE;Undefined;ATTRIBUTES;1;DM/File Type;ANSA;CONT
$AINS;ANSAPART;3;
$ANSA_PART;PART;ID;3;NAME;BARs;BELONGS_HERE;YES;STUDY_VERSION;0;PID_OFFSET;0;COL
$OR;206;168;77;0;IS_COLOR_ACTIVE;-1;PART_TYPE;Undefined;ATTRIBUTES;1;DM/File Typ
$e;ANSA;CONTAINS;SECTION_BEAM_ELFORM_8;1;
*END
