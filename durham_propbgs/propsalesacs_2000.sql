SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;

CREATE TABLE datahub_be_app_propsales00 (id char(12),
   meansp numeric,
   minsp numeric,
   maxsp numeric,
   mediansp numeric,
   totsp numeric,
   nums numeric,
   mhi numeric,
   pir numeric,
   mgr_phi numeric,
   mmoc_phi numeric);

\copy datahub_be_app_propsales00(id,meansp,minsp,maxsp,mediansp,totsp,nums,mhi,pir,mgr_phi,mmoc_phi) FROM '/home/jmcmanus/code_for_durham/affordable_housing/data/propmap/propsalesacs_2000_bgs.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
