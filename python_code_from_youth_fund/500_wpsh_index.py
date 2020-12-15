import Ngl,Nio
import datetime


fname = "/mnt/g/ERA5/1980-1989_gh_uv_500_850_200.grib"
f = Nio.open_file(fname,"r")
# t = f.variables["initial_time0_hours"]
# print(t.units)
# date_ini = datetime.datetime(1800,1,1,0)
# for i in range(len(t[:])):
#     delta = (datetime.timedelta(hours=t[i]))
#     time = date_ini + delta
#     print(time)
h_q = f.variables['Z_GDS0_ISBL_S123'][:,{500},:,:]

print(h_q)
# a_q = addfile("/mnt/g/ERA5/1980-1989_gh_uv_500_850_200.grib","r")
# a_h = addfile("/mnt/g/ERA5/1990-2019_gh_u_500.grib","r")
# h_q = a_q->Z_GDS0_ISBL_S123(6::12,{500},:,:)
# h_h = a_h->Z_GDS0_ISBL_S123(6::12,:,:)
# t_q = a_q->initial_time0_hours(6::12)
# t_h = a_h->initial_time0_hours(6::12)
# h = array_append_record(h_q,h_h,0)
# t = array_append_record(t_q,t_h,0)