#faut remplir le db index 
#cf feature_description.py
db_desc=[]
.
.
.
no.save(outputdir+'_dbdesc.npy',dbdesc)

#indexation
fl=cv2.flann.Index(np.array(db.desc,np.float32),index.params)
fl.save(outputdir+'_linear_index.dat')