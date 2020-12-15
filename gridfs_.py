import pymongo
from gridfs import GridFS
from bson.objectid import ObjectId
import time


# 用于GridFS的常规操作

class MongoGridFS():
    '''
    classdocs
    '''
    UploadCache = "uploadcache"
    dbURL = "mongodb://localhost:27017"


    def __init__(self, dbname):  # 传入数据库的名字
        client = pymongo.MongoClient(self.dbURL)
        self.db = client[dbname]


    # 判断文件是否存在,根据文件名
    def isExists(self, file_coll, filename):
        gridfs_col = GridFS(self.db, collection=file_coll)
        query = {"filename":""}
        query["filename"] = filename
              
        if gridfs_col.exists(query):
            print(f'{filename}存在')


    #上传文件
    def upLoadFile(self, file_coll, file_name, data_link):
        filter_condition = {"filename": file_name, "url": data_link}
        gridfs_col = GridFS(self.db, collection=file_coll)
        file_ = "0"
        query = {"filename":""}
        query["filename"] = file_name
                
        if gridfs_col.exists(query):
            print('已经存在该文件')
        else:
            with open(file_name, 'rb') as file_r:
                file_data = file_r.read()
                file_ = gridfs_col.put(data=file_data, **filter_condition)  # 上传到gridfs
                print(file_)
     
        return file_   
    # 按文件名获取文档
    def downLoadFile(self, file_coll, file_name, out_name, ver):
        gridfs_col = GridFS(self.db, collection=file_coll)
        try:
            file_data = gridfs_col.get_version(filename=file_name, version=ver).read()
        
            with open(out_name, 'wb') as file_w:
                file_w.write(file_data)
        except Error as error:
            print(error)
            print("获取失败")
        
    # 按文件_Id获取文档
    def downLoadFilebyID(self, file_coll, _id, out_name):
        gridfs_col = GridFS(self.db, collection=file_coll)
        
        O_Id = ObjectId(_id)
        try:
            gf = gridfs_col.get(file_id=O_Id)
            file_data = gf.read()
            with open(out_name, 'wb') as file_w:
                file_w.write(file_data)     
            return gf.filename    
        except:
            print("获取失败")
    # 列出所有文件
    def listAll(self, file_coll):
        print(GridFS(self.db, collection=file_coll).list())

if __name__ == '__main__':
    a = MongoGridFS("gridfs")
    # file_collrint(GridFS(a.db, collection="fs").list())
    # a.listAll("fs")
    a.isExists("fs", "gh_500_201911.grb")
    # a.upLoadFile("pdf","test_gribfs.py","")
    # a.downLoadFile("pdf","test_gribfs.py","out2.p",-1)
    # ll = a.downLoadFilebyID("pdf","5fcde0dfc94f75cee5f57311","out3.p")
    # print (ll)