import re

def greeting():
  print(f"Hello, world! I'm retrobit.io! Hope you're ready for me!")

def dummy(filename="retrobit.ifc"):
  """ 
    Create a random dummy IFC file
  
    Args:
    filename (string): Name of the IFC file.
    schema (string): IFC schema version

    Output:
    Valid IFC filex
  """
  file_contents = "ISO-10303-21;\n"
  file_contents = file_contents + "HEADER;\n"
  file_contents = file_contents + "FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');\n"
  file_contents = file_contents + "FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');\n"
  file_contents = file_contents + f"FILE_NAME('{filename}','2024-10-19T00:04:30',(''),(''),'Retrobit.io IFC Writer','20100326_1700','');\n"
  file_contents = file_contents + "FILE_SCHEMA(('IFC2X3'));\n"
  file_contents = file_contents + "ENDSEC;\n"
  file_contents = file_contents + "DATA;\n"
  file_contents = file_contents + "#1=IFCORGANIZATION($,'Retrobit.io',$,$,$);\n"
  file_contents = file_contents + "#2=IFCAPPLICATION(#1,'2024','Retrobit.io IFC Writer','Retrobit.io');\n"
  file_contents = file_contents + "#4=IFCCARTESIANPOINT((0.,0.));\n"
  file_contents = file_contents + "#5=IFCDIRECTION((1.,0.,0.));\n"
  file_contents = file_contents + "#10=IFCDIRECTION((0.,0.,-1.));\n"
  file_contents = file_contents + "#11=IFCDIRECTION((1.,0.));\n"
  file_contents = file_contents + "#12=IFCDIRECTION((-1.,0.));\n"
  file_contents = file_contents + "#13=IFCDIRECTION((0.,1.));\n"
  file_contents = file_contents + "#14=IFCDIRECTION((0.,-1.));\n"

  with open(filename, 'w') as file:
    file.write(file_contents)

def unique_elements(filename="retrobit.ifc"):
  element_list = []

  with open(f"./{filename}") as fp:
    lines = fp.readlines()
    search_ifc = re.compile(r"IFC(.*?)(?=\()")
    ifc_types = []
    for line in lines:
        result = search_ifc.search(line)
        if result:
            if result.group(0) not in element_list:
               element_list.append(result.group(0))
  
  element_list.sort()
  return element_list
