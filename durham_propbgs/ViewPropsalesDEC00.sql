CREATE VIEW propsalesdec_2000_bgs AS
    SELECT PS.geoid00, PS.mean_sale_price, PS.min_sale_price, PS.max_sale_price, 
           PS.median_sale_price, PS.total_sale_price, PS.num_sales, DEC.mhi99 AS mhi,
           CAST(PS.median_sale_price AS DECIMAL)/CAST(DEC.mhi99 AS DECIMAL) AS pir, 
           mgr_phi99 AS mgr_phi, mmoc_phi99 AS mmoc_phi, PS.begin_date, PS.end_date
    FROM propsales_bgs_2001 AS PS
    INNER JOIN decincome_bgs_2000 AS DEC ON (PS.geoid00=DEC.geoid00);
