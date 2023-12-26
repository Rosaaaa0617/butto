import os
import ansa
from ansa import utils
from ansa import base
from ansa import session 
from ansa import constants
from ansa import batchmesh


def OpenCADFixGeoBatchMesh(file_path, distance):
    '''
    Name: OpenCADFixGeoBatchMesh
    Description: Opens CAD file, fixes geometry errors, runs batch mesh, exports statistics report and saves it as ANSA file.
    '''
    sel_file = [file_path]
    print("Reading file:", sel_file[0])
    
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
    base.Open(sel_file[0])
    location_directory = os.path.split(sel_file[0])
    directory = location_directory[0]
    
    Extrude(distance)

    session,parameters,criteria = _CheckParamsAndCriteriaFiles(directory)
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
    _SaveANSAFile(location_directory, directory)
    print("\nProcess completed.\n")


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
    

def _CheckParamsAndCriteriaFiles(directory):    
    session = batchmesh.GetNewSession()
    parameters = batchmesh.ReadSessionMeshParams(session, directory+os.sep+'sample_parameters.ansa_mpar')
    if parameters == 1:
        print("Reading Mesh Parameters...\n")
    criteria = batchmesh.ReadSessionQualityCriteria(session, directory+os.sep+'sample_quality.ansa_qual')
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


def _SaveANSAFile(location_directory, directory):
    filename = location_directory[1]
    if filename.endswith(".3dm"):
        filename = filename[:-4]  # 移除最后四个字符（即“.3dm”）
    output_ansa_file = directory + os.sep + filename + "_meshed.key"
    print("Saving file:", output_ansa_file)
    base.OutputLSDyna(filename=output_ansa_file)


def Extrude(distance):
    sel_entities = []
    dir_entities = []
    for i in range(1, 100):
        entity = base.GetEntity(ansa.base.CurrentDeck(), 'CURVE', i)
        if not entity:
            break
        sel_entities.append(entity)
    point1 = [0, 0, 0.]
    point2 = [0, 0, 2000.]
    base.SurfaceExtrudeExtrude(select_entities=sel_entities, dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2, distance=distance)
    props = base.CollectEntities(constants.LSDYNA, None, "SECTION_SHELL", False)
    base.AutoCalculateOrientation(props, True)


def GenerateImage(file_path):
    base.SetViewAngles(rot_x=0., rot_y=22.5, rot_z= -180.)
    base.SetViewAngles(f_key="F10")
    directory = os.path.dirname(file_path)
    abs_filename_1 = os.path.join(directory, 'image1.png')
    utils.SnapShot(abs_filename_1, image_format='PNG', transparent=True)

# 定义要处理的文件夹路径
file_path = r"d:\Users\ADMIN\Desktop\ansa-nogui\ansa-extrude-mesh\curve-processed.stp"
distance = 2000

OpenCADFixGeoBatchMesh(file_path, 2000)
GenerateImage(file_path)

