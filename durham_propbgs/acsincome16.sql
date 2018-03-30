\copy acsincome_bgs_2016(geoid10,mhi,mhi_ah,mnhi,mgr_phi,mmoc_phi) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtual/development/datahub-dw/durham_propbgs/acs_income_2016.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
