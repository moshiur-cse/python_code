import pandas as pd

path ='E:/MS/Python/'

emp=pd.read_excel( path + 'Employee.xlsx', sheet_name='Emp')

pin=pd.read_excel( path + 'Employee.xlsx', sheet_name='PIN')

division=pd.read_excel( path + 'Employee.xlsx', sheet_name='Division')

empType=pd.read_excel( path + 'Employee.xlsx', sheet_name='EmpType')


data=pd.merge(emp,pin,on='Initial',how='left')

def setPin():
  return data['Initial']+'999'

datas1=data.fillna({
    'PIN': setPin(),
    'Level':'Empty'
    })

# datas1.loc[(datas1['Staff type'] == empType['Type'])] = empType['Id']


def UpdateEmpType():
    return 'aaa'


data3=pd.merge(datas1,empType,on='Staff type',how='left')


#way to chage columns values
data3['Staff type'] = data3['Staff type'].map(empType.set_index('Staff type')['Id'])



# print(data3)

finalData=pd.DataFrame(data3)

finalData.rename(columns={"Id": "Staff_type_Id"},inplace=True)

finalData.drop(columns=['Staff type'], axis=1,inplace=True)



#print("Count",datas1.count())

# print("emp",emp.count())
# data3=pd.DataFrame(columns=data3.columns)

EmpDivision =[]

for data in finalData.iterrows():
   
    for d in division.iterrows():       
        if d[1][2].strip()==data[1][3].strip():           
            EmpDivision.append(d[1][0])
            # print(d[1][0])
            break
    
finalData['Division']=EmpDivision


finalData.to_excel(path + 'NewEmpList.xlsx', sheet_name='emp',index=0)