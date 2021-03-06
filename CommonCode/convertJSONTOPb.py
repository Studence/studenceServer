import json

from google.protobuf import json_format


class ConvertJSONToPb:

    def converjsontoPB(self, response, instanceType):
        return json_format.Parse(response, instanceType, ignore_unknown_fields=False)

    #use this
    def converjsontoPBProper(self, response, instanceType):
        #return json2pb(pb=WorkerPb,js=json.dumps(response))
        return json_format.Parse(text=json.dumps(response), message=instanceType, ignore_unknown_fields=False)

    def convertToProperjson(self, response):
        finaljson = '"'
        for i in response:
            if (i == "'"):
                finaljson += '"'
            else:
                finaljson += i
        return finaljson

    def getQuotedJson(self,jsonReq):
        return '"'+str(jsonReq)+'"'
