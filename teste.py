import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
filename = get_testdata_files("CT_small.dcm")[0]
filename2 = "/home/rodrigo/Projects/TCC/samples/PatientZero/ct_plain/CT000000.dcm"
print(filename)
print(filename2)
ds = pydicom.dcmread(filename2)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
