import psutil
import pandas as pd

class conn:
    def connection(self):
        self.connect=psutil.net_connections(kind='tcp')
        return self.connect
    
    def append(self,conn,df):
        for c in conn:
            if c.laddr and c.raddr:
                data=pd.DataFrame({'pid':[c.pid],'laddr':[c.laddr],'raddr':[c.raddr],'status':[c.status]})
                df=df.append(data)
        return df
    
    def splitr(self,addr):
        for j in addr:
            i=j[0]
            k=j[1]
            ad=str(i)+"@"+str(k)
        return ad

    def print_df(self,df,df_sort):
        for i,r in df_sort.iterrows():
            pid=df.loc[df['pid']==i]

            laddr=conn().splitr(pid.laddr)
            raddr=conn().splitr(pid.raddr)
            for status in pid.status:
                t=str(i),str(laddr),str(raddr),str(status)
                print format(t)
              

def main():
    obj=conn()
    cobj=obj.connection()
    
    data_frame=pd.DataFrame()
    data_frame=obj.append(cobj,data_frame)

    df_grp=data_frame.groupby('pid').agg(['count'])

    df_sort=df_grp.apply(lambda x: x.sort_values(ascending=False))

    print "pid,\t\t" +"laddr,\t\t " +"raddr,\t\t   " +"status "
    obj.print_df(data_frame,df_sort)
 

if __name__=='__main__':
    main()
