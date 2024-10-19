
def greeting():
  print(f"Hello, world! I'm retrobit.io! Hope you're ready for me!")

def write_ifc(filename="retrobit.ifc"):
  print(f"ISO-10303-21;")
  print(f"HEADER;")
  print(f"FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');")
  print(f"FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');")
  print(f"FILE_NAME('{filename}','2024-10-19T00:04:30',(''),(''),'Retrobit.io IFC Writer','20100326_1700','');")
  print(f"FILE_SCHEMA(('IFC2X3'));")
  print(f"ENDSEC;")
  print(f"DATA;")
  print(f"#1=IFCORGANIZATION($,'Retrobit.io',$,$,$);")
  print(f"#2=IFCAPPLICATION(#1,'2024','Retrobit.io IFC Writer','Retrobit.io');")

#4=IFCCARTESIANPOINT((0.,0.));
#5=IFCDIRECTION((1.,0.,0.));
#10=IFCDIRECTION((0.,0.,-1.));
#11=IFCDIRECTION((1.,0.));
#12=IFCDIRECTION((-1.,0.));
#13=IFCDIRECTION((0.,1.));
#14=IFCDIRECTION((0.,-1.));
#15=IFCSIUNIT(*,.LENGTHUNIT.,$,.METRE.);
#16=IFCSIUNIT(*,.AREAUNIT.,$,.SQUARE_METRE.);
#17=IFCSIUNIT(*,.VOLUMEUNIT.,$,.CUBIC_METRE.);
#18=IFCSIUNIT(*,.PLANEANGLEUNIT.,$,.RADIAN.);
#19=IFCDIMENSIONALEXPONENTS(0,0,0,0,0,0,0);
#20=IFCMEASUREWITHUNIT(IFCRATIOMEASURE(0.01745329251994328),#18);
#21=IFCCONVERSIONBASEDUNIT(#19,.PLANEANGLEUNIT.,'DEGREE',#20);
#22=IFCSIUNIT(*,.TIMEUNIT.,$,.SECOND.);
#23=IFCUNITASSIGNMENT((#15,#16,#17,#21,#22));
#26=IFCAXIS2PLACEMENT3D(#3,$,$);
#27=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-009,#26,$);
#28=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Plan',3,1.E-009,#26,$);
#29=IFCGEOMETRICREPRESENTATIONSUBCONTEXT($,'Plan',*,*,*,*,#28,0.01,.PLAN_VIEW.,$);
#30=IFCPERSON($,$,'cskender',$,$,$,$,$);
#31=IFCORGANIZATION($,'','',$,$);
#32=IFCPERSONANDORGANIZATION(#30,#31,$);
#33=IFCOWNERHISTORY(#32,#2,$,.NOCHANGE.,$,$,$,0);
#35=IFCPOSTALADDRESS($,$,$,$,('Enter address here'),$,'Chicago','','','IL');