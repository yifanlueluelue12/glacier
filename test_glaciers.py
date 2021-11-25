from pathlib import Path
from pytest import raises
from glaciers import GlacierCollection, Glacier

def test_with_of_code_length():
    with raises(ValueError) as exception: 
        file_path = Path("../sheet-A.csv")
        collection = GlacierCollection(file_path)
        collection.filter_by_code('5247')


def test_with_of_code_classes():
    with raises(ValueError) as exception: 
        file_path = Path("../sheet-A.csv")
        collection = GlacierCollection(file_path)
        collection.filter_by_code('54o')



def test_is_not_accurateID():
    with raises(ValueError) as exception:     
        Glacier("1045A", "BETA", "AR", -33.0875, -70.0567, 524)
def test_is_not_5digits_ID():
    with raises(ValueError) as exception:      
        Glacier("104543", "BETA", "AR", -33.0875, -70.0567, 524)    

def test_with_lat():
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -50.75, -70.0567, 524) 
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -58.84, -70.0567, 524)
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", 58.84, -70.0567, 524) 
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -52.84, -70.0567, 524) 
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -69.84, -70.0567, 524) 

def test_with_lon():
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -33.0875, -69.0567, 524)    
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -33.0875, -78.0567, 524)
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -33.0875, 70.0567, 524)
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -33.0875, 69.0567, 524)
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "AR", -33.0875, -73.0567, 524) 


def test_with_unit():
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "TR", -33.0875, -73.0567, 524)    
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "aR", -33.0875, -73.0567, 524)
    with raises(ValueError) as exception: 
        Glacier("10454", "BETA", "ART", -33.0875, -73.0567, 524)

