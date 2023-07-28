from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from views import create_user, login_user, get_all_categories, get_single_category, create_category,\
    delete_category, update_category, get_all_comments, get_single_comment, create_comment, delete_comment, update_comment,\
    get_all_posts, get_single_post, create_post, delete_post, update_post, get_all_post_tags, get_single_post_tag,\
    create_post_tag, delete_post_tag, update_post_tag, get_all_reactions, get_single_reaction, get_all_post_reactions,\
    get_all_users, get_single_user, get_post_by_tag, get_posts_by_author, get_posts_by_category, \
    get_single_post_reaction, create_post_reaction, get_all_tags, get_single_tag, create_tag, delete_tag, update_tag, \
    get_single_subscriptions, get_all_subscriptions, create_subscription, delete_subscription, update_user


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
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        parsed = self.parse_url()

        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)

                else:
                    response = get_all_categories()

            if resource == "comments":
                if id is not None:
                    response = get_single_comment(id)

                else:
                    response = get_all_comments()

            if resource == "post_reactions":
                if id is not None:
                    response = get_single_post_reaction(id)

                else:
                    response = get_all_post_reactions()

            if resource == "post_tags":
                if id is not None:
                    response = get_single_post_tag(id)

                else:
                    response = get_all_post_tags()

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)

                else:
                    response = get_all_posts()

            if resource == "reactions":
                if id is not None:
                    response = get_single_reaction(id)

                else:
                    response = get_all_reactions()

            if resource == "tags":
                if id is not None:
                    response = get_single_tag(id)

                else:
                    response = get_all_tags()
            if resource == "users":
                if id is not None:
                    response = get_single_user(id)

                else:
                    response = get_all_users()
        else:
            (resource, key, value) = parsed

            if key == 'tag' and resource == 'posts':
                response = (get_post_by_tag(value))
            if key == 'author' and resource == 'posts':
                response = (get_posts_by_author(value))
            if key == 'category' and resource == 'posts':
                response = (get_posts_by_category(value))

        if resource == "subscriptions":
            if id is not None:
                response = get_single_subscriptions(id)

            else:
                response = get_all_subscriptions()

        self.wfile.write(json.dumps(response).encode())

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
        elif resource == 'post_tags':
            response = create_post_tag(post_body)
        elif resource == 'tags':
            response = create_tag(post_body)
        elif resource == 'post_reactions':
            response = create_post_reaction(post_body)
        elif resource == 'subscriptions':
            response = create_subscription(post_body)
        else:
            self._set_headers(404)
            response = f'{{"error": "Resource {resource} not found"}}'

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url()
        response = {}
        success = False

        if resource == "categories":

            success = update_category(id, post_body)

        elif resource == "comments":

            success = update_comment(id, post_body)

        elif resource == "posts":

            success = update_post(id, post_body)

        elif resource == "tags":

            success = update_tag(id, post_body)

        elif resource == "post_tags":

            success = update_post_tag(id, post_body)
        
        elif resource == "users":

            success = update_user(id, post_body)

        if success:
            self._set_headers(204)

        else:
            self._set_headers(404)
            response = {"error": "Resource not found"}

        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        response = {}
        # Parse the URL
        (resource, id) = self.parse_url()

        if resource == "categories":
            self._set_headers(204)
            response = delete_category(id)

        if resource == "comments":
            self._set_headers(204)
            response = delete_comment(id)

        if resource == "posts":
            self._set_headers(204)
            response = delete_post(id)

        if resource == "tags":
            self._set_headers(204)
            response = delete_tag(id)

        if resource == "post_tags":
            self._set_headers(204)
            response = delete_post_tag(id)

        if resource == "subscriptions":
            self._set_headers(204)
            delete_subscription(id)

        else:
            self._set_headers(404)
            response = 'Resource not found'

        self.wfile.write(json.dumps(response).encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
