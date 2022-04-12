from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if "fit.instructure.com" in flow.request.pretty_host:
        print(flow.request.content)
        if "<button type=\"submit\" class=\"btn btn-primary\" id=\"submit_file_button\">Submit Assignment</button>" in flow.request.content:
            print("The button is here!")
