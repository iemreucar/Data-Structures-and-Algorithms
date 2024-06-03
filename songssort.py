import os
class SongsSort():

    def list_files(self,path):
        try:
            self.dir_list = os.listdir(path)
            with open("D:\\MuSiK\\all_songs.txt","w",encoding="utf-8") as file:
                for i in self.dir_list:
                    # print(f"files in'{path}':")
                    # print(i)
                    file.write(f"folder name:"+i+"\n")
                    pathstr=path+"\\"+i
                    self.mp3_list = os.listdir(pathstr)
                    for i2 in  self.mp3_list:      #mp3leri yazma
                        if ".mp3" in i2:
                            # print(i2)
                            file.write(i2+"\n")
                            if i2.split()[0] == "the" or i2.split()[0]=="The":
                                b=i2.split()[1].replace("_","")
                                print(b)
                            else:
                                b=i2.split()[0].replace("_","")
                                print(b)

                    # for i2 in  mp3_list:      #mp3 olmayanlari yazma
                    #     if not ".mp3" in i2:
                    #         print(i2)
                    #         file.write(i2+"\n")
                    # for i2 in  mp3_list:      #herseyi yazma
                    #         print(i2)
                    #         file.write(i2+"\n")
                    list2=[]
                    set1=set()
                    # for j in mp3_list:          #aynilari varmi yokmu
                    #     if j not in set1:
                    #         set1.add(j)
                    #     else:
                    #         print(j)
                    # print(set1)
                    # for i in mp3_list:
                    #     i_modified=i.strip().split()
                    #     i_modified[0].strip("-","_")
                    #     print(i)
        except FileNotFoundError:
            print("no folder")

    def find_name(self):
        for i in self.mp3_list:
            i.split()[0].replace("_","")
            print(i)

path = "D:\\MuSiK\\ipod4 rv1"
songs=SongsSort()
songs.list_files(path)
# songs.find_name()


# a="dh_j kjgsd    sdlgf"
# b=a.split()[0].replace("_","")

# print(b)

# b=a.strip().split()
# print(b[0].split("_"))

