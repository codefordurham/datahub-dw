SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE durham_ltdbacs_7016_tr (gid serial,
   id VARCHAR(12),
   pop70 DOUBLE PRECISION,
   nhwht70 DOUBLE PRECISION,
   pnhwht70 DOUBLE PRECISION,
   nhblk70 DOUBLE PRECISION,
   pnhblk70 DOUBLE PRECISION,
   asian70 DOUBLE PRECISION,
   pasian70 DOUBLE PRECISION,
   haw70 DOUBLE PRECISION,
   phaw70 DOUBLE PRECISION,
   hu70 DOUBLE PRECISION,
   vac70 DOUBLE PRECISION,
   pvac70 DOUBLE PRECISION,
   ohu70 DOUBLE PRECISION,
   pohu70 DOUBLE PRECISION,
   own70 DOUBLE PRECISION,
   pown70 DOUBLE PRECISION,
   rent70 DOUBLE PRECISION,
   prent70 DOUBLE PRECISION,
   mhmval70a17 DOUBLE PRECISION,
   mhmval70 DOUBLE PRECISION,
   mrent70 DOUBLE PRECISION,
   mrent70a17 DOUBLE PRECISION,
   hinc70 DOUBLE PRECISION,
   hinc70a17 DOUBLE PRECISION,
   ag25up70 DOUBLE PRECISION,
   hs70 DOUBLE PRECISION,
   phs70 DOUBLE PRECISION,
   col70 DOUBLE PRECISION,
   pcol70 DOUBLE PRECISION,
   clf70 DOUBLE PRECISION,
   unemp70 DOUBLE PRECISION,
   punemp70 DOUBLE PRECISION,
   pop80 DOUBLE PRECISION,
   nhwht80 DOUBLE PRECISION,
   pnhwht80 DOUBLE PRECISION,
   nhblk80 DOUBLE PRECISION,
   pnhblk80 DOUBLE PRECISION,
   ntv80 DOUBLE PRECISION,
   pntv80 DOUBLE PRECISION,
   asian80 DOUBLE PRECISION,
   pasian80 DOUBLE PRECISION,
   hisp80 DOUBLE PRECISION,
   phisp80 DOUBLE PRECISION,
   haw80 DOUBLE PRECISION,
   phaw80 DOUBLE PRECISION,
   hu80 DOUBLE PRECISION,
   vac80 DOUBLE PRECISION,
   pvac80 DOUBLE PRECISION,
   ohu80 DOUBLE PRECISION,
   pohu80 DOUBLE PRECISION,
   own80 DOUBLE PRECISION,
   pown80 DOUBLE PRECISION,
   rent80 DOUBLE PRECISION,
   prent80 DOUBLE PRECISION,
   mhmval80 DOUBLE PRECISION,
   mhmval80a17 DOUBLE PRECISION,
   mrent80 DOUBLE PRECISION,
   mrent80a17 DOUBLE PRECISION,
   hinc80 DOUBLE PRECISION,
   hinc80a17 DOUBLE PRECISION,
   hincw80 DOUBLE PRECISION,
   hincw80a17 DOUBLE PRECISION,
   hincb80 DOUBLE PRECISION,
   hincb80a17 DOUBLE PRECISION,
   hinch80 DOUBLE PRECISION,
   hinch80a17 DOUBLE PRECISION,
   hinca80 DOUBLE PRECISION,
   hinca80a17 DOUBLE PRECISION,
   ag25up80 DOUBLE PRECISION,
   hs80 DOUBLE PRECISION,
   phs80 DOUBLE PRECISION,
   col80 DOUBLE PRECISION,
   pcol80 DOUBLE PRECISION,
   clf80 DOUBLE PRECISION,
   unemp80 DOUBLE PRECISION,
   punemp80 DOUBLE PRECISION,
   pop90 DOUBLE PRECISION,
   nhwht90 DOUBLE PRECISION,
   pnhwht90 DOUBLE PRECISION,
   nhblk90 DOUBLE PRECISION,
   pnhblk90 DOUBLE PRECISION,
   ntv90 DOUBLE PRECISION,
   pntv90 DOUBLE PRECISION,
   asian90 DOUBLE PRECISION,
   pasian90 DOUBLE PRECISION,
   hisp90 DOUBLE PRECISION,
   phisp90 DOUBLE PRECISION,
   haw90 DOUBLE PRECISION,
   phaw90 DOUBLE PRECISION,
   hu90 DOUBLE PRECISION,
   vac90 DOUBLE PRECISION,
   pvac90 DOUBLE PRECISION,
   ohu90 DOUBLE PRECISION,
   pohu90 DOUBLE PRECISION,
   own90 DOUBLE PRECISION,
   pown90 DOUBLE PRECISION,
   rent90 DOUBLE PRECISION,
   prent90 DOUBLE PRECISION,
   mhmval90 DOUBLE PRECISION,
   mhmval90a17 DOUBLE PRECISION,
   mrent90 DOUBLE PRECISION,
   mrent90a17 DOUBLE PRECISION,
   hinc90 DOUBLE PRECISION,
   hinc90a17 DOUBLE PRECISION,
   hincw90 DOUBLE PRECISION,
   hincw90a17 DOUBLE PRECISION,
   hincb90 DOUBLE PRECISION,
   hincb90a17 DOUBLE PRECISION,
   hinch90 DOUBLE PRECISION,
   hinch90a17 DOUBLE PRECISION,
   hinca90 DOUBLE PRECISION,
   hinca90a17 DOUBLE PRECISION,
   ag25up90 DOUBLE PRECISION,
   hs90 DOUBLE PRECISION,
   phs90 DOUBLE PRECISION,
   col90 DOUBLE PRECISION,
   pcol90 DOUBLE PRECISION,
   clf90 DOUBLE PRECISION,
   unemp90 DOUBLE PRECISION,
   punemp90 DOUBLE PRECISION,
   pop00 DOUBLE PRECISION,
   nhwht00 DOUBLE PRECISION,
   pnhwht00 DOUBLE PRECISION,
   nhblk00 DOUBLE PRECISION,
   pnhblk00 DOUBLE PRECISION,
   ntv00 DOUBLE PRECISION,
   pntv00 DOUBLE PRECISION,
   asian00 DOUBLE PRECISION,
   pasian00 DOUBLE PRECISION,
   hisp00 DOUBLE PRECISION,
   phisp00 DOUBLE PRECISION,
   haw00 DOUBLE PRECISION,
   phaw00 DOUBLE PRECISION,
   hu00 DOUBLE PRECISION,
   vac00 DOUBLE PRECISION,
   pvac00 DOUBLE PRECISION,
   ohu00 DOUBLE PRECISION,
   pohu00 DOUBLE PRECISION,
   own00 DOUBLE PRECISION,
   pown00 DOUBLE PRECISION,
   rent00 DOUBLE PRECISION,
   prent00 DOUBLE PRECISION,
   mhmval00 DOUBLE PRECISION,
   mhmval00a17 DOUBLE PRECISION,
   mrent00 DOUBLE PRECISION,
   mrent00a17 DOUBLE PRECISION,
   hinc00 DOUBLE PRECISION,
   hinc00a17 DOUBLE PRECISION,
   hincw00 DOUBLE PRECISION,
   hincw00a17 DOUBLE PRECISION,
   hincb00 DOUBLE PRECISION,
   hincb00a17 DOUBLE PRECISION,
   hinch00 DOUBLE PRECISION,
   hinch00a17 DOUBLE PRECISION,
   hinca00 DOUBLE PRECISION,
   hinca00a17 DOUBLE PRECISION,
   meansp9800 DOUBLE PRECISION,
   minsp9800 DOUBLE PRECISION,
   maxsp9800 DOUBLE PRECISION,
   mediansp9800 DOUBLE PRECISION,
   stddevsp9800 DOUBLE PRECISION,
   totsp9800 DOUBLE PRECISION,
   nums9800 DOUBLE PRECISION,
   meansp9800a17 DOUBLE PRECISION,
   minsp9800a17 DOUBLE PRECISION,
   maxsp9800a17 DOUBLE PRECISION,
   mediansp9800a17 DOUBLE PRECISION,
   totsp9800a17 DOUBLE PRECISION,
   pir9800 DOUBLE PRECISION,
   ag25up00 DOUBLE PRECISION,
   hs00 DOUBLE PRECISION,
   phs00 DOUBLE PRECISION,
   col00 DOUBLE PRECISION,
   pcol00 DOUBLE PRECISION,
   clf00 DOUBLE PRECISION,
   unemp00 DOUBLE PRECISION,
   punemp00 DOUBLE PRECISION,
   pop10 DOUBLE PRECISION,
   nhwht10 DOUBLE PRECISION,
   pnhwht10 DOUBLE PRECISION,
   nhblk10 DOUBLE PRECISION,
   pnhblk10 DOUBLE PRECISION,
   ntv10 DOUBLE PRECISION,
   pntv10 DOUBLE PRECISION,
   asian10 DOUBLE PRECISION,
   pasian10 DOUBLE PRECISION,
   hisp10 DOUBLE PRECISION,
   phisp10 DOUBLE PRECISION,
   haw10 DOUBLE PRECISION,
   phaw10 DOUBLE PRECISION,
   hu10 DOUBLE PRECISION,
   vac10 DOUBLE PRECISION,
   pvac10 DOUBLE PRECISION,
   ohu10 DOUBLE PRECISION,
   pohu10 DOUBLE PRECISION,
   own10 DOUBLE PRECISION,
   pown10 DOUBLE PRECISION,
   rent10 DOUBLE PRECISION,
   prent10 DOUBLE PRECISION,
   mhmval12 DOUBLE PRECISION,
   mhmval12a17 DOUBLE PRECISION,
   mrent12 DOUBLE PRECISION,
   mrent12a17 DOUBLE PRECISION,
   hinc12 DOUBLE PRECISION,
   hinc12a17 DOUBLE PRECISION,
   hincw12 DOUBLE PRECISION,
   hincw12a17 DOUBLE PRECISION,
   hincb12 DOUBLE PRECISION,
   hincb12a17 DOUBLE PRECISION,
   hinch12 DOUBLE PRECISION,
   hinch12a17 DOUBLE PRECISION,
   hinca12 DOUBLE PRECISION,
   hinca12a17 DOUBLE PRECISION,
   meansp0809 DOUBLE PRECISION,
   minsp0809 DOUBLE PRECISION,
   maxsp0809 DOUBLE PRECISION,
   mediansp0809 DOUBLE PRECISION,
   stddevsp0809 DOUBLE PRECISION,
   totsp0809 DOUBLE PRECISION,
   nums0809 DOUBLE PRECISION,
   meansp0809a17 DOUBLE PRECISION,
   minsp0809a17 DOUBLE PRECISION,
   maxsp0809a17 DOUBLE PRECISION,
   mediansp0809a17 DOUBLE PRECISION,
   totsp0809a17 DOUBLE PRECISION,
   pir0812 DOUBLE PRECISION,
   ag25up12 DOUBLE PRECISION,
   hs12 DOUBLE PRECISION,
   phs12 DOUBLE PRECISION,
   col12 DOUBLE PRECISION,
   pcol12 DOUBLE PRECISION,
   clf12 DOUBLE PRECISION,
   unemp12 DOUBLE PRECISION,
   punemp12 DOUBLE PRECISION,
   pccol0012 DOUBLE PRECISION,
   pcnhwht0010 DOUBLE PRECISION,
   pcnhblk0010 DOUBLE PRECISION,
   pcasian0010 DOUBLE PRECISION,
   pchisp0010 DOUBLE PRECISION,
   cmhmval0012a17 DOUBLE PRECISION,
   pcmhmval0012a17 DOUBLE PRECISION,
   cmrent0012a17 DOUBLE PRECISION,
   pcmrent0012a17 DOUBLE PRECISION,
   chinc0012a17 DOUBLE PRECISION,
   chincw0012a17 DOUBLE PRECISION,
   chincb0012a17 DOUBLE PRECISION,
   chinca0012a17 DOUBLE PRECISION,
   chinch0012a17 DOUBLE PRECISION,
   cmeansp0009a17 DOUBLE PRECISION,
   cmediansp0009a17 DOUBLE PRECISION,
   pchinc0012a17 DOUBLE PRECISION,
   pchincw0012a17 DOUBLE PRECISION,
   pchincb0012a17 DOUBLE PRECISION,
   pchinca0012a17 DOUBLE PRECISION,
   pchinch0012a17 DOUBLE PRECISION,
   pcmeansp0009a17 DOUBLE PRECISION,
   pcmediansp0009a17 DOUBLE PRECISION,
   pop16 DOUBLE PRECISION,
   nhwht16 DOUBLE PRECISION,
   pnhwht16 DOUBLE PRECISION,
   nhblk16 DOUBLE PRECISION,
   pnhblk16 DOUBLE PRECISION,
   ntv16 DOUBLE PRECISION,
   pntv16 DOUBLE PRECISION,
   asian16 DOUBLE PRECISION,
   pasian16 DOUBLE PRECISION,
   haw16 DOUBLE PRECISION,
   phaw16 DOUBLE PRECISION,
   oth16 DOUBLE PRECISION,
   poth16 DOUBLE PRECISION,
   twomr16 DOUBLE PRECISION,
   ptwomr16 DOUBLE PRECISION,
   hisp16 DOUBLE PRECISION,
   phisp16 DOUBLE PRECISION,
   pcnhwht0016 DOUBLE PRECISION,
   pcnhblk0016 DOUBLE PRECISION,
   pcasian0016 DOUBLE PRECISION,
   pchisp0016 DOUBLE PRECISION,
   pcnhwht1016 DOUBLE PRECISION,
   pcnhblk1016 DOUBLE PRECISION,
   pcasian1016 DOUBLE PRECISION,
   pchisp1016 DOUBLE PRECISION,
   hu16 DOUBLE PRECISION,
   ohu16 DOUBLE PRECISION,
   pohu16 DOUBLE PRECISION,
   vac16 DOUBLE PRECISION,
   pvac16 DOUBLE PRECISION,
   own16 DOUBLE PRECISION,
   pown16 DOUBLE PRECISION,
   rent16 DOUBLE PRECISION,
   prent16 DOUBLE PRECISION,
   mhmval16 DOUBLE PRECISION,
   mrent16 DOUBLE PRECISION,
   mhmval16a17 DOUBLE PRECISION,
   mrent16a17 DOUBLE PRECISION,
   cmhmval0016a17 DOUBLE PRECISION,
   pcmhmval0016a17 DOUBLE PRECISION,
   cmrent0016a17 DOUBLE PRECISION,
   pcmrent0016a17 DOUBLE PRECISION,
   cmhmval1216a17 DOUBLE PRECISION,
   pcmhmval1216a17 DOUBLE PRECISION,
   cmrent1216a17 DOUBLE PRECISION,
   pcmrent1216a17 DOUBLE PRECISION,
   hinc16 DOUBLE PRECISION,
   hinc16a17 DOUBLE PRECISION,
   hincw16 DOUBLE PRECISION,
   hincw16a17 DOUBLE PRECISION,
   hincb16 DOUBLE PRECISION,
   hincb16a17 DOUBLE PRECISION,
   hincn16 DOUBLE PRECISION,
   hincn16a17 DOUBLE PRECISION,
   hinca16 DOUBLE PRECISION,
   hinca16a17 DOUBLE PRECISION,
   hincp16 DOUBLE PRECISION,
   hincp16a17 DOUBLE PRECISION,
   hinco16 DOUBLE PRECISION,
   hinco16a17 DOUBLE PRECISION,
   hincm16 DOUBLE PRECISION,
   hincm16a17 DOUBLE PRECISION,
   hinch16 DOUBLE PRECISION,
   hinch16a17 DOUBLE PRECISION,
   meansp1517 DOUBLE PRECISION,
   minsp1517 DOUBLE PRECISION,
   maxsp1517 DOUBLE PRECISION,
   mediansp1517 DOUBLE PRECISION,
   stddevsp1517 DOUBLE PRECISION,
   totsp1517 DOUBLE PRECISION,
   nums1517 DOUBLE PRECISION,
   meansp1517a17 DOUBLE PRECISION,
   minsp1517a17 DOUBLE PRECISION,
   maxsp1517a17 DOUBLE PRECISION,
   mediansp1517a17 DOUBLE PRECISION,
   totsp1517a17 DOUBLE PRECISION,
   pir1517 DOUBLE PRECISION,
   chinc1216a17 DOUBLE PRECISION,
   chincw1216a17 DOUBLE PRECISION,
   chincb1216a17 DOUBLE PRECISION,
   chinca1216a17 DOUBLE PRECISION,
   chinch1216a17 DOUBLE PRECISION,
   cmeansp0917a17 DOUBLE PRECISION,
   cmediansp0917a17 DOUBLE PRECISION,
   pchinc1216a17 DOUBLE PRECISION,
   pchincw1216a17 DOUBLE PRECISION,
   pchincb1216a17 DOUBLE PRECISION,
   pchinca1216a17 DOUBLE PRECISION,
   pchinch1216a17 DOUBLE PRECISION,
   pcmeansp0917a17 DOUBLE PRECISION,
   pcmediansp0917a17 DOUBLE PRECISION,
   chinc0016a17 DOUBLE PRECISION,
   chincw0016a17 DOUBLE PRECISION,
   chincb0016a17 DOUBLE PRECISION,
   chinca0016a17 DOUBLE PRECISION,
   chinch0016a17 DOUBLE PRECISION,
   cmeansp0017a17 DOUBLE PRECISION,
   cmediansp0017a17 DOUBLE PRECISION,
   pchinc0016a17 DOUBLE PRECISION,
   pchincw0016a17 DOUBLE PRECISION,
   pchincb0016a17 DOUBLE PRECISION,
   pchinca0016a17 DOUBLE PRECISION,
   pchinch0016a17 DOUBLE PRECISION,
   pcmeansp0017a17 DOUBLE PRECISION,
   pcmediansp0017a17 DOUBLE PRECISION,
   ag25up16 DOUBLE PRECISION,
   batm16 DOUBLE PRECISION,
   masm16 DOUBLE PRECISION,
   prom16 DOUBLE PRECISION,
   phdm16 DOUBLE PRECISION,
   batf16 DOUBLE PRECISION,
   masf16 DOUBLE PRECISION,
   prof16 DOUBLE PRECISION,
   phdf16 DOUBLE PRECISION,
   col16 DOUBLE PRECISION,
   pcol16 DOUBLE PRECISION,
   pccol1216 DOUBLE PRECISION,
   pccol0016 DOUBLE PRECISION,
   grprchi12 DOUBLE PRECISION,
   grprchi16 DOUBLE PRECISION,
   pcgrprchi1216 DOUBLE PRECISION,
   mmocphi12 DOUBLE PRECISION,
   mmocphiym12 DOUBLE PRECISION,
   mmocphinm12 DOUBLE PRECISION,
   mmocphi16 DOUBLE PRECISION,
   mmocphiym16 DOUBLE PRECISION,
   mmocphinm16 DOUBLE PRECISION,
   pcmmocphiym1216 DOUBLE PRECISION);
ALTER TABLE durham_ltdbacs_7016_tr ADD PRIMARY KEY (gid);
COMMIT;
