\copy datahub_be_app_propsales00(id,meansp,minsp,maxsp,mediansp,totsp,nums,mhi,pir,mgr_phi,mmoc_phi) FROM '/home/jmcmanus/code_for_durham/affordable_housing/virtualenv/development/datahub-dw/durham_propbgs/propsalesdec_2000_bgs.csv' WITH DELIMITER ',' CSV HEADER;

COMMIT;