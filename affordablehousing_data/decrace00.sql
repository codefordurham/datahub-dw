\copy datahub_be_app_decrace_bgs_00(id,pop_00,ptwhnl_00,ptblknl_00,ptnanl_00,ptasnl_00,ptpanl_00,ptothnl_00,pt2mnl_00,ptlat_00) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/affordablehousing_data/dec_race_2000.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
