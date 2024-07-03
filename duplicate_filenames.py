import pandas as pd


def main():
    csvFile = pd.read_csv(r'test2.csv',usecols=['FileName'])
    df1 = pd.DataFrame(csvFile,columns=['FileName'])
    unique1 =  df1.FileName.unique()
    df2 = pd.DataFrame(unique1) 
    df3 = df1.loc[df1['FileName'].duplicated(),'FileName']
    
    #print(df2)
    count1 = df2.index.size
    count2 = df3.index.size

    print("total number of unique values",count1 )
    print("total number of Duplicate values" , count2)
    # print(df3) 

    df2.to_csv('test_out.csv',mode='a',index=False, header=['FileName'])

    csvFile1 = pd.read_csv(r'test_out.csv',usecols=['FileName'])
    df4 = pd.DataFrame(csvFile1,columns=['FileName'])
    unique1 =  df4.FileName.unique()
    df5 = pd.DataFrame(unique1) 
    df5.to_csv('final_output.csv', header=['FileName'])


    

if __name__ == "__main__":

    main()