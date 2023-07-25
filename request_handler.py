from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from views import create_user, login_user, get_all_categories, get_single_category, create_category, delete_category, update_category, get_all_comments, get_single_comment, create_comment, delete_comment, update_comment, get_all_posts, get_single_post, create_post, delete_post, update_post, get_all_post_tags, get_single_post_tag, create_post_tag, delete_post_tag, update_post_tag, get_all_reactions, get_single_reaction, get_all_post_reactions, get_single_post_reaction, create_post_reaction, get_all_tags, get_single_tag, create_tag, delete_tag, update_tag


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        pass


    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url()

        if resource == 'login':
            response = login_user(post_body)
        elif resource == 'register':
            response = create_user(post_body)
        elif resource == 'categories':
            response = create_category(post_body)
        elif resource == 'comments':
            response = create_comment(post_body)
        elif resource == 'posts':
            response = create_post(post_body)
        elif resource == 'post_tag':
            response = create_post_tag(post_body)
        elif resource == 'tags':
            response = create_tag(post_body)
        elif resource == 'post_reactions':
            response = create_post_reaction(post_body)
        else:
            self._set_headers(404)
            response = f'{{"error": "Resource {resource} not found"}}'
        

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        updated_item = None

        if resource == "category":
            self._set_headers(204)
            updated_item = post_body
            update_category(updated_item, id)

        if resource == "comment":
            self._set_headers(204)
            updated_item = post_body
            update_comment(updated_item, id)

        if resource == "post":
            self._set_headers(204)
            updated_item = post_body
            update_post(updated_item, id)

        if resource == "tag":
            self._set_headers(204)
            updated_item = post_body
            update_tag(updated_item, id)

        if resource == "post_tag":
            self._set_headers(204)
            updated_item = post_body
            update_post_tag(updated_item, id)

        else:
            self._set_headers(404)
            updated_item = {"error": "Resource not found"}


        self.wfile.write((json.dumps(updated_item)).encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        
        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "category":
            self._set_headers(204)
            delete_category(id)

        if resource == "comment":
            self._set_headers(204)
            delete_comment(id)

        if resource == "post":
            self._set_headers(204)
            delete_post(id)

        if resource == "tag":
            self._set_headers(204)
            delete_tag(id)

        if resource == "post_tag":
            self._set_headers(204)
            delete_post_tag(id)

        else:
            self._set_headers(404)
            error_message = "Unable to delete"
            self.wfile.write(error_message.encode())
        
        self.wfile.write("".encode())

  

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
