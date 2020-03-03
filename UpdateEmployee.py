import pandas as pd

path ='D:/Employee/'
currentEmp=pd.read_excel( path + 'dbo_LookUpEmployees.xlsx', sheet_name='dbo_LookUpEmployees')
emp=pd.read_excel( path + 'Employee.xlsx', sheet_name='Emp') #, header= None
pin=pd.read_excel( path + 'Employee.xlsx', sheet_name='Pin')

div=pd.read_excel( path + 'Employee.xlsx', sheet_name='Division')
empType=pd.read_excel( path + 'Employee.xlsx', sheet_name='EmpType')

matchEmp = pd.merge(emp, pin, left_on='Initial', right_on='Initial')

print(matchEmp.columns)


#Get Column names

col=[]
for c in currentEmp.columns:
    #print(c,':',c)
    col.append(c)
    
newEmp=pd.DataFrame(columns=col)


EmpId =[]
SortingSerialNo =[]
EmpPinNo =[]
EmpTypeId =[]
EmpInitial =[]
EmpFullName =[]
EmpDivisionId =[]
EmpDesignation =[]
EmpLevel =[]
EmpEmail =[]
EmpMobile =[]
EmpRoomNo =[]
EmpPresentAddress =[]
EmpNid =[]
EmpPaasportNo =[]
EmpBloodGroup =[]
EmpHighestDegree =[]
EmpHighestDegreeMajorSubject =[]
EmpCareerSummary =[]
Signature =[]
count=1

for data in matchEmp.iterrows():
    EmpId.append(1)
    SortingSerialNo.append(1)
    EmpPinNo.append(data[1][7])
    
    for t in empType.iterrows():
        if t[1][2]==data[1][6]:
            EmpTypeId .append(t[1][0])
            break     
    #EmpTypeId .append(3)
    
    EmpInitial.append(data[1][0])
    EmpFullName.append(data[1][1])
    
    for d in div.iterrows():
        if d[1][2].strip()==data[1][3].strip():
            EmpDivisionId .append(d[1][0])
            break
#        else:
#            EmpDivisionId .append(0)
#            break
    
    EmpDesignation.append(data[1][4])
    EmpLevel.append(data[1][2])
    EmpEmail.append(data[1][0]+'@cegisbd.com')
    EmpMobile.append('Empty')
    EmpRoomNo.append(data[1][5])
    EmpPresentAddress.append('')
    EmpNid .append('')
    EmpPaasportNo.append('')
    EmpBloodGroup.append('')
    EmpHighestDegree.append('')
    EmpHighestDegreeMajorSubject .append('')
    EmpCareerSummary.append('')
    Signature.append('')
    count=count+1


df = pd.DataFrame({
        'EmpId' : EmpId,
        'SortingSerialNo' : SortingSerialNo,
        'EmpPinNo' : EmpPinNo,
        'EmpTypeId' : EmpTypeId,
        'EmpInitial' : EmpInitial,
        'EmpFullName' : EmpFullName,
        'EmpDivisionId' : EmpDivisionId,
        'EmpDesignation' : EmpDesignation,
        'EmpLevel' : EmpLevel,
        'EmpEmail' : EmpEmail,
        'EmpMobile' : EmpMobile,
        'EmpRoomNo' : EmpRoomNo,
        'EmpPresentAddress' : EmpPresentAddress,
        'EmpNid' : EmpNid,
        'EmpPaasportNo' : EmpPaasportNo,
        'EmpBloodGroup' : EmpBloodGroup,
        'EmpHighestDegree' : EmpHighestDegree,
        'EmpHighestDegreeMajorSubject' : EmpHighestDegreeMajorSubject,
        'EmpCareerSummary' : EmpCareerSummary,
        'Signature' : Signature                                      
                   })  
    
    
       
df.to_excel( path + 'NerEmpList.xlsx', sheet_name='emp',index=0)

print("Success")

#data.head()
#col=['id','name','divcode','billNo']
#
#db=pd.DataFrame(columns = col)
#
#index=[]
#name=[]
#divcode=[]
#billNo=[]
#
#
#
#for x in data.iterrows():
#    for xd in dataDiv.iterrows():
#        if xd[1][1]==x[1][2]:            
#           divcode.append(xd[1][0])
#    for bg in databillNo.iterrows():
#        if bg[1][1]==x[1][3]:            
#           billNo.append(bg[1][0])      
#       
#    index.append(x[1][0])    
#    name.append(x[1][1])    
#
#df = pd.DataFrame({'name': name,'id':index,'divcode':divcode,'billNo':billNo})  
#df.to_excel( path + 'cpt22.xlsx', sheet_name='rimu',index=0)