\copy datahub_be_app_acsrace_bgs_16(id,pop_16,ptwhnl_16,ptblknl_16,ptnanl_16,ptasnl_16,ptpanl_16,ptothnl_16,pt2mnl_16,ptlat_16) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/durham_propbgs/acs_race_2016.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;