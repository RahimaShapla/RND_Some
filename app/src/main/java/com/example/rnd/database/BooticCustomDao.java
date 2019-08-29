package com.example.rnd.database;


import android.arch.persistence.room.Dao;
import android.arch.persistence.room.Query;

import com.w3engineers.ecommerce.bootic.data.helper.models.CustomProductInventory;

import java.util.List;

@Dao

public interface BooticCustomDao extends BaseDao<CustomProductInventory> {

    @Query("SELECT * FROM " + TableNames.CODES)
    List<CustomProductInventory> getAllFlowableCodes();

    @Query("SELECT COUNT(id) FROM " + TableNames.CODES)
    int getRowCount();


    @Query("DELETE FROM "  + TableNames.CODES)
    void nukeTable();

    @Query("UPDATE " + TableNames.CODES+" SET currentQuantity = :quantity WHERE id =:id")
    void update(int quantity, int id);

}
