from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

def main(dict):
    authenticator = IAMAuthenticator("yHWBp5stAAiPjj3aN62So0PLQ2CEpscHuyQh_3QwYXgQ")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://c7215078-03aa-4238-a655-a144b7caa8d0-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    
    try:
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except ApiException as e:
        print(f"Error: {e.code} - {e.message}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': {'error': 'Internal Server Error'}
        }