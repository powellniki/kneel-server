import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

#imports
from views import get_all_orders, get_single_order, create_order, delete_order, update_order



class JSONServer(HandleRequests):
    """server class to handle incoming HTTP requests for kneel-diamonds"""


    def do_GET(self):
        """handles GET request from client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url['requested_resource'] == 'orders':
            if url['pk'] == 0:
                response_body = get_all_orders()
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            else:
                response_body = get_single_order(url)
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
        else:
            return self.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


    def do_POST(self):
        """handles PUT request from client"""

        #parse the url and get the primary key 
        url = self.parse_url(self.path)

        #get the request body JSON for the new data
        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url['requested_resource'] == 'orders':
            successfully_created = create_order(request_body)
            if successfully_created:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)


    def do_PUT(self):
        """handles PUT request from client"""

        #parse the URL and get the primary key
        url = self.parse_url(self.path)
        pk = url['pk']

        #get the request body JSON for the new data
        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url['requested_resource'] == 'orders':
            if pk != 0:
                successfully_updated = update_order(pk, request_body)
                if successfully_updated:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
                
                else:
                    return self.response("Could not update order", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


    def do_DELETE(self):
        """handles DELETE request from client"""

        url = self.parse_url(self.path)
        pk = url['pk']

        if url['requested_resource'] == 'orders':
            if pk != 0:
                successfully_deleted = delete_order(pk)
                if successfully_deleted:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
                
                return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)



#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()