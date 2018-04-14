\copy datahub_be_app_compassrace_bgs_1314(id,pop_13,pop_14,ptwhnl_13,ptwhnl_14,ptblknl_13,ptblknl_14,ptasnl_13,ptasnl_14,ptothnl_13,ptothnl_14,ptlat_13,ptlat_14) FROM 'compass_race_1314.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;
