import mysql.connector
import pandas as pd
import json
from mysql.connector import Error
import xlsxwriter

try:
    connection = mysql.connector.connect(host='172.16.224.19',
                                         database='rctkoesio',
                                         user='rctkoesio',
                                         password='rdsHyibKASnw')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        stmt = "select filter from authorization au inner join  account ac on au.tenant_id=ac.id where date_fin >'2018-12-31' and type_compte='CLIENT' and status='ACTIVE'"
        cursor.execute(stmt)
        record = cursor.fetchall()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

        # record sont des tuples de taille 1 element
        list_criterion = []
        maxi_dict_list = []
        for rec in record:
            rec_json = json.loads(rec[0])
            list_criterion.append(rec_json["criterions"])
        for list_elem in list_criterion:
            for mini_dic in list_elem:
                maxi_dict_list.append(mini_dic)
        panda_data = pd.DataFrame(maxi_dict_list)
        panda_data["nombre"] = 1

        # récupère liste des id des propriétés
        unique = panda_data['attribute'].unique()
        properties = [rule for rule in unique if "ProprieteCustomField" in rule]
        prop_id = []
        for propnr in properties:
            myvar = (len(propnr) - propnr.find('_') - 1)
            prop_id.append(propnr[-myvar:])

        #  all-column detailed groupby
        detailed_split = panda_data.groupby(['attribute', 'matcher', 'predicate'])
        detailed_apply_combine = detailed_split['nombre'].size()
        detailed = detailed_apply_combine.to_frame()

        #  rule name detailed groupby
        summary_split = panda_data.groupby('attribute')
        summary_apply_combine = summary_split['nombre'].size()
        summary = summary_apply_combine.to_frame()

# Write each dataframe to a different worksheet
writer = pd.ExcelWriter('pandas_multiple2.xlsx', engine='xlsxwriter')

detailed.to_excel(writer, sheet_name='Sheet1')
summary.to_excel(writer, sheet_name='Sheet2')

writer.save()
