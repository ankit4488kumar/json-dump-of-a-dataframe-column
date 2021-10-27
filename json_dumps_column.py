import json
import traceback
#from env import appendOfaErrors

def JsonDumpsColumns(JsonDumpsColumnsData, JsonDumpsColumns):
    try:
        for json_column in JsonDumpsColumns:
            JsonDumpsColumnsData[json_column] = JsonDumpsColumnsData[json_column].apply(lambda x:json.dumps(x))
            #JsonDumpsColumnsData[json_column] = "{}"
    except Exception as e:
        #appendOfaErrors(JsonDumpsColumnsData, e, "JsonDumpsColumns")
        print("Error in JsonDumpsColumns processing- ", e) 
        traceback.print_exc()
    return JsonDumpsColumnsData
    