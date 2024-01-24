import pytest
from hurcan_POS import*

# Indexs for Item Inventory
MODEL_INDEX = 0
SERIAL_INDEX = 1  
PRICE_INDEX = 2
RECIVED_INDEX = 3 
LOCATION_INDEX = 4

# Indexes for the Customer Account List
ACCOUNT_NUM_INDEX = 0
ACCOUNT_NAME__INDEX = 1
ACCOUNT_PHONE_NUM_INDEX = 2
ACCOUNT_EMAIL_INDEX =3
ACCOUNT_ADDRESS_INDEX = 4
ACCOUNT_BAL_INDEX = 5








pytest.main(["-v", "--tb=line", "-rN", __file__])