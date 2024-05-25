# utils/footer.py
# Description: This file contains the code to generate the footer HTML code.

def get_footer():
    footer_html = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: px;
    }
    .footer a {
        color: black;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="footer">
        <a href="https://www.linkedin.com/in/shobhit-singhh" target="_blank">LinkedIn</a> ||
        <a href="https://github.com/Shobhit-Singhh" target="_blank">GitHub</a> ||
        <a href="mailto:shobhit22iit@gmail.com" target="_blank">Gmail</a> ||
        <a href="https://codeforces.com/profile/shobhit10" target="_blank">Codeforces</a> ||
        <a href="https://leetcode.com/u/shobhit-singh/" target="_blank">LeetCode</a>
        
        
    </div>
    """
    return footer_html
