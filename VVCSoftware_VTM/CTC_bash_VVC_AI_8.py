##creat_ssh.py
##_author_='Yu_Pengfei'
import os
#取出测试文件列表：
def load_file_list(directory):
    list = []
    for filename in [y for y in os.listdir(directory) if os.path.isfile(os.path.join(directory,y))]:
        if filename.split('.')[-1]=='yuv':
            list.append(filename.split('.yuv')[0])
    return sorted(list)
YUV_PATH="../../HEVCceshishipin"
CLASS_LIST=["ClassA","ClassB","ClassC","ClassD","ClassE","ClassF"]
SOFTWARE_PATH="./EncoderAppStatic"
with open('CTC_bash_VVC_AI_8.sh','a') as f:  
    #encoder_lowdelay_main10.cfg
    f.write("mkdir VVC_CTCAI\n")
    for CLASS in CLASS_LIST:
        f.write('mkdir VVC_CTCAI/'+CLASS+"\n")
        f.write('mkdir VVC_CTCAI/'+CLASS+"/vvc\n")
        f.write('mkdir VVC_CTCAI/'+CLASS+"/txt\n")
        f.write('mkdir VVC_CTCAI/'+CLASS+"/rec_yuv\n")
        YUV_LIST=load_file_list(YUV_PATH+'/'+CLASS)
        for qp in [22,27,32,37]:
            f.write('mkdir VVC_CTCAI/'+CLASS+"/vvc/"+str(qp)+"\n")
            f.write('mkdir VVC_CTCAI/'+CLASS+"/txt/"+str(qp)+"\n")
            f.write('mkdir VVC_CTCAI/'+CLASS+"/rec_yuv/"+str(qp)+"\n")           
            for YUV in YUV_LIST:
                f.write(SOFTWARE_PATH)
                f.write(' -ipp '+YUV_PATH+'/'+CLASS)
                f.write(' -i '+YUV+'.yuv')
                f.write(' -c '+'../cfg/encoder_intra_vtm_8bit.cfg')
                YUV_CFG=YUV.split('_')[0]+'.cfg'
                f.write(' -c '+'../cfg/'+'per-sequence/'+YUV_CFG)
                f.write(' -f '+'30 ')
                f.write(' -q '+str(qp)+' ')
                f.write(' -b '+'VVC_CTCAI/'+CLASS+'/vvc/'+str(qp)+'/'+YUV+'.vvc')
                f.write(' -o '+'VVC_CTCAI/'+CLASS+'/rec_yuv/'+str(qp)+'/'+YUV+'.yuv')
                f.write(' > '+'VVC_CTCAI/'+CLASS+'/txt/'+str(qp)+'/'+YUV.split('.')[0]+'.txt\n')
