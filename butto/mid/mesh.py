import os, ansa
from ansa import base,constants,batchmesh,session
   
# directory=save, input_dir=batchmesh filepath
def FixGeoBatchMesh(directory,input_dir,mpar,qual):
    '''
    Name: OpenCADFixGeoBatchMesh
    Description: Opens CAD file, fixes geometry errors, runs batch mesh, exports statistics report and saves it as ANSA file.
    '''
    
    base.SetANSAdefaultsValues({
        # ANSA Tolerances
        "tolerance_mode":"fine",        #fine tolerances
        "ntolerance":"0.0125",          #|
        "ctolerance":"0.05",            #|
        
        # ANSA Resolution
        "curv_resol":"4.",              #Resolution of curves
        "perimeter_length":"4.",        #Resolution of CONS
        
        # Translators' Tolerances
        "TRANSL_TOLERANCE_MODE":"fine",        #fine tolerances
        "TRANSL_NTOLERANCE":"0.0125",          #|
        "TRANSL_CTOLERANCE":"0.05",            #|
        
        # Translators' Resolution
        "TRANSL_CURVES_RESOLUTION":"4.",
        "TRANSL_PERIMETER_LENGTH":"4.",
        # Edit translation options according to client's needs
        "TRANSLATORS_FLATTEN_ASSEMBLIES":"true",
        "TRANSLATORS_PREVIEW":"false",
        "TRANSLATORS_SINGLE_PART":"false",
        "TRANSLATORS_FEATURE_MODE":"true",
        "TRANSLATORS_READ_NOSHOW":"false",
        "TRANSLATORS_LAYER_VIS":"false",
        "TRANSLATORS_INCLUDE_LAYERS":"false",
        "TRANSLATORS_EXCLUDE_LAYERS":"false",
        "TRANSLATORS_READ_FREE_GEOMETRY":"true",
        "TRANSLATORS_READ_ATTRIBUTES":"true",
        "TRANSLATORS_READ_ANNOTATIONS":"true",
        "TRANSLATORS_GENERATE_3D_CURVES":"false",
        "READ_CONSTRUCTION_SURFACES":"false",
        "TRANSLATORS_ANSACOLOR":"false",
        "TRANSLATORS_PART2PID":"false",
        "TRANSLATORS_LAYER2PID":"false",
        "TRANSLATORS_COLOR2PID":"false",
        "TRANSLATORS_SINGLEPID":"false",
        "TRANSLATORS_CREATE_VOLUMES":"false",
        "TRANSLATORS_CREATE_SETS":"false",
        "TRANSLATORS_ORIENT_VEC":"false",
        "TRANSLATORS_THICKNESS_LINES":"false",
        "TRANSLATORS_MATERIAL_VECTOR":"false",
        "TRANSLATORS_CADHEAL":"true",
        "PERFORM_TOPOLOGY":"false",
        "TOPO_BETWEEN_LAYERS":"false",
        "TOPO_BETWEEN_PARTS":"false",
        "GEOMETRY_CLEAN_UP":"false",
        "TRANSLATORS_WRITE_LOG":"true"
    })

    session,parameters,criteria = _CheckParamsAndCriteriaFiles(input_dir,mpar,qual)
    if parameters == 0:
        print("\nNo such file! sample_parameters.ansa_mpar file does not exist in the directory!\n")
        return
    if criteria == 0:
        print("\nNo such file! sample_quality.ansa_qual file does not exist in the directory!\n")
        return
    length_of_faces_list = _CheckAndFixGeometry()
    if length_of_faces_list == 0:
        print("\nNo faces have been detected in the file!\n")
        return
    session_status = _RunSession(session, directory)
    if session_status == 2 or session_status == -1:
        print("\nBatch mesh session has been halted!\n")
        return
    


def _CheckAndFixGeometry():
    all_faces = base.CollectEntities(constants.NASTRAN, None, "FACE")
    length_of_faces_list= len(all_faces)
    if length_of_faces_list>0:
        print("\nChecking and fixing possible geometry errors...\n")
        options = ["CRACKS", "TRIPLE CONS", "OVERLAPS", "NEEDLE FACES", "COLLAPSED CONS"]
        fix = [1, 1, 1, 1, 1]
        ret = base.CheckAndFixGeometry(all_faces, options, fix) #The automatic fix functionality may work better if Tolerances are set to 'fine' or 'extra fine'.
        if ret == None:
            print("Fixing geometry completed successfully.\n")
        else:
            print("Total remaining errors:", len(ret['failed']),"\n")
    
    return length_of_faces_list
    

def _CheckParamsAndCriteriaFiles(input_dir,mpar,qual):    
    session = batchmesh.GetNewSession()
    mpar_path=os.path.join(input_dir,f"{mpar}.ansa_mpar")
    parameters = batchmesh.ReadSessionMeshParams(session, mpar_path)
    if parameters == 1:
        print("Reading Mesh Parameters...\n")
    qual_path=os.path.join(input_dir,f"{qual}.ansa_qual")
    criteria = batchmesh.ReadSessionQualityCriteria(session, qual_path)
    if criteria == 1:
        print("Reading Quality Criteria...\n")
    
    return session,parameters,criteria


def _RunSession(session,directory):
    parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
    for part in parts:
        batchmesh.AddPartToSession(part, session)
    session_status = batchmesh.RunSession(session)
    if session_status == 1:
        print("Session has run.\n")
        ret_val = batchmesh.WriteStatistics(session, directory+os.sep+"statistics_report.html")
        if ret_val == 1:
            print("Quality violations and/or unmeshed macro(s) remain!")
            print("Report saved in "+directory+os.sep+"statistics_report.html.\n")
    elif session_status == 2:
        print("Session hasn't run!\n")
    
    return session_status




if __name__ == "__main__":
    # batchmesh file directory
    input_dir = r"E:\#code\butto\data"
    
    # output directory
    directory = r"E:\#code\butto\data\output"
    
    # input cross-section file
    
    FixGeoBatchMesh(directory,input_dir)
    
    
    