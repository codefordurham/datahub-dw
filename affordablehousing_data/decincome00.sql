SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE decincome_bgs_2000 (gid serial,
     geoid00 varchar(12),
     mgr_phi99 double precision,
     mmoc_phi99 double precision, 
     mhi99 double precision, 
     mhi99_ah double precision, 
     mfh99 double precision, 
     mnhi99 double precision, 
     mhi99_w double precision, 
     mhi99_b double precision, 
     mhi99_n double precision, 
     mhi99_a double precision, 
     mhi99_h double precision, 
     mhi99_o double precision, 
     mhi_99_t double precision, 
     mhi99_wnh double precision, 
     mfi99_w double precision, 
     mfi99_b double precision, 
     mfi99_n double precision, 
     mfi99_a double precision, 
     mfi99_h double precision, 
     mfi99_o double precision, 
     mfi99_t double precision, 
     mfi99_wnh double precision, 
     mnfh99 double precision); 
ALTER TABLE decincome_bgs_2000 ADD PRIMARY KEY (gid);
COMMIT;
\copy decincome_bgs_2000(geoid00,mgr_phi99,mmoc_phi99,mhi99,mhi99_ah,mfh99,mnhi99,mhi99_w,mhi99_b,mhi99_n,mhi99_a,mhi99_h,mhi99_o,mhi_99_t,mhi99_wnh,mfi99_w,mfi99_b,mfi99_n,mfi99_a,mfi99_h,mfi99_o,mfi99_t,mfi99_wnh,mnfh99) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/affordablehousing_data/dec_income_2000.csv' WITH DELIMITER ',' CSV HEADER;
COMMIT;
