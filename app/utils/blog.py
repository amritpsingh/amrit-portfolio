import os
import markdown

def get_blog_posts():
    blog_posts = []
    blog_dir = "content/blog"
    for filename in os.listdir(blog_dir):
        if filename.endswith(".md"):
            with open(os.path.join(blog_dir, filename), "r") as file:
                content = file.read()
                html_content = markdown.markdown(content)
                blog_post = {
                    "title": filename.replace(".md", ""),
                    "content": html_content
                }
                blog_posts.append(blog_post)
    return blog_posts