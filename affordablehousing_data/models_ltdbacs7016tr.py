from django.db import models

class LTDBACS_trts_7016(models.Model):
   id = models.TextField(12,primary_key=True)
   pop70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   nhwht70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhwht70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   nhblk70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhblk70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   asian70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pasian70 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   haw70 = models.DecimalField(max_digits=4,decimal_places=2,null=False)
   phaw70 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   hu70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   vac70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pvac70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ohu70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pohu70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   own70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pown70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   rent70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   prent70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mhmval70a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   mhmval70 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   mrent70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   mrent70a17 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   hinc70 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   hinc70a17 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   ag25up70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   hs70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   phs70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   col70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pcol70 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   clf70 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   unemp70 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   punemp70 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   pop80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   nhwht80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhwht80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   nhblk80 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pnhblk80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ntv80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   pntv80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   asian80 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pasian80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   hisp80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   phisp80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   haw80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   phaw80 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   hu80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   vac80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pvac80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ohu80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pohu80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   own80 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   pown80 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   rent80 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   prent80 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   mhmval80 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   mhmval80a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mrent80 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   mrent80a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   hinc80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hinc80a17 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hincw80 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincw80a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincb80 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincb80a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinch80 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinch80a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinca80 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hinca80a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   ag25up80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hs80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   phs80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   col80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pcol80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   clf80 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   unemp80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   punemp80 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pop90 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   nhwht90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhwht90 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   nhblk90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhblk90 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   ntv90 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pntv90 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   asian90 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pasian90 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
   hisp90 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   phisp90 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   haw90 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   phaw90 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   hu90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   vac90 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pvac90 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ohu90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pohu90 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   own90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pown90 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   rent90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   prent90 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mhmval90 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mhmval90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mrent90 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   mrent90a17 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hinc90 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hinc90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincw90 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincw90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincb90 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hincb90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinch90 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinch90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinca90 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hinca90a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   ag25up90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hs90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   phs90 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   col90 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pcol90 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   clf90 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   unemp90 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   punemp90 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pop00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   nhwht00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pnhwht00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   nhblk00 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pnhblk00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ntv00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   pntv00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   asian00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pasian00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   hisp00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   phisp00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   haw00 = models.DecimalField(max_digits=4,decimal_places=2,null=False)
   phaw00 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   hu00 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   vac00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pvac00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ohu00 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   pohu00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   own00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pown00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   rent00 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   prent00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mhmval00 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mhmval00a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mrent00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mrent00a17 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hinc00 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   hinc00a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   hincw00 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincw00a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincb00 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hincb00a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinch00 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinch00a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinca00 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinca00a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   meansp9800 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   minsp9800 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   maxsp9800 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mediansp9800 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   stddevsp9800 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp9800 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   nums9800 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   meansp9800a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   minsp9800a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp9800a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mediansp9800a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp9800a17 = models.DecimalField(max_digits=13,decimal_places=2,null=True)
   pir9800 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   ag25up00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   hs00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   phs00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   col00 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pcol00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   clf00 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   unemp00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   punemp00 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pop10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   nhwht10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pnhwht10 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   nhblk10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pnhblk10 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ntv10 = models.DecimalField(max_digits=3,decimal_places=1,null=False)
   pntv10 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   asian10 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   pasian10 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   hisp10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   phisp10 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   haw10 = models.DecimalField(max_digits=2,decimal_places=1,null=False)
   phaw10 = models.DecimalField(max_digits=4,decimal_places=2,null=False)
   hu10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   vac10 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   pvac10 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   ohu10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pohu10 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   own10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pown10 = models.DecimalField(max_digits=5,decimal_places=2,null=False)
   rent10 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   prent10 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   mhmval12 = models.DecimalField(max_digits=7,decimal_places=1,null=False)
   mhmval12a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   mrent12 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   mrent12a17 = models.DecimalField(max_digits=8,decimal_places=2,null=False)
   hinc12 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   hinc12a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   hincw12 = models.DecimalField(max_digits=7,decimal_places=1,null=False)
   hincw12a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   hincb12 = models.DecimalField(max_digits=7,decimal_places=1,null=False)
   hincb12a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   hinch12 = models.DecimalField(max_digits=7,decimal_places=1,null=False)
   hinch12a17 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   hinca12 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   hinca12a17 = models.DecimalField(max_digits=10,decimal_places=2,null=False)
   meansp0709 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   minsp0709 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   maxsp0709 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mediansp0709 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   stddevsp0709 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp0709 = models.DecimalField(max_digits=11,decimal_places=2,null=True)
   nums0709 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   meansp0709a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   minsp0709a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp0709a17 = models.DecimalField(max_digits=11,decimal_places=2,null=True)
   mediansp0709a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp0709a17 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   pir0712 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   ag25up12 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   hs12 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   phs12 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   col12 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pcol12 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   clf12 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   unemp12 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   punemp12 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pcnhwht0010 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pcnhblk0010 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pcasian0010 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pchisp0010 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   cmhmval0012a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   pcmhmval0012a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   cmrent0012a17 = models.DecimalField(max_digits=7,decimal_places=2,null=False)
   pcmrent0012a17 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   chinc0012a17 = models.DecimalField(max_digits=9,decimal_places=2,null=False)
   chincw0012a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chincb0012a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chinca0012a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   chinch0012a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   cmeansp0009a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   cmediansp0009a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   pchinc0012a17 = models.DecimalField(max_digits=6,decimal_places=2,null=False)
   pchincw0012a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchincb0012a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pchinca0012a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchinch0012a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pcmeansp0009a17 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   pcmediansp0009a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pop16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   nhwht16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pnhwht16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   nhblk16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pnhblk16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   ntv16 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   pntv16 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
   asian16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pasian16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   haw16 = models.DecimalField(max_digits=3,decimal_places=1,null=False)
   phaw16 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
   oth16 = models.DecimalField(max_digits=3,decimal_places=1,null=False)
   poth16 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
   twomr16 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   ptwomr16 = models.DecimalField(max_digits=4,decimal_places=2,null=True)
   hisp16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   phisp16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   pcnhwht0016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcnhblk0016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcasian0016 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   pchisp0016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcnhwht1016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcnhblk1016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcasian1016 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   pchisp1016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   hu16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   ohu16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pohu16 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   vac16 = models.DecimalField(max_digits=4,decimal_places=1,null=False)
   pvac16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   own16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pown16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   rent16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   prent16 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   mhmval16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   mrent16 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   mhmval16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mrent16a17 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   cmhmval0016a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   pcmhmval0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   cmrent0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pcmrent0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   cmhmval1216a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   pcmhmval1216a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   cmrent1216a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcmrent1216a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   hinc16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinc16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincw16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincw16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincb16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincb16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincn16 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   hincn16a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinca16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinca16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincp16 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
   hincp16a17 = models.DecimalField(max_digits=4,decimal_places=1,null=True)
   hinco16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinco16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hincm16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hincm16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   hinch16 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   hinch16a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   meansp1517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   minsp1517 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   maxsp1517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   mediansp1517 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   stddevsp1517 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp1517 = models.DecimalField(max_digits=12,decimal_places=2,null=True)
   nums1517 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   meansp1517a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   minsp1517a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   maxsp1517a17 = models.DecimalField(max_digits=11,decimal_places=2,null=True)
   mediansp1517a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   totsp1517a17 = models.DecimalField(max_digits=13,decimal_places=2,null=True)
   pir1517 = models.DecimalField(max_digits=5,decimal_places=2,null=True)
   chinc1216a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chincw1216a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chincb1216a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chinca1216a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   chinch1216a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   cmeansp0917a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   cmediansp0917a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   pchinc1216a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchincw1216a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pchincb1216a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchinca1216a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pchinch1216a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pcmeansp0917a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pcmediansp0917a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   chinc0016a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chincw0016a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   chincb0016a17 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   chinca0016a17 = models.DecimalField(max_digits=8,decimal_places=2,null=True)
   chinch0016a17 = models.DecimalField(max_digits=9,decimal_places=2,null=True)
   cmeansp0017a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   cmediansp0017a17 = models.DecimalField(max_digits=10,decimal_places=2,null=True)
   pchinc0016a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchincw0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pchincb0016a17 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pchinca0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pchinch0016a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pcmeansp0017a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   pcmediansp0017a17 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
   ag25up16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   colm16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   colf16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   col16 = models.DecimalField(max_digits=5,decimal_places=1,null=False)
   pcol16 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
   pccol0016 = models.DecimalField(max_digits=6,decimal_places=2,null=True)
