import os
import nbconvert
import nbformat

def render_jupyter_notebook(notebook_path):
    with open(notebook_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)

    exporter = nbconvert.HTMLExporter()
    html, _ = exporter.from_notebook_node(notebook)
    return html